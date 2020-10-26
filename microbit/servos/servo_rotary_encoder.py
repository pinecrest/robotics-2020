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
    min_width, max_width = 0.5, 2.5
    width = (angle / max_angle) * (max_width - min_width) + min_width
    set_pulse(width)

def set_pulse(width):
    servo_pin.write_analog(1023 * width / 20)
                                                                                                                                       
position = 0
MAX_POSITION = 180
MIN_POSITION = 0
last_a = 0
last_b = 0
last_s = 0
b = pin12.read_digital()
last_pos = position
move_to_angle(position)

while True: 
    a = pin16.read_digital()
    s = pin8.read_digital()
    if a != last_a and a:
        print(a, last_a)
        b = pin12.read_digital()
        print(b)
        if b != a:
            print("incrementing by 5")
            position = min(position + 5, MAX_POSITION)
        else:
            print("decrementing by 5")
            position = max(position - 5, MIN_POSITION)
    elif s != last_s:
        print("resetting position to 0")
        position = 0
    if position != last_pos:
        print(position)
        move_to_angle(position)
    last_a, last_s, last_pos = a, s, position



