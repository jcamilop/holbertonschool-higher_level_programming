#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    numeros_romanos = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    resultado = 0
    valor_previo = 0
    for i in roman_string:
        valor = numeros_romanos.get(i, 0)
        resultado += valor
        if valor > valor_previo:
            resultado -= 2 * valor_previo
        valor_previo = valor
    return resultado
