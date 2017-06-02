# The tokens and their tags are specified here

token_expressions = [
    # reserved keywords
    (r'include', 'INCLUDE'),
    (r'int', 'INT'),
    (r'main', 'MAIN'),
    (r'char', 'CHAR'),
    (r'printf', 'PRINTF'),
    (r'getchar', 'GETCHAR'),
    (r'return', 'RETURN'),
    # other tokens
    # (r'[A-Za-z0-9_]+\.[A-Za-z]+', 'FILENAME'),
    (r'[A-Za-z_]+[A-Za-z0-9_]*', 'ID'),
    (r'[0-9]+', 'NUM'),
    (r'\#', 'OP_HASH'),
    (r'\<', 'OP_LESS'),
    (r'\=', 'OP_ASSIGN'),
    (r'\+', 'OP_PLUS'),
    (r'\,', 'OP_COMMA'),
    (r'\;', 'OP_SEMICOLON'),
    (r'\>', 'OP_LARGER'),
    (r'\(', 'OP_BR_OPEN'),
    (r'\)', 'OP_BR_CLOSE'),
    (r'\{', 'OP_PAR_OPEN'),
    (r'\}', 'OP_PAR_CLOSE'),
    (r'["][^\"]*["]', 'STRING'),
]