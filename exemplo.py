'''def soma(a, b):
    if type(a) == int and type(b) == int:
        c= a + b
        print(f'Resultado da soma: {c}')
    else:
        raise TypeError('Os tipos dos parâmetros devem ser inteiros')

a = 2
b = 3.5


try:
    soma(a, b)
except TypeError as msg:
    print(f"Erro: {msg}")'''

def soma(a, b):
    if type(a) == int and type(b) == int and a > 0 and b > 0:
        c= a + b
        print(f'Resultado da soma: {c}')
    else:
        raise TypeError('Os tipos dos parâmetros devem ser inteiros e positivos')

while True:
    try:
        a = int(input('Informe o primeiro número: '))
        b = int(input('Insira o segundo número: '))
        if a == 0 and b == 0:
            break
        try:
            soma(a, b)
        except TypeError as msg:
            print(f'ERRO: {msg}')
    except ValueError:
        print('ERRO: os valores devem ser inteiros')
