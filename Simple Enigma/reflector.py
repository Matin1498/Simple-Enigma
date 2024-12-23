class Reflector:
    def __init__(self, reflector):
        self.right = reflector
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
