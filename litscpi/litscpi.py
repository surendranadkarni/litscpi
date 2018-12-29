import socket

class SCPI:
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__measurement_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__measurement_sock.settimeout(0.5)
        self.__measurement_sock.connect((ip, port))

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

