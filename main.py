import keyboard
import regex as re
import random
import os


class Tuping:
    def __init__(self, sentense_len: int):
        if sentense_len >= 50:
            raise ValueError("Invalid length, must be less than 50")

        self.index = 0
        self.text = self.generate_text(sentense_len)
        self.sentense_len = sentense_len

        print(self.text)

    def generate_text(self, lenth: int):
        random_words = []

        with open("./text.txt", mode="r", encoding="UTF-8") as file:
            text = file.read()
            text = re.sub(r'[^\pL\p{Space}]', '', text)
            list_text = text.lower().replace("\n", "").split(" ")

        for _ in range(lenth):
            random_words.append(list_text[random.randint(0, len(list_text) - 1)])

        return " ".join(random_words)

    def pressed_key(self, key: keyboard.KeyboardEvent):

        try:
            if key.name == self.text[self.index] or \
               (key.name == "space" and self.text[self.index] == " "):
                print(self.text[self.index:] + " " * 50, end="\r")

                self.index += 1

        except IndexError:
            self.index = 0

        if key.name == "enter":
            self.text = self.generate_text(self.sentense_len)
            self.index = 0

            print(self.text)

        elif key.name == "esc":
            os._exit(0)


if __name__ == "__main__":
    tuping = Tuping(10)

    keyboard.on_press(tuping.pressed_key)
    keyboard.wait()
