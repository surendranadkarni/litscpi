import litscpi

power_supply = litscpi.SCPI("192.168.0.254", 30000)
power_supply.connect()
power_supply.enable_remote_control()
power_supply.start_battery()
print power_supply.read_current()
print power_supply.read_current_array()

power_supply.stop_battery()
power_supply.enable_local_control()
power_supply.disconnect()

