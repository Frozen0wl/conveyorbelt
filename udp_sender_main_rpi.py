import socket

class ServoController:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.udp_port = 5555  # Same port as used in the slave Raspberry Pi

    def send_command(self, command):
        message = command.encode("utf-8")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(message, (self.ip_address, self.udp_port))
        client_socket.close()

    def extract_servo1(self):
        self.send_command("servo1.extract")

    def retract_servo1(self):
        self.send_command("servo1.retract")

    def extract_servo2(self):
        self.send_command("servo2.extract")

    def retract_servo2(self):
        self.send_command("servo2.retract")

# Function to handle user input for servo control
def servo_control(servo_controller):
    while True:
        user_input = input("Enter command (e.g., '1e' for servo 1 extract, '1r' for servo 1 retract): ")
        if user_input == '1e':
            servo_controller.extract_servo1()
        elif user_input == '1r':
            servo_controller.retract_servo1()
        elif user_input == '2e':
            servo_controller.extract_servo2()
        elif user_input == '2r':
            servo_controller.retract_servo2()
        elif user_input.lower() == 'exit':
            break
        else:
            print("Invalid command. Please enter a valid command.")

# Usage example
if __name__ == "__main__":
    ip_address_rpi_slave = "192.168.14.54"
    servo_controller = ServoController(ip_address_rpi_slave)
    servo_control(servo_controller)
