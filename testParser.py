from scanner import Scanner
from parser import Parser

# Ejemplo de entrada válida de tu DSL
codigo = """
MAQUINA Maquina1 {
    LAYOUT {
        FILAS : 3 ;
        COLUMNAS : 5 ;
    }
    PRODUCTOS {
    P1 : {
        DESCRIPCION : CocaCola ;
        PRECIO : 12.50 ;
        STOCK : 10 ;
        STOCK_MIN : 2 ;
        STOCK_MAX : 20 ;
        }
    }
    DINERO {
        MONEDA 5 ;
        BILLETE 20 ;
    }
}
"""

scanner = Scanner(codigo)
parser = Parser(scanner)
parser.parse_maquina()  # O el método inicial de tu gramática