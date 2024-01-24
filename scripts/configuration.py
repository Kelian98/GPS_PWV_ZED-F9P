from serial import Serial
from pyubx2 import UBXReader, UBXMessage

serialOut = Serial('/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00', 115200, timeout=3)

ubr = UBXReader(serialOut)

# CONFIGURE THE RECEIVER TO OUTPUT THE DESIRED DATA
layers = 1
transaction = 0
enable = 1
port_type = "USB"
sample_rate = 250 #e.g. scale ms (0.001s) 100 = 10Hz, 1000 = 1 Hz
nav_rate = 4 #e.g. 5 means five measurements for every navigation solution. The minimum value is 1. The maximum value is 127.

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

serialOut.write(msg.serialize())
