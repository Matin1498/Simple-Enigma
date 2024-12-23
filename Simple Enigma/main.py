from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector

message = input("Type your message: ").upper()
encryped = ""

KB = Keyboard()
PB = Plugboard([])
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK")
UKW_A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
UKW_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
UKW_C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")



for letter in message:
    signal = KB.forward(letter)
    signal = PB.forward(signal)
    signal = III.forward(signal)
    signal = II.forward(signal)
    signal = I.forward(signal)
    signal = UKW_A.forward(signal)
    signal = I.backward(signal)
    signal = II.backward(signal)
    signal = III.backward(signal)
    signal = PB.backward(signal)
    letter = KB.backward(signal)
    encryped += letter

print("encrypted message: " + encryped)
