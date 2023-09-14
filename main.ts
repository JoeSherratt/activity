input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    binary = "" + binary + "1"
    basic.showString(binary)
    decimal = decimal * 2 + 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showNumber(decimal)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    binary = "" + binary + "0"
    basic.showString(binary)
    decimal = decimal * 2
})
let binary = ""
let decimal = 0
decimal = 0
binary = ""
