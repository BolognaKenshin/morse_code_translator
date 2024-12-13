int_morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
                                  "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
                                  "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "1": ".----",
                                  "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"}

reverse_int_morse = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i",
    ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r",
    "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", ".----": "1",
    "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0"
}

def text_to_morse():
    text = input("Please input your text for international morse code translation (letters and numbers only): ")
    text_to_translate = text.lower().split()
    translated_code = ""
    for word in text_to_translate:
        for char in word:
            morse_char = int_morse[char] + " "
            translated_code += morse_char
        translated_code += "/ "
    print(f"Text entered: {text}")
    print(f'Morse Code: {translated_code}')

def morse_to_text():
    morse = input("Please input your morse code for translation: ")
    translated_text = ""
    for char in morse:
        if char == "/":
            translated_text += " "
        else:
            translated_text += reverse_int_morse[char]
    print(f"Morse entered: {morse}")
    print(f"Translated to text: {translated_text}")

