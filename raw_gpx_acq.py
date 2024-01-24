from serial import Serial
from pyubx2 import UBXReader
from pyubx2.ubxmessage import UBXMessage
import time
from datetime import datetime
import os

# Try mkdir
output_folder = '/home/sommer/Documents/PWV/GPX_logs'
os.makedirs(output_folder, exist_ok=True)

# Open the serial port
stream = Serial('/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00', 9600, timeout=3)

# Create a UBXReader instance
ubr = UBXReader(stream)

# Configure UBX-CFG-MSG to enable only UBX-RXM-RAWX
ubx_cfg_msg = bytes.fromhex("B5620601000100010000")  # Set rates to 0 for all messages
ubx_cfg_msg += bytes.fromhex("B5620601000100020100")  # Enable UBX-RXM-RAWX at 1Hz

# Send the UBX-CFG-MSG command to the u-blox device
stream.write(ubx_cfg_msg)

# Delay
delay = 0.5 # in seconds

# Read the response and save to binary file
while True:
    raw_data, parsed_data = ubr.read()

    # Check if it's a UBX-RXM-RAWX message
    if isinstance(parsed_data, UBXMessage):
        # Save parsed_data to a binary file with datetime isoformat name
        current_time = datetime.utcnow().isoformat()
        file_name = os.path.join(output_folder, f"{current_time}.bin")
            
        with open(file_name, 'wb') as binary_file:
            binary_file.write(parsed_data.serialize())
        print(f"Saved {file_name} at {current_time}")
            
    time.sleep(delay)
