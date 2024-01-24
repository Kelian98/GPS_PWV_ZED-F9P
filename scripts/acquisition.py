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

Created on 07 Aug 2021

:author: semuadmin
:copyright: SEMU Consulting © 2021
:license: BSD 3-Clause
"""
# pylint: disable=invalid-name

from queue import Queue
from sys import platform
from threading import Event, Lock, Thread
from time import sleep
from serial import Serial
from pyubx2 import POLL, UBX_PROTOCOL, UBXMessage, UBXReader, UBX_PAYLOADS_POLL
from datetime import datetime

# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
ORANGE = "\033[93m"
CYAN = "\033[96m"
RESET_COLOR = "\033[0m"

def io_data(
    stream: object,
    ubr: UBXReader,
    readqueue: Queue,
    sendqueue: Queue,
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
                if parsed_data:
                    readqueue.put((raw_data, parsed_data))

                # refine this if outbound message rates exceed inbound
                while not sendqueue.empty():
                    data = sendqueue.get(False)
                    if data is not None:
                        ubr.datastream.write(data.serialize())
                    sendqueue.task_done()

            except Exception as err:
                print(f"\n\nSomething went wrong {err}\n\n")
                continue


def process_data(queue: Queue, stop: Event, filename: str):
    """
    THREADED
    Get UBX data from queue and display.
    """

    with open(filename, 'ab') as binary_file:
        while not stop.is_set():
            if queue.empty() is False:
                (raw_data, parsed) = queue.get()
                print(parsed)
                binary_file.write(raw_data)
                queue.task_done()


if __name__ == "__main__":
    # set port, baudrate and timeout to suit your device configuration
    if platform == "win32":  # Windows
        port = "COM13"
    elif platform == "darwin":  # MacOS
        port = "/dev/tty.usbmodem101"
    else:  # Linux
        port = "/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00"

    # Constants
    baudrate = 115200
    timeout = 1
    layers = 1
    transaction = 0
    enable = 1
    port_type = "USB"
    sample_rate = 250 #e.g. scale ms (0.001s) 100 = 10Hz, 1000 = 1 Hz
    nav_rate = 4 #e.g. 5 means five measurements for every navigation solution. The minimum value is 1. The maximum value is 127.
    DELAY = 1

    # Filename to write the UBX raw data
    filename = datetime.utcnow().isoformat() + ".ubx"

    with Serial(port, baudrate, timeout=timeout) as serial_stream:

        ubxreader = UBXReader(serial_stream, protfilter=UBX_PROTOCOL)

        cfg_data = []
        cfg_data.append((f"CFG_{port_type}OUTPROT_NMEA", not enable))
        cfg_data.append((f"CFG_{port_type}OUTPROT_RTCM3X", not enable))
        cfg_data.append((f"CFG_{port_type}OUTPROT_UBX", enable))
        cfg_data.append((f"CFG_MSGOUT_UBX_RXM_RAWX_{port_type}", enable))
        cfg_data.append((f"CFG_MSGOUT_UBX_RXM_SFRBX_{port_type}", enable))
        cfg_data.append((f"CFG_RATE_MEAS", sample_rate))
        cfg_data.append((f"CFG_RATE_NAV", nav_rate))

        msg = UBXMessage.config_set(layers, transaction, cfg_data)
        print(msg)

        serial_stream.write(msg.serialize())

        serial_lock = Lock()
        read_queue = Queue()
        send_queue = Queue()
        stop_event = Event()

        io_thread = Thread(
            target=io_data,
            args=(
                serial_stream,
                ubxreader,
                read_queue,
                send_queue,
                stop_event,
            ),
        )
        process_thread = Thread(
            target=process_data,
            args=(
                read_queue,
                stop_event, filename,
            ),
        )

        print("\nStarting handler threads. Press Ctrl-C to terminate...")
        io_thread.start()
        process_thread.start()

        # loop until user presses Ctrl-C
        while not stop_event.is_set():
            try:
                # DO STUFF IN THE BACKGROUND...
                # poll all available NAV messages (receiver will only respond
                # to those NAV message types it supports; responses won't
                # necessarily arrive in sequence)
                count = 0
                for nam in UBX_PAYLOADS_POLL:
                    if nam[0:4] == "NAV-":
                        print(f"Polling {nam} message type...")
                        msg = UBXMessage("NAV", nam, POLL)
                        send_queue.put(msg)
                        count += 1
                        sleep(DELAY)
                #stop_event.set()
                print(f"{GREEN}{datetime.utcnow().isoformat()} | {count} NAV message types polled.{RESET_COLOR}")

            except KeyboardInterrupt:  # capture Ctrl-C
                print("\n\nTerminated by user.")
                stop_event.set()

        print(f"\n{RED}Stop signal set. Waiting for threads to complete...{RESET_COLOR}")
        io_thread.join()
        process_thread.join()
        print(f"\n{GREEN}Processing complete {datetime.utcnow().isoformat()}{RESET_COLOR}")
