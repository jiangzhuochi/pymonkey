from dataclasses import dataclass
from typing import NewType

TokenType = NewType("TokenType", str)


@dataclass
class Token:
    _Type: TokenType
    _Literal: str


ILLEGAL = TokenType("ILLEGAL")
EOF = TokenType("EOF")

# Identifiers + literals
IDENT = TokenType("IDENT")  # add, foobar, x, y, ...
INT = TokenType("INT")  # 1343456

# Operators
ASSIGN = TokenType("=")
PLUS = TokenType("+")

# Delimiters
COMMA = TokenType(",")
SEMICOLON = TokenType(";")
LPAREN = TokenType("(")
RPAREN = TokenType(")")
LBRACE = TokenType("{")
RBRACE = TokenType("}")

# Keywords
FUNCTION = TokenType("FUNCTION")
LET = TokenType("LET")
