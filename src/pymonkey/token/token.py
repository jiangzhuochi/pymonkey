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
MINUS = TokenType("-")
BANG = TokenType("!")
ASTERISK = TokenType("*")
SLASH = TokenType("/")

LT = TokenType("<")
GT = TokenType(">")

EQ = TokenType("==")
NOT_EQ = TokenType("!=")

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
TRUE     = TokenType("TRUE")
FALSE    = TokenType("FALSE")
IF       = TokenType("IF")
ELSE     = TokenType("ELSE")
RETURN   = TokenType("RETURN")
