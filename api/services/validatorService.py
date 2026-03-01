import re
from datetime import datetime

def esNumeroValido(valor, campo:str):
    if (valor<=0 or valor>99999999.99):
        return f"El campo {campo} debe ser un numero mayor que 0 y menor o igual a 99999999.99"
    return None

def estaVacio(valor:str, campo:str):
    valorLimpio = valor.strip()
    if (valorLimpio == ""):
        return f"El campo {campo} esta vacio"
    return None

def esNumeroTelefonico(valor: str):
    try:
        if (len(valor) != 10):
            return "La longitud del número de teléfono debe de ser de 10 digitos"
        int(valor)
        return None
    except Exception as e:
        return "Numero de teléfono invalido"

def formatoPlaca(valor: str):
    if re.fullmatch(r"^[A-Z]{3}-[0-9]{3}$", valor):
        return None
    return "El formato de la placa debe ser 3 letras mayusculas, guion medio, 3 números. Ejemplo XXX-123"

def anioValido(anio: int):
    anioMaximo = datetime.now().year + 1
    if anio < 1900 or anio > anioMaximo:
        return f"El año debe estar entre 1900 y {anioMaximo}"
    return None