import sys

# Define Braille to English and English to Braille mappings
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".....O": "CAP", ".....O": "NUM",
    # Add Braille symbols for numbers and capital indicator
    ".O.OOO": "0", ".O..OO": "1", ".OO.OO": "2", ".O.O.O": "3", ".OO.OO": "4",
    ".O.OOO": "5", ".OOOOO": "6", ".OOO.O": "7", ".O.O.O": "8", ".O..OO": "9"
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

def translate_to_braille(text):
    result = []
    for char in text:
        # Handle numbers
        if char.isdigit():
            result.append(braille_to_english["NUM"])
            result.append(english_to_braille[char])
        # Handle uppercase letters
        elif char.isupper():
            result.append(braille_to_english["CAP"])
            result.append(english_to_braille[char.lower()])
        # Handle lowercase letters and spaces
        else:
            result.append(english_to_braille.get(char, ""))
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    is_number = False
    is_capital = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_to_english["NUM"]:
            is_number = True
        elif symbol == braille_to_english["CAP"]:
            is_capital = True
        else:
            char = braille_to_english.get(symbol, "")
            if is_number:
                char = str(char)
                is_number = False
            elif is_capital:
                char = char.upper()
                is_capital = False
            result.append(char)
        i += 6
    return ''.join(result)

def main():
    # Get the input from command line
    input_text = sys.argv[1]
    
    # Determine if input is English or Braille
    if set(input_text).issubset({'O', '.'}):
        # Input is Braille
        print(translate_to_english(input_text))
    else:
        # Input is English
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
