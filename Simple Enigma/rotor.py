class Rotor:
    def __init__(self, wiring):
        self.right = wiring
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
