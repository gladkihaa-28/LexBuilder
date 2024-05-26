# About LexBuilder:
LexBuilder is a library for automatically building a lexer in Python and C++. In the future, the library will be able to build lexers in major programming languages such as Golang, Java/Kotlin, etc.

## About Syntax:
In order for the library to generate a Lexer.py or Lexer.h file, you need to pass a list of tokens to the Builder class or use its .add_token() method. To declare a token, you need to import the Token() class from the Builder() class. You need to pass the token name and its value to the Token() class. After that, add all the tokens we created to a list and pass it as an argument to the PyBuilder() or CppBuilder class. By default, the lexer contains the tokens:
```python
INT_NUMBER = "INT_NUMBER"
FLOAT_NUMBER = "FLOAT_NUMBER"
PLUS = "PLUS"
MINUS = "MINUS"
STRING = "STRING"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"
VAR = "VAR"
ASSIGN = "ASSIGN"
EOF = "EOF"
```
### Example of creating a list of tokens:
```python
from LexBuilder.Builder import Token

PRINT = Token("PRINT", "print")
INPUT = Token("INPUT", "input")

tokens = [PRINT, INPUT]
```
#
## Python Example:
### Generate Lexer:
```python
from LexBuilder.Builder import PyBuilder, Token

PRINT = Token("PRINT", "print")
tokens = [PRINT]

lexer = PyBuilder(tokens)

lexer.add_token(Token("INPUT", "input"))
lexer.add_token(Token("LPAREN", "("))
lexer.add_token(Token("RPAREN", ")"))

lexer.build()
```

### Use Lexer:
```python
from Lexer import *


code = 'print("Hello, world!")'
lexer = Lexer(code)

token = lexer.get_next_token()
print(token)

while token.type != EOF:
    token = lexer.get_next_token()
    print(token)
```

```python
Token(PRINT, "print")
Token(LPAREN, "(")
Token(STRING, "Hello, world!")
Token(RPAREN, ")")
Token(EOF, None)
```
#
## C++ Example:
### Generate Lexer:
```python
from LexBuilder.Builder import CppBuilder, Token

PRINT = Token("PRINT", "print")
tokens = [PRINT]

lexer = CppBuilder(tokens)

lexer.add_token(Token("INPUT", "input"))
lexer.add_token(Token("LPAREN", "("))
lexer.add_token(Token("RPAREN", ")"))

lexer.build()
```

### Use Lexer:
```cpp
#include "Lexer.h"

using namespace std;


int main() {
    string code = "5 + 5";
    Lexer lexer(code);
    Token current_token = lexer.get_next_token();
    cout << current_token << endl;
    while (current_token.type != EOF_TOKEN) {
        current_token = lexer.get_next_token();
        cout << current_token << endl;
    }
}

```

```python
Token(INT_NUMBER, 5)
Token(PLUS, +)
Token(INT_NUMBER, 5)
Token(EOF, )
```