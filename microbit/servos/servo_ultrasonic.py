from microbit import *
from machine import time_pulse_us

# Servo control:
# 100 = 1 millisecond pulse all right
# 200 = 2 millisecond pulse all left
# 150 = 1.5 millisecond pulse center

# Set up the servo pin.
# You can choose pinX (where X is the
# number next to the pin on your board)
servo_pin = pin13  # change 13 to the pin you have the yellow/orange wire connected to
servo_pin.set_analog_period(20)
trig = pin0
echo = pin1
MIN_WIDTH = 0.5
MAX_WIDTH = 2.7
MIN_ANGLE = 0
MAX_ANGLE = 250


def setup_ultrasonic():

    trig.write_digital(0)
    echo.read_digital()


def move_to_angle(angle, min_angle=MIN_ANGLE, max_angle=MAX_ANGLE):
    angle = max(min_angle, angle)
    angle = min(max_angle, angle)
    width = (angle / max_angle) * (MAX_WIDTH - MIN_WIDTH) + MIN_WIDTH
    set_pulse(width)


def set_pulse(width):
    servo_pin.write_analog(1023 * width / 20)


def get_distance():
    trig.write_digital(1)
    trig.write_digital(0)

    micros = time_pulse_us(echo, 1)
    t_echo = micros / 1000000

    distance_cm = (t_echo / 2) * 34300
    return distance_cm


setup_ultrasonic()
min_distance, max_distance = 0, 50

while True:
    dist = get_distance()
    if min_distance < dist < max_distance:
        move_to_angle(180)
        print((dist, angle, min_distance, max_distance))
    else:
        move_to_angle(0)
    sleep(100)