from __future__ import annotations

from dataclasses import dataclass

from pymonkey import token

TOKENMAPS = {
    "=": token.Token(token.ASSIGN, "="),
    ";": token.Token(token.SEMICOLON, ";"),
    "(": token.Token(token.LPAREN, "("),
    ")": token.Token(token.RPAREN, ")"),
    ",": token.Token(token.COMMA, ","),
    "+": token.Token(token.PLUS, "+"),
    "{": token.Token(token.LBRACE, "{"),
    "}": token.Token(token.RBRACE, "}"),
    "": token.Token(token.EOF, ""),
}


KEYWORDS = {"fn": token.FUNCTION, "let": token.LET}


def new(_input: str) -> Lexer:
    l = Lexer(_input)
    l.read_char()
    return l


def is_letter(ch: str) -> bool:
    return "a" <= ch <= "z" or "A" <= ch <= "Z" or ch == "_"


def is_digit(ch: str) -> bool:
    return "0" <= ch <= "9"


@dataclass
class Lexer:
    _input: str = ""
    _position: int = 0
    _read_position: int = 0
    _ch: str = ""

    def read_char(self):
        if self._read_position >= len(self._input):
            self._ch = ""
        else:
            self._ch = self._input[self._read_position]
        self._position = self._read_position
        self._read_position += 1

    def next_token(self) -> token.Token:
        self.skip_whitespace()
        ch = self._ch
        tok = TOKENMAPS.get(ch)
        if tok is None:
            if is_letter(ch):
                _literal = self.read_identifier()
                tok = token.Token(KEYWORDS.get(_literal, token.IDENT), _literal)
                return tok
            elif is_digit(ch):
                tok = token.Token(token.INT, self.read_number())
                return tok
            else:
                tok = token.Token(token.ILLEGAL, ch)
        self.read_char()
        return tok

    def skip_whitespace(self):
        while any(
            [self._ch == " ", self._ch == "\t", self._ch == "\n", self._ch == "\r"]
        ):
            self.read_char()

    def read_identifier(self) -> str:
        pos = self._position
        while is_letter(self._ch):
            self.read_char()
        return self._input[pos : self._position]

    def read_number(self) -> str:
        pos = self._position
        while is_digit(self._ch):
            self.read_char()
        return self._input[pos : self._position]
