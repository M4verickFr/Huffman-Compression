class Frequency():
    def __init__(self, text):
        self.text = text
        self.freq = {}

        for character in text:
            if character in self.freq:
                self.freq[character] += 1
            else:
                self.freq[character] = 1

        self.freq = dict(sorted(self.freq.items(), key=lambda x: x[1]))

    def get_text(self):
        return self.text

    def get_freq(self):
        return self.freq