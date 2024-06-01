import RPi.GPIO as GPIO
from tkinter import Tk, Radiobutton, Button, StringVar, W

# GPIO pins setup
GPIO.setmode(GPIO.BCM)
LED_PINS = {
    "Red": 17,
    "Green": 27,
    "Blue": 22
}
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to control LEDs
def control_led(color):
    for led_color, pin in LED_PINS.items():
        GPIO.output(pin, GPIO.HIGH if led_color == color else GPIO.LOW)

# GUI setup buttons to control LED
root = Tk()
root.title("LED Controller")

selected_color = StringVar()
selected_color.set("Off")

Radiobutton(root, text="Red", variable=selected_color, value="Red", command=lambda: control_led("Red")).grid(row=0, column=0, sticky=W)
Radiobutton(root, text="Green", variable=selected_color, value="Green", command=lambda: control_led("Green")).grid(row=1, column=0, sticky=W)
Radiobutton(root, text="Blue", variable=selected_color, value="Blue", command=lambda: control_led("Blue")).grid(row=2, column=0, sticky=W)

def exit_program():
    GPIO.cleanup()
    root.destroy()

Button(root, text="Exit", command=exit_program).grid(row=3, column=0, sticky=W)

root.mainloop()
