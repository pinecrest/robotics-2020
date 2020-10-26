from microbit import * 
# Servo control: 
# 100 = 1 millisecond pulse all right 
# 200 = 2 millisecond pulse all left 
# 150 = 1.5 millisecond pulse center 

# Set up the servo pin. 
# You can choose pinX (where X is the 
# number next to the pin on your board)
servo_pin = pin13 # change 13 to the pin you have the yellow/orange wire connected to
servo_pin.set_analog_period(20)
MIN_WIDTH = 0.5
MAX_WIDTH = 2.7

def move_to_angle(angle, min_angle=0, max_angle=250):
    angle = max(min_angle, angle)
    angle = min(max_angle, angle)
    width = (angle / max_angle) * (MAX_WIDTH - MIN_WIDTH) + MIN_WIDTH
    print(width)
    set_pulse(width)

def set_pulse(width): 
    servo_pin.write_analog(1023 * width / 20)

while True: 
    if button_a.is_pressed():
        move_to_angle(180, 180)
    elif button_b.is_pressed():
        move_to_angle(0)
    else:
        move_to_angle(90)
    sleep(100)