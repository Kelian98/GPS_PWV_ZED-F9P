### Code for Multi-GNSS raw measurements

```python
from serial import Serial
from pyubx2 import UBXReader

stream = Serial('/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00', 9600, timeout=3)

ubr = UBXReader(stream)

(raw_data, parsed_data) = ubr.read()

print(parsed_data)

<UBX(RXM-RAWX, rcvTow=66422.984, week=2298, leapS=18, numMeas=42, leapSec=1, clkReset=0, reserved1=220673, prMes_01=20854699.685791124, cpMes_01=109592186.13122922, doMes_01=-3756.82421875, gnssId_01=GPS, svId_01=5, sigId_01=0, freqId_01=0, locktime_01=0, cno_01=20, prStd_01=10, cpStd_01=15, doStd_01=12, prValid_01=1, cpValid_01=0, halfCyc_01=0, subHalfCyc_01=0, reserved3_01=0, prMes_02=15611803.57169668, cpMes_02=82040577.26329689, doMes_02=-232.724609375, gnssId_02=GPS, svId_02=16, sigId_02=0, freqId_02=0, locktime_02=64500, cno_02=49, prStd_02=3, cpStd_02=1, doStd_02=5, prValid_02=1, cpValid_02=1, halfCyc_02=1, subHalfCyc_02=0, reserved3_02=0, prMes_03=16729262.179294799, cpMes_03=87912850.94739302, doMes_03=-2748.707763671875, gnssId_03=GPS, svId_03=18, sigId_03=0, freqId_03=0, locktime_03=2920, cno_03=26, prStd_03=8, cpStd_03=7, doStd_03=8, prValid_03=1, cpValid_03=1, halfCyc_03=0, subHalfCyc_03=0, reserved3_03=0, prMes_04=18616369.14392781, cpMes_04=97829764.18745126, doMes_04=2575.177001953125, gnssId_04=GPS, svId_04=10, sigId_04=0, freqId_04=0, locktime_04=38060, cno_04=28, prStd_04=8, cpStd_04=7, doStd_04=8, prValid_04=1, cpValid_04=1, halfCyc_04=1, subHalfCyc_04=1, reserved3_04=0, prMes_05=19975695.895894475, cpMes_05=104972929.88442287, doMes_05=-4057.870361328125, gnssId_05=GPS, svId_05=31, sigId_05=0, freqId_05=0, locktime_05=5800, cno_05=28, prStd_05=8, cpStd_05=7, doStd_05=8, prValid_05=1, cpValid_05=1, halfCyc_05=1, subHalfCyc_05=0, reserved3_05=0, prMes_06=34583307.25185277, cpMes_06=180084379.936574, doMes_06=-1686.4600830078125, gnssId_06=BeiDou, svId_06=8, sigId_06=0, freqId_06=0, locktime_06=64500, cno_06=31, prStd_06=6, cpStd_06=6, doStd_06=8, prValid_06=1, cpValid_06=1, halfCyc_06=1, subHalfCyc_06=0, reserved3_06=0, prMes_07=16804542.64296813, cpMes_07=87505660.28660622, doMes_07=-1177.177001953125, gnssId_07=BeiDou, svId_07=35, sigId_07=0, freqId_07=0, locktime_07=64500, cno_07=37, prStd_07=5, cpStd_07=3, doStd_07=7, prValid_07=1, cpValid_07=1, halfCyc_07=1, subHalfCyc_07=0, reserved3_07=0, prMes_08=18178466.72487842, cpMes_08=94660048.68813282, doMes_08=62.7705078125, gnssId_08=BeiDou, svId_08=24, sigId_08=0, freqId_08=0, locktime_08=64500, cno_08=46, prStd_08=3, cpStd_08=1, doStd_08=6, prValid_08=1, cpValid_08=1, halfCyc_08=1, subHalfCyc_08=1, reserved3_08=0, prMes_09=20793087.248262897, cpMes_09=108275017.6872972, doMes_09=-324.788818359375, gnssId_09=BeiDou, svId_09=20, sigId_09=0, freqId_09=0, locktime_09=44080, cno_09=26, prStd_09=6, cpStd_09=9, doStd_09=8, prValid_09=1, cpValid_09=1, halfCyc_09=1, subHalfCyc_09=0, reserved3_09=0, prMes_10=15081636.861099428, cpMes_10=80393614.02445132, doMes_10=399.883544921875, gnssId_10=GLONASS, svId_10=14, sigId_10=0, freqId_10=0, locktime_10=64500, cno_10=53, prStd_10=5, cpStd_10=1, doStd_10=4, prValid_10=1, cpValid_10=1, halfCyc_10=1, subHalfCyc_10=1, reserved3_10=0, prMes_11=19500981.748581197, cpMes_11=104097564.5083074, doMes_11=-4256.14404296875, gnssId_11=GLONASS, svId_11=22, sigId_11=0, freqId_11=4, locktime_11=0, cno_11=22, prStd_11=9, cpStd_11=15, doStd_11=12, prValid_11=1, cpValid_11=0, halfCyc_11=0, subHalfCyc_11=0, reserved3_11=0, prMes_12=15208435.728768507, cpMes_12=81326347.95615959, doMes_12=618.037353515625, gnssId_12=GLONASS, svId_12=24, sigId_12=0, freqId_12=9, locktime_12=64500, cno_12=53, prStd_12=5, cpStd_12=1, doStd_12=4, prValid_12=1, cpValid_12=1, halfCyc_12=1, subHalfCyc_12=1, reserved3_12=0, prMes_13=17208353.741621707, cpMes_13=90430534.20004773, doMes_13=1134.921630859375, gnssId_13=GPS, svId_13=23, sigId_13=0, freqId_13=0, locktime_13=45540, cno_13=29, prStd_13=6, cpStd_13=5, doStd_13=8, prValid_13=1, cpValid_13=1, halfCyc_13=1, subHalfCyc_13=1, reserved3_13=0, prMes_14=19628523.36088611, cpMes_14=103148552.26427178, doMes_14=2382.314453125, gnssId_14=GPS, svId_14=8, sigId_14=0, freqId_14=0, locktime_14=64500, cno_14=38, prStd_14=5, cpStd_14=2, doStd_14=7, prValid_14=1, cpValid_14=1, halfCyc_14=1, subHalfCyc_14=1, reserved3_14=0, prMes_15=18341797.4357237, cpMes_15=95510570.0039958, doMes_15=-2858.26025390625, gnssId_15=BeiDou, svId_15=26, sigId_15=0, freqId_15=0, locktime_15=64500, cno_15=32, prStd_15=6, cpStd_15=5, doStd_15=8, prValid_15=1, cpValid_15=1, halfCyc_15=1, subHalfCyc_15=1, reserved3_15=0, prMes_16=33713916.93293233, cpMes_16=175557160.3786531, doMes_16=-1292.056640625, gnssId_16=BeiDou, svId_16=13, sigId_16=0, freqId_16=0, locktime_16=64500, cno_16=37, prStd_16=5, cpStd_16=3, doStd_16=7, prValid_16=1, cpValid_16=1, halfCyc_16=1, subHalfCyc_16=1, reserved3_16=0, prMes_17=15525003.213381032, cpMes_17=83048384.08169048, doMes_17=-2882.10693359375, gnssId_17=GLONASS, svId_17=23, sigId_17=0, freqId_17=10, locktime_17=64500, cno_17=40, prStd_17=5, cpStd_17=2, doStd_17=7, prValid_17=1, cpValid_17=1, halfCyc_17=1, subHalfCyc_17=0, reserved3_17=0, prMes_18=18392641.996812478, cpMes_18=98457252.93581213, doMes_18=-1.434326171875, gnssId_18=GLONASS, svId_18=7, sigId_18=0, freqId_18=12, locktime_18=64500, cno_18=37, prStd_18=6, cpStd_18=3, doStd_18=7, prValid_18=1, cpValid_18=1, halfCyc_18=1, subHalfCyc_18=0, reserved3_18=0, prMes_19=18495669.284726985, cpMes_19=98835242.24916908, doMes_19=3356.29736328125, gnssId_19=GLONASS, svId_19=15, sigId_19=0, freqId_19=7, locktime_19=64500, cno_19=41, prStd_19=5, cpStd_19=2, doStd_19=7, prValid_19=1, cpValid_19=1, halfCyc_19=1, subHalfCyc_19=0, reserved3_19=0, prMes_20=18971400.259256113, cpMes_20=101519766.38841173, doMes_20=2662.841796875, gnssId_20=GLONASS, svId_20=17, sigId_20=0, freqId_20=11, locktime_20=64500, cno_20=37, prStd_20=6, cpStd_20=3, doStd_20=7, prValid_20=1, cpValid_20=1, halfCyc_20=1, subHalfCyc_20=0, reserved3_20=0, prMes_21=16512405.924950635, cpMes_21=86773294.64092542, doMes_21=4355.8857421875, gnssId_21=Galileo, svId_21=14, sigId_21=0, freqId_21=0, locktime_21=64500, cno_21=46, prStd_21=3, cpStd_21=1, doStd_21=6, prValid_21=1, cpValid_21=1, halfCyc_21=1, subHalfCyc_21=0, reserved3_21=0, prMes_22=18380141.015057188, cpMes_22=96588264.44795445, doMes_22=-526.4970703125, gnssId_22=Galileo, svId_22=26, sigId_22=0, freqId_22=0, locktime_22=64500, cno_22=30, prStd_22=6, cpStd_22=6, doStd_22=8, prValid_22=1, cpValid_22=1, halfCyc_22=1, subHalfCyc_22=0, reserved3_22=0, prMes_23=21187892.68084906, cpMes_23=111343116.13846672, doMes_23=1762.8394775390625, gnssId_23=Galileo, svId_23=31, sigId_23=0, freqId_23=0, locktime_23=64500, cno_23=39, prStd_23=4, cpStd_23=2, doStd_23=6, prValid_23=1, cpValid_23=1, halfCyc_23=1, subHalfCyc_23=0, reserved3_23=0, prMes_24=20734006.970225196, cpMes_24=108958071.69375268, doMes_24=-2960.547119140625, gnssId_24=Galileo, svId_24=13, sigId_24=0, freqId_24=0, locktime_24=64500, cno_24=27, prStd_24=7, cpStd_24=8, doStd_24=8, prValid_24=1, cpValid_24=1, halfCyc_24=1, subHalfCyc_24=0, reserved3_24=0, prMes_25=20609842.79907891, cpMes_25=108305405.33013351, doMes_25=1664.2969970703125, gnssId_25=Galileo, svId_25=33, sigId_25=0, freqId_25=0, locktime_25=64500, cno_25=41, prStd_25=4, cpStd_25=2, doStd_25=6, prValid_25=1, cpValid_25=1, halfCyc_25=1, subHalfCyc_25=0, reserved3_25=0, prMes_26=20734052.567869857, cpMes_26=83487436.9260775, doMes_26=-2262.721923828125, gnssId_26=Galileo, svId_26=13, sigId_26=6, freqId_26=0, locktime_26=0, cno_26=23, prStd_26=9, cpStd_26=15, doStd_26=12, prValid_26=1, cpValid_26=0, halfCyc_26=0, subHalfCyc_26=0, reserved3_26=0, prMes_27=20550030.412737843, cpMes_27=82746455.54231697, doMes_27=-2341.233642578125, gnssId_27=Galileo, svId_27=21, sigId_27=6, freqId_27=0, locktime_27=28660, cno_27=29, prStd_27=6, cpStd_27=7, doStd_27=8, prValid_27=1, cpValid_27=1, halfCyc_27=1, subHalfCyc_27=0, reserved3_27=0, prMes_28=18380137.876198128, cpMes_28=74009208.47670433, doMes_28=-403.876708984375, gnssId_28=Galileo, svId_28=26, sigId_28=6, freqId_28=0, locktime_28=64500, cno_28=37, prStd_28=4, cpStd_28=3, doStd_28=7, prValid_28=1, cpValid_28=1, halfCyc_28=1, subHalfCyc_28=0, reserved3_28=0, prMes_29=21187897.14602708, cpMes_29=85314920.45453669, doMes_29=1350.745361328125, gnssId_29=Galileo, svId_29=31, sigId_29=6, freqId_29=0, locktime_29=64500, cno_29=36, prStd_29=5, cpStd_29=3, doStd_29=7, prValid_29=1, cpValid_29=1, halfCyc_29=1, subHalfCyc_29=0, reserved3_29=0, prMes_30=20609846.722881377, cpMes_30=82987342.88580343, doMes_30=1275.03173828125, gnssId_30=Galileo, svId_30=33, sigId_30=6, freqId_30=0, locktime_30=64500, cno_30=44, prStd_30=3, cpStd_30=1, doStd_30=6, prValid_30=1, cpValid_30=1, halfCyc_30=1, subHalfCyc_30=0, reserved3_30=0, prMes_31=33713940.27429444, cpMes_31=135752066.77046952, doMes_31=-998.819091796875, gnssId_31=BeiDou, svId_31=13, sigId_31=2, freqId_31=0, locktime_31=0, cno_31=17, prStd_31=10, cpStd_31=15, doStd_31=12, prValid_31=1, cpValid_31=0, halfCyc_31=0, subHalfCyc_31=0, reserved3_31=0, prMes_32=16512408.335609822, cpMes_32=66488642.696004964, doMes_32=3337.70068359375, gnssId_32=Galileo, svId_32=14, sigId_32=6, freqId_32=0, locktime_32=64500, cno_32=52, prStd_32=3, cpStd_32=1, doStd_32=4, prValid_32=1, cpValid_32=1, halfCyc_32=1, subHalfCyc_32=0, reserved3_32=0, prMes_33=34583300.04674833, cpMes_33=139252529.9519698, doMes_33=-1303.5205078125, gnssId_33=BeiDou, svId_33=8, sigId_33=2, freqId_33=0, locktime_33=64500, cno_33=33, prStd_33=5, cpStd_33=5, doStd_33=8, prValid_33=1, cpValid_33=1, halfCyc_33=1, subHalfCyc_33=1, reserved3_33=0, prMes_34=16729228.59064775, cpMes_34=68503393.77229066, doMes_34=-2130.47412109375, gnssId_34=GPS, svId_34=18, sigId_34=3, freqId_34=0, locktime_34=0, cno_34=15, prStd_34=10, cpStd_34=15, doStd_34=13, prValid_34=1, cpValid_34=0, halfCyc_34=0, subHalfCyc_34=0, reserved3_34=0, prMes_35=15081639.930081703, cpMes_35=62528398.12464517, doMes_35=310.91650390625, gnssId_35=GLONASS, svId_35=14, sigId_35=2, freqId_35=0, locktime_35=64500, cno_35=49, prStd_35=5, cpStd_35=1, doStd_35=5, prValid_35=1, cpValid_35=1, halfCyc_35=1, subHalfCyc_35=1, reserved3_35=0, prMes_36=19501004.85890242, cpMes_36=80964868.55655874, doMes_36=-3313.555419921875, gnssId_36=GLONASS, svId_36=22, sigId_36=2, freqId_36=4, locktime_36=0, cno_36=21, prStd_36=9, cpStd_36=15, doStd_36=12, prValid_36=1, cpValid_36=0, halfCyc_36=0, subHalfCyc_36=0, reserved3_36=0, prMes_37=15208434.712907294, cpMes_37=63253833.41048642, doMes_37=480.66650390625, gnssId_37=GLONASS, svId_37=24, sigId_37=2, freqId_37=9, locktime_37=64500, cno_37=47, prStd_37=5, cpStd_37=1, doStd_37=5, prValid_37=1, cpValid_37=1, halfCyc_37=1, subHalfCyc_37=0, reserved3_37=0, prMes_38=17208371.457243014, cpMes_38=70465403.85874805, doMes_38=882.040771484375, gnssId_38=GPS, svId_38=23, sigId_38=3, freqId_38=0, locktime_38=0, cno_38=23, prStd_38=9, cpStd_38=15, doStd_38=12, prValid_38=1, cpValid_38=0, halfCyc_38=0, subHalfCyc_38=0, reserved3_38=0, prMes_39=19628526.788827542, cpMes_39=80375539.53815998, doMes_39=1856.5040283203125, gnssId_39=GPS, svId_39=8, sigId_39=3, freqId_39=0, locktime_39=64500, cno_39=33, prStd_39=6, cpStd_39=5, doStd_39=8, prValid_39=1, cpValid_39=1, halfCyc_39=1, subHalfCyc_39=0, reserved3_39=0, prMes_40=18392649.958921965, cpMes_40=76577885.93375795, doMes_40=-1.24853515625, gnssId_40=GLONASS, svId_40=7, sigId_40=2, freqId_40=12, locktime_40=5040, cno_40=28, prStd_40=8, cpStd_40=7, doStd_40=8, prValid_40=1, cpValid_40=1, halfCyc_40=1, subHalfCyc_40=0, reserved3_40=0, prMes_41=18495670.53278722, cpMes_41=76871761.6534265, doMes_41=2610.562744140625, gnssId_41=GLONASS, svId_41=15, sigId_41=2, freqId_41=7, locktime_41=64500, cno_41=42, prStd_41=5, cpStd_41=1, doStd_41=6, prValid_41=1, cpValid_41=1, halfCyc_41=1, subHalfCyc_41=0, reserved3_41=0, prMes_42=18971405.220094472, cpMes_42=78959940.01933555, doMes_42=2071.185302734375, gnssId_42=GLONASS, svId_42=17, sigId_42=2, freqId_42=11, locktime_42=64500, cno_42=40, prStd_42=5, cpStd_42=2, doStd_42=7, prValid_42=1, cpValid_42=1, halfCyc_42=1, subHalfCyc_42=0, reserved3_42=0)>

# To save in binary file
with open('/home/sommer/Documents/PWV/sample_raw_gpx_data.bin', 'wb') as binary_file:
    binary_file.write(raw_data)
    
# To read from binary file
r_stream = open('/home/sommer/Documents/PWV/sample_raw_gpx_data.bin', 'rb')

ubr2 = UBXReader(r_stream, protfilter=2)

(raw_data2, parsed_data2) = ubr2.read()

```

From u-blox F9 HPG 1.32 Interface Description (page 188, section 3.17.6) :

Message		UBX-RXM-RAWX

Type			Periodic/polled

Comment		**This message contains the information needed to be able to generate a RINEX 3 multi-GNSS observation file**
(see ftp://ftp.igs.org/pub/data/format/). This message contains pseudorange, Doppler, carrier phase, phase lock and signal quality information for
GNSS satellites once signals have been synchronized. This message supports all active GNSS.

### Convert UBX binary file to RINEX

Install RTKLIB with `sudo apt install rtklib`

In CMD : `convbin sample_raw_gpx_data.bin -r ubx`

Normally, a file named `sample_raw_gpx_data.obs` should appear

```bash
base) sommer@portable-sommer:~/Documents/PWV$ convbin sample_raw_gpx_data.bin -r ubx
input file  : sample_raw_gpx_data.bin (u-blox UBX)
->rinex obs : sample_raw_gpx_data.obs
->rinex nav : sample_raw_gpx_data.nav
->sbas log  : sample_raw_gpx_data.sbs


2024/01/21 18:27:03: O=1 
(base) sommer@portable-sommer:~/Documents/PWV$ ll | grep sample_raw
   rw-rw-r--    1   sommer   sommer      1 KiB   Sun Jan 21 21:42:45 2024    sample_raw_gpx_data.bin 
   rw-rw-r--    1   sommer   sommer      4 KiB   Sun Jan 21 22:11:37 2024    sample_raw_gpx_data.obs 
   rw-rw-r--    1   sommer   sommer      1 KiB   Sun Jan 21 21:42:14 2024    sample_raw_gpx_data.txt 

```

### Download IGS data products

Download GNSS Products and Data with RTKGET

### Write to the device

```python
from pyubx2 import UBXMessage, SET
from serial import Serial

serialOut = Serial('/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00', 115200, timeout=5)

# msg = UBXMessage('CFG','CFG-MSG', SET, msgClass=0xf0, msgID=0x01, rateUART1=1, rateUSB=1)

msg = UBXMessage('CFG','CFG-MSG', SET, msgClass=0x02, msgID=0x15)

msg = UBXMessage('CFG','CFG-MSG', SET, msgClass=0x02, msgID=0x15)

output = msg.serialize()


serialOut.write(output)


CFG_MSGOUT_UBX_RXM_RAWX_USB

0X209102a7




```

![image-20240122120826986](/home/sommer/.config/Typora/typora-user-images/image-20240122120826986.png)

### ChatGPT

To enable UBX-RXM-RAWX measurements with a u-blox device, you need to send the appropriate configuration message to the device. The configuration message is a UBX-CFG-MSG message. Below is the bytearray command to enable UBX-RXM-RAWX:

```python
from serial import Serial
from pyubx2 import UBXReader
import time

# Define the UBX-CFG-MSG message to enable UBX-RXM-RAWX
ubx_cfg_msg = bytes.fromhex("B5620601000100010001")

# Open the serial port
stream = Serial('/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00', 9600, timeout=3)

# Send the UBX-CFG-MSG command to the u-blox device
stream.write(ubx_cfg_msg)
```

Explanation of the hex string:

- B5 62: UBX Sync characters.
- 06 01: CFG class and MSG message ID.
- 00 01: Rate divisor (1) - how often the message is sent.
- 00 01: UBX-RXM-RAWX message ID.
- 00 01: Enable (1) the message.

This command configures the u-blox device to send UBX-RXM-RAWX messages at a rate of 1Hz. Adjust the rate divisor according to your desired update rate. The command will be sent as a bytearray to the u-blox device using the `write` method on the serial port.

Please note that directly manipulating the device configuration can have consequences, and you should be careful while doing so. Make sure you have a good understanding of the u-blox protocol and the implications of the changes you are making.

### pyubx2

```python
from pyubx2 import UBXMessage, UBXReader

# layers - 1 = Volatile RAM, 2 = Battery-Backed RAM (BBR), 4 = External Flash (may be OR'd)
layers = 1

# transaction - 0 = None, 1 = Start, 2 = Ongoing, 3 = Commit
transaction = 1

# "CFG_MSGOUT_UBX_RXM_RAWX_USB": (0x209102A7, U1)
cfgData = [("CFG_MSGOUT_UBX_RXM_RAWX_USB", 1), (0x209102A7, 1)]


msg = UBXMessage.config_set(layers, transaction, cfgData)

print(msg)

serialOut.write(msg.serialize())


ubr = UBXReader(serialOut)

(raw_data, parsed_data) = ubr.read()

print(parsed_data)
```

## Utility Methods

`pyubx2` provides the following utility methods (via the `pynmeagps` library):

- `latlon2dms` - converts decimal lat/lon to degrees, minutes, decimal seconds format e.g. "53°20′45.6″N", "2°32′46.68″W"
- `latlon2dmm` - converts decimal lat/lon to degrees, decimal minutes format e.g. "53°20.76′N", "2°32.778′W"
- `ecef2llh` - converts ECEF (X, Y, Z) coordinates to geodetic (lat, lon, ellipsoidal height) coordinates
- `llh2ecef` - converts geodetic (lat, lon, ellipsoidal height) coordinates to ECEF (X, Y, Z) coordinates
- `haversine` - finds spherical distance in km between two sets of (lat, lon) coordinates
- `bearing` - finds bearing in degrees between two sets of (lat, lon) coordinates
- `cel2cart` - converts celestial coordinates (elevation, azimuth) to cartesian coordinations (X,Y)

### ChatGPT 2

Certainly! If you want to keep the serial port open after the script finishes, you can remove the `stream.close()` line from the `finally` block. Here's the modified script without the port closure:

```python
from serial import Serial
from pyubx2 import UBXReader
from pyubx2.ubxmessage import UBXMessage
import time

# Open the serial port
stream = Serial('/dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00', 9600, timeout=3)

# Create a UBXReader instance
ubr = UBXReader(stream)

# Configure UBX-CFG-MSG to enable only UBX-RXM-RAWX
ubx_cfg_msg = bytes.fromhex("B5620601000100010000")  # Set rates to 0 for all messages
ubx_cfg_msg += bytes.fromhex("B5620601000100020100")  # Enable UBX-RXM-RAWX at 1Hz

# Send the UBX-CFG-MSG command to the u-blox device
stream.write(ubx_cfg_msg)

# Read the response
while True:
    raw_data, parsed_data = ubr.read()

    if isinstance(parsed_data, UBXMessage):
        # Check if it's a UBX-RXM-RAWX message
        print(parsed_data)  # Output the UBX-RXM-RAWX message
      
    time.sleep(0.5)
```

Now, the script does not close the serial port explicitly, allowing you to keep it open as needed.

### Final script

```python
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

```

```python
>>> from pyubx2 import UBXReader
>>> stream = open('ubxdata.bin', 'rb')
>>> ubr = UBXReader(stream, protfilter=2)
>>> for (raw_data, parsed_data) in ubr: print(parsed_data)
```

![image-20240124000104733](/home/sommer/.config/Typora/typora-user-images/image-20240124000104733.png)

CFG-MSGOUT-UBX_RXM_SFRBX_USB

​    "CFG_MSGOUT_UBX_RXM_SFRBX_USB": (0x20910234, U1),

![image-20240124000438913](/home/sommer/.config/Typora/typora-user-images/image-20240124000438913.png)


layers = 1
transaction = 0
cfg_data = []
for port_type in ("USB", "UART1"):
    cfg_data.append((f"CFG_{port_type}OUTPROT_NMEA", not enable))
    cfg_data.append((f"CFG_{port_type}OUTPROT_UBX", enable))
    cfg_data.append((f"CFG_MSGOUT_UBX_NAV_PVT_{port_type}", enable))
    cfg_data.append((f"CFG_MSGOUT_UBX_NAV_SAT_{port_type}", enable * 4))
    cfg_data.append((f"CFG_MSGOUT_UBX_NAV_DOP_{port_type}", enable * 4))
    cfg_data.append((f"CFG_MSGOUT_UBX_RXM_RTCM_{port_type}", enable))

msg = UBXMessage.config_set(layers, transaction, cfg_data)
self.sendqueue.put((msg.serialize(), msg))