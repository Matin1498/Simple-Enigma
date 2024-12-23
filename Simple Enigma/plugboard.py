class Plugboard:
    def __init__(self, pairs):
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            if self.right.find(pair[0]) > self.right.find(pair[1]):
                temp = pair[0]
                pair = pair[1] + temp

            a = self.right.find(pair[0])
            b = self.right.find(pair[1])

            self.left = self.left[:a] + pair[1] + self.left[a + 1:b] + pair[0] + self.left[b + 1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
