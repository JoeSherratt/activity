def on_button_pressed_a():
    global binary, decimal
    binary = "" + binary + "1"
    basic.show_string(binary)
    decimal = decimal * 2 + 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(decimal)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global binary, decimal
    binary = "" + binary + "0"
    basic.show_string(binary)
    decimal = decimal * 2
input.on_button_pressed(Button.B, on_button_pressed_b)

binary = ""
decimal = 0
decimal = 0
binary = ""