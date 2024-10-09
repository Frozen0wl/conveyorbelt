import RPi.GPIO as GPIO
import socket

class ServoController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.servo1_pin = 12  # Replace with the actual GPIO pin connected to servo 1
        self.servo2_pin = 13  # Replace with the actual GPIO pin connected to servo 2
        GPIO.setup(self.servo1_pin, GPIO.OUT)
        GPIO.setup(self.servo2_pin, GPIO.OUT)
        self.servo1 = GPIO.PWM(self.servo1_pin, 50)
        self.servo2 = GPIO.PWM(self.servo2_pin, 50)
        self.servo1.start(0)
        self.servo2.start(0)

    def extract_servo1(self):
        self.servo1.ChangeDutyCycle(7.5)  # Adjust duty cycle for extraction
        # Add any necessary delay to allow servo movement
        # For example: time.sleep(1)
        
    def retract_servo1(self):
        self.servo1.ChangeDutyCycle(2.5)  # Adjust duty cycle for retraction
        # Add any necessary delay to allow servo movement
        # For example: time.sleep(1)

    def extract_servo2(self):
        self.servo2.ChangeDutyCycle(7.5)  # Adjust duty cycle for extraction
        # Add any necessary delay to allow servo movement
        # For example: time.sleep(1)

    def retract_servo2(self):
        self.servo2.ChangeDutyCycle(2.5)  # Adjust duty cycle for retraction
        # Add any necessary delay to allow servo movement
        # For example: time.sleep(1)

def main():
    udp_ip = "0.0.0.0"  # Listen on all available interfaces
    udp_port = 5555  # Choose an arbitrary port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((udp_ip, udp_port))

    servo_controller = ServoController()

    while True:
        data, addr = server_socket.recvfrom(1024)
        decoded_data = data.decode("utf-8")

        if decoded_data == "servo1.extract":
            servo_controller.extract_servo1()
        elif decoded_data == "servo1.retract":
            servo_controller.retract_servo1()
        elif decoded_data == "servo2.extract":
            servo_controller.extract_servo2()
        elif decoded_data == "servo2.retract":
            servo_controller.retract_servo2()

if __name__ == "__main__":
    main()
