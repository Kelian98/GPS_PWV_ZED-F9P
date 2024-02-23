"""
ubxpoller.py

This example illustrates how to read, write and display UBX messages
"concurrently" using threads and queues. This represents a useful
generic pattern for many end user applications.

It implements two threads which run concurrently:
1) an I/O thread which continuously reads UBX data from the
receiver and sends any queued outbound command or poll messages.
2) a process thread which processes parsed UBX data - in this example
it simply prints the parsed data to the terminal.
UBX data is passed between threads using queues.

Press CTRL-C to terminate.

FYI: Since Python implements a Global Interpreter Lock (GIL),
threads are not strictly concurrent, though this is of minor
practical consequence here. True concurrency could be
achieved using multiprocessing (i.e. separate interpreter
processes rather than threads) but this is non-trivial in
this context as serial streams cannot be shared between
processes. A discrete hardware I/O process must be implemented
e.g. using RPC server techniques.

Write each day data in a separate file and update automatically.

"""

# pylint: disable=invalid-name

import os
import time
from queue import Queue
from sys import platform
from threading import Event, Lock, Thread
from serial import Serial
from pyubx2 import (
    UBX_PROTOCOL,
    UBXMessage,
    UBXReader,
    VALNONE,
)
from datetime import datetime, timedelta, timezone
from utilities import *


# Constants
BAUDRATE = 460800  # 115200
TIMEOUT = 5  # in seconds
LAYERS = 1
TRANSACTION = 0
ENABLE = 1
PORT_TYPE = "USB"
SAMPLE_RATE = 1000  # e.g. scale ms (0.001s) 100 = 10Hz, 1000 = 1 Hz
NAV_RATE = 5  # e.g. 5 means five measurements for every navigation solution. The minimum value is 1. The maximum value is 127.
DELAY = 1


def io_data(
    stream: object,
    ubr: UBXReader,
    readqueue: Queue,
    stop: Event,
):
    """
    THREADED
    Read and parse inbound UBX data and place
    raw and parsed data on queue.

    Send any queued outbound messages to receiver.
    """
    # pylint: disable=broad-exception-caught

    while not stop.is_set():
        if stream.in_waiting:
            try:
                (raw_data, parsed_data) = ubr.read()

                if parsed_data and "UNKNOWN PROTOCOL" not in str(parsed_data):
                    # print(parsed_data)
                    readqueue.put((raw_data, parsed_data))

                elif "UNKNOWN PROTOCOL" in str(parsed_data):
                    print(f"{datetime.utcnow().isoformat()} : WARNING : CORRUPTED DATA = {str(parsed_data)}, SKIPPING...")
                    time.sleep(DELAY)

            except Exception as err:
                print(f"\n\nSomething went wrong {err}\n\n")
                continue


def process_data(queue: Queue, stop: Event, filename: str):
    """
    THREADED
    Get UBX data from queue and display.
    """

    with open(filename, "ab") as binary_file:
        while not stop.is_set():
            if queue.empty() is False:
                (raw_data, parsed) = queue.get()
                # print(parsed)
                binary_file.write(raw_data)
                queue.task_done()


def generate_filename(data_path="/mnt/data/gnss/raw"):
    os.makedirs(data_path, exist_ok=True)
    return os.path.join(
        data_path, datetime.now(timezone.utc).strftime("%Y-%m-%d") + ".ubx"
    )


def check_file_exists(filename):
    """
    Check if a file exists.
    If the file exists, append a suffix with the current time (HH_MM_SS) to the filename.
    Returns the modified filename.
    """
    if os.path.exists(filename):
        # Get current time
        current_time = datetime.now().strftime("%H_%M_%S")
        # Split the filename and extension
        base, ext = os.path.splitext(filename)
        # Add the suffix with current time
        new_filename = f"{base}_{current_time}{ext}"
        return new_filename
    else:
        return filename


if __name__ == "__main__":

    # set port, BAUDRATE and TIMEOUT to suit your device configuration
    if platform == "win32":  # Windows
        PORT = "COM13"
    elif platform == "darwin":  # MacOS
        PORT = "/dev/tty.usbmodem101"
    else:  # Linux
        PORT = (
            "/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00"
        )

    # First iteration
    # Get filename to write the UBX raw data
    filename = generate_filename()
    # Failsafe : if reboot during the day, create new filename with time of reboot
    filename = check_file_exists(filename)
    old_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%d")


    with Serial(PORT, BAUDRATE, timeout=TIMEOUT) as serial_stream:

        ubxreader = UBXReader(serial_stream, protfilter=UBX_PROTOCOL, validate=VALNONE)

        # Configure to output RAW UBX data
        cfg_data = []
        cfg_data.append((f"CFG_{PORT_TYPE}OUTPROT_NMEA", not ENABLE))
        cfg_data.append((f"CFG_{PORT_TYPE}OUTPROT_RTCM3X", not ENABLE))
        cfg_data.append((f"CFG_{PORT_TYPE}OUTPROT_UBX", ENABLE))
        cfg_data.append((f"CFG_MSGOUT_UBX_RXM_RAWX_{PORT_TYPE}", ENABLE))
        cfg_data.append((f"CFG_MSGOUT_UBX_RXM_SFRBX_{PORT_TYPE}", ENABLE))
        cfg_data.append((f"CFG_RATE_MEAS", SAMPLE_RATE))
        cfg_data.append((f"CFG_RATE_NAV", NAV_RATE))

        msg = UBXMessage.config_set(LAYERS, TRANSACTION, cfg_data)
        print(msg)

        serial_stream.write(msg.serialize())

        serial_lock = Lock()
        read_queue = Queue()
        stop_event = Event()

        io_thread = Thread(
            target=io_data,
            args=(
                serial_stream,
                ubxreader,
                read_queue,
                stop_event,
            ),
        )
        process_thread = Thread(
            target=process_data,
            args=(
                read_queue,
                stop_event,
                filename,
            ),
        )

        print("\nStarting handler threads. Press Ctrl-C to terminate...")
        io_thread.start()
        process_thread.start()

        # loop until user presses Ctrl-C
        while not stop_event.is_set():
            try:
                # Get new date time
                new_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%d")

                # Compare the actual datetime with previous datetime.
                # If Midnight passed, update the old_datetime variable and filename
                # Stop writing in the old file, and reinstantiate the threads.
                if new_datetime != old_datetime:

                    # Update datetime
                    old_datetime = new_datetime
                    current_filename = generate_filename()

                    filename = current_filename
                    print(
                        f"{GREEN}New filename: {filename}, restarting threads...{RESET_COLOR}"
                    )
                    time.sleep(DELAY)

                    # Stop current threads
                    stop_event.set()
                    io_thread.join()
                    process_thread.join()

                    # Restart all threads
                    serial_lock = Lock()
                    read_queue = Queue()
                    stop_event = Event()

                    io_thread = Thread(
                        target=io_data,
                        args=(
                            serial_stream,
                            ubxreader,
                            read_queue,
                            stop_event,
                        ),
                    )
                    process_thread = Thread(
                        target=process_data,
                        args=(
                            read_queue,
                            stop_event,
                            filename,
                        ),
                    )

                    print("\nStarting handler threads. Press Ctrl-C to terminate...")
                    io_thread.start()
                    process_thread.start()

            except KeyboardInterrupt:  # capture Ctrl-C
                print("\n\nTerminated by user.")
                stop_event.set()

        print(
            f"\n{RED}Stop signal set. Waiting for threads to complete...{RESET_COLOR}"
        )
        io_thread.join()
        process_thread.join()
        print(
            f"\n{GREEN}Processing complete {datetime.now(timezone.utc).isoformat()}{RESET_COLOR}"
        )
