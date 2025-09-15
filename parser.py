#importar scanner y tokens
from scanner import Scanner, Token

class Parser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.current_token = self.scanner.next_token()
        self.error_found = False

    # Metodo para verificar el tipo de token actual es decir si esperamos un ID deberiamos recibir un ID
    def match(self, expected_type):
        if self.current_token and self.current_token.type == expected_type:
            self.current_token = self.scanner.next_token()
        else:
            print(f"Error de sintaxis: se esperaba {expected_type} pero se encontró {self.current_token.type if self.current_token else 'EOF'} en la línea {self.current_token.line if self.current_token else 'EOF'}, columna {self.current_token.column if self.current_token else 'EOF'}")
            self.error_found = True
    #
    def check(self, expected_type):
        return self.current_token and self.current_token.type == expected_type
    
    # Definimos las gramaticas
    '''
    def parse_maquina(self):
        if self.current_token and self.current_token.type == 'MAQUINA':
            self.match('MAQUINA')
        if self.current_token and self.current_token.type == 'ID':
            self.match('ID')
        if self.current_token and self.current_token.type == 'LLAVEI':
            self.match('LLAVEI')
        if self.current_token and self.current_token.type in ['LAYOUT', 'PRODUCTOS', 'DINERO', 'REPORTES']:
            self.parse_contenido_maquina()
        if self.current_token and self.current_token.type == 'LLAVED':
         self.match('LLAVED')
    '''
    def parse_contenido_maquina(self):
        if self.current_token and self.current_token.type == 'LAYOUT':
            self.parse_layout()
            self.parse_contenido_maquina() 
        elif self.current_token and self.current_token.type == 'PRODUCTOS':
            self.parse_productos()
            self.parse_contenido_maquina()
        elif self.current_token and self.current_token.type == 'DINERO':
            self.parse_dinero()
            self.parse_contenido_maquina()
        elif self.current_token and self.current_token.type == 'REPORTES':
            self.match('REPORTES')
            self.parse_contenido_maquina()
    
    def parse_maquina(self):
        self.match('MAQUINA')
        self.match('ID')
        self.match('LLAVEI')
        self.parse_contenido_maquina()
        self.match('LLAVED')
    '''
    def parse_layout(self):
        if self.current_token and self.current_token.type == 'LAYOUT':
            self.match('LAYOUT')
        if self.current_token and self.current_token.type == 'LLAVEI':
            self.match('LLAVEI')
        if self.current_token and self.current_token.type == 'FILAS':
            self.match('FILAS')
        if self.current_token and self.current_token.type == 'COLON':
            self.match('COLON')
        if self.current_token and self.current_token.type == 'NUMERO':
            self.match('NUMERO')
        if self.current_token and self.current_token.type == 'SEMICOL':
            self.match('SEMICOL')
        if self.current_token and self.current_token.type == 'COLUMNAS':
            self.match('COLUMNAS')
        if self.current_token and self.current_token.type == 'COLON':
            self.match('COLON')
        if self.current_token and self.current_token.type == 'NUMERO':
            self.match('NUMERO')
        if self.current_token and self.current_token.type == 'SEMICOL':
            self.match('SEMICOL')
        if self.current_token and self.current_token.type == 'LLAVED':  
            self.match('LLAVED')
    '''
    def parse_layout(self):
        self.match('LAYOUT')
        self.match('LAYOUT')
        self.match('LLAVEI')
        self.match('FILAS')
        self.match('COLON')
        self.match('NUMERO')
        self.match('SEMICOL')
        self.match('COLUMNAS')
        self.match('COLON')
        self.match('NUMERO')
        self.match('SEMICOL')
        self.match('LLAVED')

    def parse_productos(self):
        if self.current_token and self.current_token.type == 'PRODUCTOS':
            self.match('PRODUCTOS')
        if self.current_token and self.current_token.type == 'LLAVEI':
            self.match('LLAVEI')
        if self.current_token and self.current_token.type == 'ID':
            self.parse_producto()
            self.parse_productos()  # llamada recursiva para el siguiente producto
        elif self.current_token and self.current_token.type == 'LLAVED':
            self.match('LLAVED')
        else:
            print(f"Error inesperado en PRODUCTOS: se esperaba ID o LLAVED pero se encontró {self.current_token.type if self.current_token else 'EOF'} en la línea {self.current_token.line if self.current_token else 'EOF'}, columna {self.current_token.column if self.current_token else 'EOF'}")
            self.error_found = True

    '''
    def parse_producto(self):
        if self.current_token and self.current_token.type == 'ID':
            self.match('ID')
        if self.current_token and self.current_token.type == 'COLON':
            self.match('COLON')
        if self.current_token and self.current_token.type == 'LLAVEI':
            self.match('LLAVEI')
        if self.current_token and self.current_token.type == 'DESCRIPCION':
            self.match('DESCRIPCION')
        if self.current_token and self.current_token.type == 'COLON':
            self.match('COLON')
        if self.current_token and self.current_token.type == 'DESCRIPCION':
            self.match('DESCRIPCION')
        if self.current_token and self.current_token.type == 'SEMICOL':
            self.match('SEMICOL')
        if self.current_token and self.current_token.type == 'PRECIO':
            self.match('PRECIO')
        if self.current_token and self.current_token.type == 'COLON':
            self.match('COLON')
        if self.current_token and self.current_token.type == 'DECIMAL':
            self.match('DECIMAL')
        if self.current_token and self.current_token.type == 'SEMICOL':
            self.match('SEMICOL')
        if self.current_token and self.current_token.type == 'STOCK':
            self.match('STOCK')
        if self.current_token and self.current_token.type == 'COLON':
            self.match('COLON')
        if self.current_token and self.current_token.type == 'NUMERO':
            self.match('NUMERO')
        if self.current_token and self.current_token.type == 'SEMICOL':
            self.match('SEMICOL')
        if self.current_token and self.current_token.type == 'STOCK_MIN':
            self.match('STOCK_MIN')
        if self.current_token and self.current_token.type == 'COLON':
            self.match('COLON')
        if self.current_token and self.current_token.type == 'NUMERO':
            self.match('NUMERO')
        if self.current_token and self.current_token.type == 'SEMICOL':
            self.match('SEMICOL')
        if self.current_token and self.current_token.type == 'STOCK_MAX':
            self.match('STOCK_MAX')
        if self.current_token and self.current_token.type == 'COLON':
            self.match('COLON')
        if self.current_token and self.current_token.type == 'NUMERO':
            self.match('NUMERO')
        if self.current_token and self.current_token.type == 'SEMICOL':
            self.match('SEMICOL')
        if self.current_token and self.current_token.type == 'LLAVED':
            self.match('LLAVED')
    '''
    def parse_producto(self):
        self.match('ID')
        self.match('COLON')
        self.match('LLAVEI')
        self.match('DESCRIPCION')
        self.match('COLON')
        self.match('DESCRIPCION')
        self.match('SEMICOL')
        self.match('PRECIO')
        self.match('COLON')
        self.match('DECIMAL')
        self.match('SEMICOL')
        self.match('STOCK')
        self.match('COLON')
        self.match('NUMERO')
        self.match('SEMICOL')
        self.match('STOCK_MIN')
        self.match('COLON')
        self.match('NUMERO')
        self.match('SEMICOL')
        self.match('STOCK_MAX')
        self.match('COLON')
        self.match('NUMERO')
        self.match('SEMICOL')
        self.match('LLAVED')

    def parse_dinero(self):
        self.match('DINERO')
        self.match('LLAVEI')
        if self.check('MONEDA'):
            self.match('MONEDA')
            self.parse_moneda()
            self.parse_dinero()  # acepta más monedas o billetes
        elif self.check('BILLETE'):
            self.match('BILLETE')
            self.parse_billete()
            self.parse_dinero()  # acepta más monedas o billetes
        self.match('LLAVED')

    def parse_moneda(self):
       #if self.check('NUMERO'):
            self.match('MONEDA')
            self.match('NUMERO')
            self.match('SEMICOL')

    def parse_billete(self):
        #if self.check('NUMERO'):
            self.match('BILLETE')
            self.match('NUMERO')
            self.match('SEMICOL')
