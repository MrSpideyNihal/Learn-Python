"""Simple lexer for basic syntax."""
import re
class Lexer:
    """Lexer for basic syntax."""
    def __init__(self, input_string):
        self.tokens = []
        self.input = input_string.lower()

    def tokenize(self):
        """Tokenize the input string into keywords and identifiers."""
        while len(self.input) > 0:
            if re.match(r'\bif\b', self.input): # 'if'
                token = re.match(r'\bif\b', self.input).group()
                self.tokens.append(token)
                self.input = self.input[len(token):]
            elif re.match(r'\bwhile\b', self.input): # 'while'
                token = re.match(r'\bwhile\b', self.input).group()
                self.tokens.append(token)
                self.input = self.input[len(token):]
            else:
                match = re.search(r'[a-zA-Z_][a-zA-Z_0-9]*', self.input)
                if match:
                    token = match.group()
                    self.tokens.append(token)
                    self.input = self.input[len(token):]

    def get_tokens(self):
        """Return the list of tokens."""
        return self.tokens

if __name__ == "__main__":
    lexer = Lexer("if 1 then print(2 + 3) while True: print('hello')\n")
    lexer.tokenize()
    print(lexer.get_tokens())
