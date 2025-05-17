import keyboard
import regex as re
import random


def generate_text(lenth: int):
    random_words = []

    with open("./data.txt", mode="r", encoding="UTF-8") as file:
        text = file.read()
        text = re.sub(r'[^\pL\p{Space}]', '', text)
        list_text = text.lower().replace("\n", "").split(" ")

    for _ in range(lenth):
        random_words.append(list_text[random.randint(0, len(list_text) - 1)])

    return " ".join(random_words)


index = 0
text = generate_text(10)
print(text)


def pressed_key(key: keyboard.KeyboardEvent):
    global index
    global text

    try:
        if key.name == text[index] or (key.name == "space" and text[index] == " "):
            print(text[index:], end="\r")

            index += 1

    except IndexError:
        index -= 1

    if key.name == "esc":
        text = generate_text(10)
        index = 0

        print(text)


if __name__ == "__main__":
    keyboard.on_press(pressed_key)
    keyboard.wait()
