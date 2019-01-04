import socket
import time

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
        command = 'SENS:FUNC "CURRent"\n'
        self.__measurement_sock.send(command)
        command = 'SENS:SWE:POIN 50\n'
        self.__measurement_sock.send(command)
        command = 'SENS:SWE:FREQ 1000\n'
        self.__measurement_sock.send(command)

    def enable_local_control(self):
        command = "SYST:LOC\n"
        self.__measurement_sock.send(command)

    def start_battery(self):
        self.__measurement_sock.send("BATT:STAR\n")

    def stop_battery(self):
        self.__measurement_sock.send("BATT:STOP\n")

    def clear_battery_capacity(self):
        self.__measurement_sock.send("BATT:CAP:CLE\n")

    def read_current(self):
        # dirty way to clear pervious buffer
        try:
            _dummy_read = self.__measurement_sock.recv(20000)
        except socket.timeout:
            pass
        self.__measurement_sock.send("MEAS:CURR?\n")

        try:
            current_measurement = float(self.__measurement_sock.recv(100))
        except socket.timeout:
            time.sleep(1)
            current_measurement = float(self.__measurement_sock.recv(100))
        return current_measurement

    def read_current_array(self):
        self.__measurement_sock.send("MEAS:ARR:CURR?\n")
        time.sleep(0.5)
        try:
            current_measurements_str = self.__measurement_sock.recv(40000)
        except socket.timeout:
            current_measurement = []
        else:
            splitted_list = current_measurements_str.strip().split(",")
            current_measurement = reduce(tranlsate_str_measurement, splitted_list, [])
        finally:
            return current_measurement

