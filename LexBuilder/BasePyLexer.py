from string import Template

types = """INT_NUMBER = "INT_NUMBER"
FLOAT_NUMBER = "FLOAT_NUMBER"
PLUS = "PLUS"
MINUS = "MINUS"
STRING = "STRING"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"
VAR = "VAR"
ASSIGN = "ASSIGN"
EOF = "EOF"
{0}
"""

lexer = Template("""class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return self.__str__()


class Lexer:
     def __init__(self, text):
         self.text = text
         self.pos = 0
         self.current_char = self.text[self.pos]

     def advance(self):
         self.pos += 1
         if self.pos < len(self.text):
             self.current_char = self.text[self.pos]
         else:
             self.current_char = None

     def change_pos(self, pos):
         self.pos = pos
         if self.pos < len(self.text):
             self.current_char = self.text[self.pos]
         else:
             self.current_char = None

     def skip_whitespace(self):
         while self.current_char is not None and self.current_char.isspace():
             self.advance()

     def get_next_token(self):
         while self.current_char is not None:
             if self.current_char.isspace():
                 self.skip_whitespace()
                 continue

             if self.current_char.isdigit() or self.current_char == "-":
                 token_value = ""
                 while self.current_char is not None and (self.current_char.isdigit() or self.current_char == "." or self.current_char == "-"):
                     token_value += self.current_char
                     self.advance()
                 try:
                     return Token(INT_NUMBER, int(token_value))
                 except:
                     try:
                         return Token(FLOAT_NUMBER, float(token_value))
                     except:
                         return Token(MINUS, "-")

             if self.current_char == '"':
                 self.advance()
                 string_value = ""
                 while self.current_char is not None and self.current_char != '"':
                     string_value += self.current_char
                     self.advance()
                 if self.current_char == '"':
                     self.advance()
                     return Token(STRING, '"' + string_value + '"')
                 else:
                     print(f"Некорректный символ: {self.current_char}")
                     sys.exit()

             if self.current_char == '+':
                 self.advance()
                 return Token(PLUS, '+')

             if self.current_char == '-':
                 self.advance()
                 return Token(MINUS, '-')
                 
             if self.current_char == '*':
                 self.advance()
                 return Token(MULTIPLY, '*')

             if self.current_char == '/':
                 self.advance()
                 return Token(DIVIDE, '/')
                 
             if self.current_char == '=':
                 self.advance()
                 return Token(ASSIGN, '=')

${first}

             if self.current_char.isalpha():
                 token_value = ""
                 while self.current_char is not None and (self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == "_"):
                     token_value += self.current_char
                     self.advance()

${second}
                 else:
                     return Token(VAR, token_value)

             print(f"Неверный синтаксис: {self.text}")
             sys.exit()

         return Token(EOF, None)""")