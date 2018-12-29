# litscpi
This library provides minimilistic control for devices that one can control over SCPI. This code is written specifically for controlling IT6412. One may find the programming manual at http://www.itechate.com/Upload/File/20171023133402.pdf
# Installation
```
python setup.py install
```
# Usage
```python
power_supply = litscpi.SCPI("192.168.11.254", 30000)
power_supply.enable_remote_control()
power_supply.start_battery()
print power_supply.read_current()
power_supply.stop_battery()
power_supply.enable_local_control()
```
