from .BasePyLexer import types as pytypes, lexer as pylexer
from .BaseCppLexer import types as cpptypes, lexer as cpplexer


class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PyBuilder:
    def __init__(self, tokens=None):
        self.tokens = tokens if tokens else []

    def add_token(self, token):
        self.tokens.append(token)

    def generate_code_for_tokens(self):
        result1 = ""
        result2 = ""
        result3 = ""

        for token in self.tokens:
            name = token.name
            value = token.value
            result1 += f'{name} = "{name}"\n'
            if len(set(value)) == 1:
                result1 += f'{"_".join([name, name])} = "{"_".join([name, name])}"\n'
                result2 += f"             if self.current_char == '{list(set(value))[0]}':\n"
                result2 += '                 self.advance()\n'
                result2 += f"                 if self.current_char == '{list(set(value))[0]}':\n"
                result2 += f'                     self.advance()\n'
                result2 += f'                     return Token({"_".join([name, name])}, "{value*2}")\n'
                result2 += f'                 else:\n'
                result2 += f"                     return Token({name}, '{value}')\n\n"
            else:
                result3 += f'                     if token_value == "{value}":\n'
                result3 += f'                         return Token({name}, "{value}")\n\n'

        return result1, result2, result3


    def build(self):
        code1, code2, code3 = self.generate_code_for_tokens()
        with open("Lexer.py", "w", encoding="utf-8") as file:
            file.write("import sys\n\n\n")
            file.write(pytypes.format(code1) + "\n")
            file.write(pylexer.substitute(first=code2, second=code3) + "\n\n")


class CppBuilder:
    def __init__(self, tokens=None):
        self.tokens = tokens if tokens else []

    def add_token(self, token):
        self.tokens.append(token)

    def generate_code_for_tokens(self):
        result1 = "\n"
        result2 = ""
        result3 = ""

        for token in self.tokens:
            name = token.name
            value = token.value
            result1 += f'string {name} = "{name}";\n'
            if len(set(value)) == 1:
                result1 += f'string {"_".join([name, name])} = "{"_".join([name, name])}";\n'
                result2 += f"             if (current_char == '{list(set(value))[0]}') " + "{\n"
                result2 += f'                 advance();\n'
                result2 += f"                 if (current_char == '{list(set(value))[0]}') " + "{\n"
                result2 += f'                     advance();\n'
                result2 += f'                     return Token({"_".join([name, name])}, "{value}");\n'
                result2 += f'                 ' + "} " + 'else ' + '{\n'
                result2 += f'                     return Token({name}, "{value}");' + "\n                 }\n             }"
            else:
                result3 += f'                     if (token_value == "{value}") ' + '{\n'
                result3 += f'                         return Token({name}, "{value}");' + '\n                     }\n'

        return result1, result2, result3

    def build(self):
        code1, code2, code3 = self.generate_code_for_tokens()
        with open("Lexer.h", "w", encoding="utf-8") as file:
            file.write("#include <iostream>\n#include <string>\n\nusing namespace std;\n\n\n")
            file.write(cpptypes.format(code1) + "\n")
            file.write(cpplexer.substitute(first=code2, second=code3) + "\n\n")