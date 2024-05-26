from string import Template


types = """string INT_NUMBER = "INT_NUMBER";
string FLOAT_NUMBER = "FLOAT_NUMBER";
string PLUS = "PLUS";
string MINUS = "MINUS";
string STRING = "STRING";
string MULTIPLY = "MULTIPLY";
string DIVIDE = "DIVIDE";
string VAR = "VAR";
string ASSIGN = "ASSIGN";
string EOF_TOKEN = "EOF";
{0}
"""


lexer = Template("""struct Token {
    string type;
    std::string value;

    Token(string t, string v) : type(t), value(v) {}

    friend ostream& operator<<(ostream& out, Token& token) {
        out << "Token(" + token.type + ", " + token.value + ")";
        return out;
    }
};


class Lexer {
private:
    std::string text;
    size_t pos;
    char current_char;

public:
    Lexer(const string& t) : text(t), pos(0), current_char(text[pos]) {}

    void advance() {
        pos++;
        if (pos < text.length()) {
            current_char = text[pos];
        } else {
            current_char = '\0';
        }
    }

    void change_pos(size_t p) {
        pos = p;
        if (pos < text.length()) {
            current_char = text[pos];
        } else {
            current_char = '\0';
        }
    }

    void skip_whitespace() {
        while (current_char == ' ' && std::isspace(current_char) && pos < text.length()) {
            advance();
        }
    }

    Token get_next_token() {
        while (pos < text.length()) {
            if (current_char == ' ') {
                skip_whitespace();
                continue;
            }

            if (std::isdigit(current_char) || current_char == '-') {
                std::string token_value;
                while (current_char != '\0' && (std::isdigit(current_char) || current_char == '.' || current_char == '-')) {
                    token_value += current_char;
                    advance();
                }
                try {
                    return Token(INT_NUMBER, token_value);
                } catch (const std::invalid_argument&) {
                    try {
                        return Token(FLOAT_NUMBER, token_value);
                    } catch (const std::invalid_argument&) {
                        return Token(MINUS, "-");
                    }
                }
            }

            if (current_char == '"') {
                advance();
                std::string string_value;
                while (current_char != '\0' && current_char != '"') {
                    string_value += current_char;
                    advance();
                }
                if (current_char == '"') {
                    advance();
                    return Token(STRING, "\"" + string_value + "\"");
                } else {
                    throw std::runtime_error("Некорректный символ: " + std::string(1, current_char));
                }
            }

            if (current_char == '+') {
                advance();
                return Token(PLUS, "+");
            }

            if (current_char == '-') {
                advance();
                return Token(MINUS, "-");
            }
            
            if (current_char == '*') {
                advance();
                return Token(MULTIPLY, "*");
            }
            
            if (current_char == '/') {
                advance();
                return Token(DIVIDE, "/");
            }
            
            if (current_char == '=') {
                advance();
                return Token(ASSIGN, "=");
            }
            
${first}

            if (std::isalpha(current_char)) {
                std::string token_value;
                while (current_char != '\0' && (std::isalnum(current_char) || current_char == '_')) {
                    token_value += current_char;
                    advance();
                }

${second}

                return Token(VAR, token_value);
            }

            throw std::runtime_error("Неверный синтаксис: " + text);
        }
        return Token(EOF_TOKEN, "");
    }
};""")