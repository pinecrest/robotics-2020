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

def move_to_angle(angle, min_angle=0, max_angle=180):
    min_width, max_width = 0.5, 2.6
    width = (angle / max_angle) * (max_width - min_width) + min_width
    print(width)
    set_pulse(width)

def set_pulse(width):
    servo_pin.write_analog(1023 * width / 20)

position = 0
MAX_POSITION = 180
MIN_POSITION = 0

while True: 
    if button_a.is_pressed():
        position = min(position + 5, MAX_POSITION)
    elif button_b.is_pressed():
        position = max(position - 5, MIN_POSITION)
    move_to_angle(position)
    sleep(20)