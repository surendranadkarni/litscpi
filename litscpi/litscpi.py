import socket

def tranlsate_str_measurement(acc, str_mesurement):
    stripped = str_mesurement.strip()
    if stripped is not "":
        acc.append(float(stripped))
    return acc

class SCPI:
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__measurement_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__measurement_sock.settimeout(0.5)


    def connect(self):
        self.__measurement_sock.connect((self.__ip, self.__port))

    def disconnect(self):
        self.__measurement_sock.close()

    def enable_remote_control(self):
        command = "SYST:REM\n"
        self.__measurement_sock.send(command)

    def enable_local_control(self):
        command = "SYST:LOC\n"
        self.__measurement_sock.send(command)

    def start_battery(self):
        self.__measurement_sock.send("BATT:STAR\n")

    def stop_battery(self):
        self.__measurement_sock.send("BATT:STOP\n")

    def read_current(self):
        self.__measurement_sock.send("MEAS:CURR?\n")
        return float(self.__measurement_sock.recv(100))

    def read_current_array(self):
        self.__measurement_sock.send("MEAS:ARR:CURR?\n")
        current_measurements_str = self.__measurement_sock.recv(20000)
        splitted_list = current_measurements_str.strip().split(",")
        current_measurement = reduce(tranlsate_str_measurement, splitted_list, [])
        return current_measurement

