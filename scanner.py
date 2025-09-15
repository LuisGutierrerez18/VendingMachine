# Este es el archivo del scanner
# Es responsable de escanear el código fuente y generar tokens

# importaciones necesarias
import re
from position import Position


# Definicion de tokens
# Fueron definidos en el archivo de documentacion 
TOKENS = [
    ("COD",        r"[A-Z][oO][0-9]"),
    ("DECIMAL",    r"\d+\.\d+"),
    ("NUMERO",     r"\d+"),
    ("MAQUINA",    r"\bMAQUINA\b"),
    ("PRODUCTO",   r"\bproducto\b"),
    ("ID",         r"[A-Za-z][A-Za-z0-9_]*"),
    ("DESCRIPCION",r"[A-Za-z]+"),
    ("PRECIO",     r"\bprecio\b"),
    ("STOCK",      r"\bstock\b"),
    ("STOCK_MIN",  r"\bstock_min\b"),
    ("STOCK_MAX",  r"\bstock_max\b"),
    ("RESTOCK",    r"\brestock\b"),
    ("DINERO",     r"\bdinero\b"),
    ("MONEDA",     r"\bmoneda\b"),
    ("BILLETE",    r"\bbillete\b"),
    ("VENTA",      r"\bventa\b"),
    ("PAGO",       r"\bpago\b"),
    ("REPORTE",    r"\breporte\b"),
    ("FILAS",      r"\bfilas\b"),
    ("COLUMNAS",   r"\bcolumnas\b"),
    ("COLON",      r":"),
    ("LLAVEI",     r"\{"),
    ("LLAVED",     r"\}"),
    ("SEMICOL",    r";"),
    ("COMMA",      r","),
    ("COMMENT",    r"//.*|/\*[\s\S]*?\*/"),
    ("WS",         r"\s+"),
]

class Position:
    def __init__(self, line=1, column=1):
        self.line = line
        self.column = column

# Asociar expresiones regulares con tipos de tokens
# Con esto el programa puede identificar cada token
TOKEN_REGEX = {name: re.compile(pattern) for name, pattern in TOKENS}

# Defimimos la clase token para manejar los tokens
class Token():
    # constructor de la clase
    def __init__(self, type_, value, line, column):
        self.type = type_ # type es el tipo de token de la lista de arriba lo que estan entre comillas
        self.value = value #  value es el valor del token que se encontro o lo que coinicida con la regex
        self.line = line # line es la linea en la que se encontro el token
        self.column = column # column es la columna en la que se encontro el token
    
    # devuelve una representacion del token para mejor entendimiento y visualizacion
    def __repr__(self):
        return f"Token({self.type}, {self.value}, {self.line}, {self.column})"

# Definir la clase Scanner
class Scanner:
    #inicializamos 
    def __init__(self, code):
        self.code = code
        self.position = Position(1, 1)  # Iniciar en la línea 1, columna 1
        self.tokens = []
        self.errors = []
        self.current_index = 0

    #Metodo para avanzar en el codigo y actualizar la posicion
    def advance(self):
        if self.current_index < len(self.code):
            char = self.code[self.current_index]
            self.current_index += 1
            if char == '\n':
                self.position.line += 1
                self.position.column = 1
            else:
                self.position.column += 1
            return char
        return None
    
    # Metodo para pasar al siguiente token
    def next_token(self):
        # Si ya llegamos al final del codigo, retornamos None
        if self.current_index >= len(self.code):
            return None
        
        #guardamos la posicion actual
        start_position = Position(self.position.line, self.position.column)

        #Ignoramos espacios en blanco y comentarios
        while self.current_index < len(self.code):
            # Paso 1:verficamos si el caracter actual es espacio en blanco
            ws_match = TOKEN_REGEX["WS"].match(self.code, self.current_index)
            if ws_match:
                for char in ws_match.group(0):
                    if char == '\n':
                        self.position.line += 1
                        self.position.column = 1
                    else:
                        self.position.column += 1
                self.current_index = ws_match.end()
                continue

            # Paso 2:verificamos si el caracter actual es un comentario
            comment_match = TOKEN_REGEX["COMMENT"].match(self.code, self.current_index)
            if comment_match:
                for char in comment_match.group(0):
                    if char == '\n':
                        self.position.line += 1
                        self.position.column = 1
                    else:
                        self.position.column += 1
                self.current_index = comment_match.end()
                continue
            break  
        # Paso 3: Intentamos hacer match con cada token definido
        for token_name, token_regex in TOKEN_REGEX.items(): # Recorremos cada token y su regex
            match = token_regex.match(self.code, self.current_index) # Intentamos hacer match en la posicion actual
            if match:
                lexeme = match.group(0) # Obtenemos el lexema que hizo match
                # Creamos el token con su tipo, lexema y posicion
                token = Token(token_name, lexeme, start_position.line, start_position.column) # Lo creamos para guardar toda la info del token encontrado  
                self.current_index = match.end() # Actualizamos el indice actual al final del match
                for char in lexeme:
                    if char == '\n':
                        self.position.line += 1
                        self.position.column = 1
                    else:
                        self.position.column += 1
                return token

        # Si no se encontró ningún token, retornamos None
        # Si no se encontró ningún token, reportamos error léxico
        if self.current_index < len(self.code):
            caracter = self.code[self.current_index]
            print(f"Error léxico: carácter no reconocido '{caracter}' en la línea {self.position.line}, columna {self.position.column}")
            self.current_index += 1
            self.position.column += 1
        return None
