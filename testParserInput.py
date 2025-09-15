from scanner import Scanner
from parser import Parser

print("Ingresa el código de la máquina (termina con Ctrl+D):")
import sys
codigo = sys.stdin.read()

scanner = Scanner(codigo)
# Consumir todos los tokens para mostrar errores léxicos antes de parsear
while True:
    token = scanner.next_token()
    if token is None:
        break
# Reiniciar el scanner para el parser (opcional, si tu parser espera tokens desde el inicio)
scanner = Scanner(codigo)
parser = Parser(scanner)
parser.parse_maquina()  # O el método inicial de tu gramática
print("¡Análisis terminado!")

if not parser.error_found:
    print("¡Entrada aceptada!")
else:
    print("¡Entrada rechazada por error de sintaxis!")