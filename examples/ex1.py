import litscpi

power_supply = litscpi.SCPI("192.168.11.254", 30000)
power_supply.enable_remote_control()
power_supply.start_battery()
print power_supply.read_current()
power_supply.stop_battery()
power_supply.enable_local_control()

