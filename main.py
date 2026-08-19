from pynput import keyboard
import regex as re
import random
import sys
import os


class Tuping:
    def __init__(self, sentense_len: int, text_dir: str)):
        if sentense_len >= 50:
            raise ValueError("Invalid length, must be less than 50")

        self.dir - text_dir
        self.index = 0
        self.sentense_len = sentense_len
        self.text = self.generate_text(sentense_len)

        self.show_text()

    def generate_text(self, lenth: int):
        random_words = []

        with open(self.dir, mode="r", encoding="UTF-8") as file:
            text = file.read()
            text = re.sub(r"[^\pL\p{Space}]", "", text)
            list_text = text.lower().replace("\n", "").split(" ")

        list_text = [word for word in list_text if word]

        for _ in range(lenth):
            random_words.append(list_text[random.randint(0, len(list_text) - 1)])

        return " ".join(random_words)

    def show_text(self):
        os.system("clear")

        if self.index < len(self.text):
            before = self.text[:self.index]
            current = self.text[self.index] if self.index < len(self.text) else " "
            after = self.text[self.index + 1:] if self.index + 1 < len(self.text) else ""

            print(f"{before}[{current}]{after}")

        else:
            print(self.text)

    def pressed_key(self, key):
        try:
            if self.index >= len(self.text):
                if hasattr(key, "name") and key.name == "enter":
                    self.text = self.generate_text(self.sentense_len)
                    self.index = 0
                    self.show_text()
                return

            if hasattr(key, "char") and key.char is not None:
                if key.char == self.text[self.index]:
                    self.index += 1
                    self.show_text()

            elif hasattr(key, "name"):
                if key.name == "space" and self.text[self.index] == " ":
                    self.index += 1
                    self.show_text()

                elif key.name == "enter":
                    self.text = self.generate_text(self.sentense_len)
                    self.index = 0
                    self.show_text()

                elif key.name == "esc":
                    sys.exit(0)

        except IndexError:
            self.index = 0
            self.text = self.generate_text(self.sentense_len)
            self.show_text()


if __name__ == "__main__":
    directory = "/media/doge/F4A80B8AA80B4B16/penis_type/text.txt"
    tuping = Tuping(10, directory)

    with keyboard.Listener(on_press=tuping.pressed_key) as listener:
        listener.join()
