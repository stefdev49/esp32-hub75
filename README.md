# esp32-hub75
esp32 + HUB75 with micropython


## connecting device

```shell
stef@pop-os:~/repos_github/esp32-hub75$ lsusb
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
...
Bus 001 Device 004: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
...
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
stef@pop-os:~/repos_github/esp32-hub75$ ls -l /dev/ttyUSB0 
crw-rw---- 1 root dialout 188, 0 Dec 22 11:51 /dev/ttyUSB0
```

```shell
adduser stef dialout
```

## flashing

Following this [doc](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)

### erase flash

```shell
stef@pop-os:~$ poetry run  esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py v4.8.1
Serial port /dev/ttyUSB0
Connecting.....
Detecting chip type... Unsupported detection protocol, switching and trying again...
Connecting.........
Detecting chip type... ESP32
Chip is ESP32-D0WDQ6 (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: a4:cf:12:9a:04:dc
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 8.7s
Hard resetting via RTS pin...
```

### flas with micropython

```shell
stef@pop-os:~$ poetry run esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ~/Downloads/ESP32_GENERIC-20241129-v1.24.1.bin
esptool.py v4.8.1
Serial port /dev/ttyUSB0
Connecting.....
Chip is ESP32-D0WDQ6 (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
WARNING: Detected crystal freq 41.13MHz is quite different to normalized freq 40MHz. Unsupported crystal in use?
Crystal is 40MHz
MAC: a4:cf:12:9a:04:dc
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Flash will be erased from 0x00001000 to 0x0019efff...
Compressed 1691664 bytes to 1109554...
Wrote 1691664 bytes (1109554 compressed) at 0x00001000 in 98.2 seconds (effective 137.8 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

## connecting

[mpremote doc](https://docs.micropython.org/en/latest/reference/mpremote.html)

```shell
stef@pop-os:~$ poetry run mpremote fs ls
ls :
         139 boot.py
stef@pop-os:~$ poetry run mpremote cat boot.py
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
```

## run

### blink

```shell
mpremote run src/blink.py
```

### 32x64 lcd panel

```bash
(esp32hub75-py3.10) stef@pop-os:~/repos_github/esp32-hub75/src$ mpremote cp *.py :
cp blink.py :
cp hub75.py :
Up to date: ./hub75.py
cp logo.py :
cp main.py :                            
cp matrixdata.py :
(esp32hub75-py3.10) stef@pop-os:~/repos_github/esp32-hub75/src$ mpremote run main.py
```

## HUB75 protocol

The basic operation of the display:

    Select the current row with the pins A, B, C, D
    Place the corresponding bit for the R1, G1 and B1 channels on the input, then shift it into the display by bringing CLK up and down
    When the current row is complete, bring LATCH up and down

This lets you display an entire row of data. Repeat this with different values for A/B/C/D and you can shift in an entire bit plane.

1. Clock in data for entire row (use R1,G1,B1,R2,G2,B2 for data and CLK for clock)
2. OE high
3. Select line address (A,B,C,D)
4. LAT high
5. LAT low
6. OE low

Repeat for each line

![diagramme](doc/matrix_wave-1.png)