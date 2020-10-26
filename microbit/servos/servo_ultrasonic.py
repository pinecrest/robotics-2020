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

# Select the trigger pin0 and the echo pin1
trig = pin0
echo = pin1

#This is the min and max length of the servo control pulse in ms
MIN_WIDTH = 0.5
MAX_WIDTH = 2.7

# This is the min and max angle of the servo
MIN_ANGLE = 0
MAX_ANGLE = 250


def setup_ultrasonic():
    #This sets up the trigger and echo pins.
    trig.write_digital(0)
    echo.read_digital()


def move_to_angle(angle, min_angle=MIN_ANGLE, max_angle=MAX_ANGLE):
    # Move the servo to an angle between min and max.
    angle = max(min_angle, angle)
    angle = min(max_angle, angle)
    width = (angle / max_angle) * (MAX_WIDTH - MIN_WIDTH) + MIN_WIDTH
    set_pulse(width)


def set_pulse(width):
    # send the control pulse to the servo
    servo_pin.write_analog(1023 * width / 20)


def get_distance():
    # send a very fast on and off signal pulse to the Ultrasonic sensor.
    # This pulse tells the sensor to send out a sound wave.
    trig.write_digital(1)
    trig.write_digital(0)

    # Measure the time of the signal coming back from the sensor. 
    micros = time_pulse_us(echo, 1)

    # divide the number of microseconds by a million to get seconds
    t_echo = micros / 1000000

    # divide the time by 2 to get the one way time, then 
    # multiply by 34300 (speed of sound * 100)
    # to get the distance.
    distance_cm = (t_echo / 2) * 34300
    return distance_cm


setup_ultrasonic()
min_distance, max_distance = 0, 50

while True:
    #get the distance
    dist = get_distance()

    # if the distance is between the limits we set, then move the servo
    if min_distance < dist < max_distance:
        move_to_angle(180)
        print((dist, 180, min_distance, max_distance))
    else: # otherwise go back to original position
        move_to_angle(0)

    # wait for a tenth of a second before measuring again.
    sleep(100)