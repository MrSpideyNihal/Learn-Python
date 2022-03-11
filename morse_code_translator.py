"""Morse code translator."""
import string

def morse_dict():
    """Return a dictionary mapping characters to Morse code."""
    return {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-",
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/',
    }


def text_to_morse(text):
    """Return the Morse code translation of the input text."""
    return ''.join([morse_dict()[char.upper()] for char in text if char in string.ascii_letters + string.digits + ' '])


def morse_to_text(morse):
    """Return the original text from the given Morse code."""
    return ''.join(['' if ch == '/' else ''.join([list(morse_dict().values())[i] for i, c in enumerate(morse) if c == list(morse_dict().keys())[i][0]]) for ch in morse])

if __name__ == "__main__":
    while True:
        print("Enter 't' to translate text to Morse code, 'm' to translate Morse code to text, or 'q' to quit.")
        op = input()
        if op.lower() == 'q': break
        elif op.lower() == 't':
            text = input("Enter the text: ")
            print(f"Morse code translation: {text_to_morse(text)}")
        elif op.lower() == 'm':
            morse = input("Enter the Morse code: ")
            print(f"Text translation: {morse_to_text(morse)}")
