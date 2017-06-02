"""
    Simple lexer for analysing a piece of C code:
"""
import os
import re
import sys

from token_expressions import token_expressions

lexemes_array = []

def lex(characters, token_exprs):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    if tag == 'ID':
                        if text in lexemes_array:
                            lex_id = lexemes_array.index(text)
                        else:
                            lexemes_array.append(text)
                            lex_id = lexemes_array.index(text)
                        token = str(tag) + ', ' + str(lex_id)
                    elif tag == 'NUM':
                        token = str(tag) + ', ' + str(text)
                    else:                   
                        token = (tag)
                tokens.append(token)

                break
        if not match:
            sys.stderr.write('Syntax error at: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens

if __name__ == "__main__":
    fname = os.path.abspath("lexical.c")
    file = open(fname)
    xters = file.read()
    xters = re.sub(r'[\s]', '', xters)
    file.close()
    tokens = lex(xters, token_expressions)
    s = ''
    for token in tokens:
        token = '<' + token + '>'
        s += token
    print s