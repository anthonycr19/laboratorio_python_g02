"""Programación funcional en Python"""


def multiplica(a, b, c=100):
    #resultado = a * b * c
    #return resultado
    return a * b * c

print("El resultado de mi función es: {}".format(
    multiplica(40, 50)))

# Es correcto usasr la función cambiando el valor del tercer parámetro
print("El resultado de mi función es: {}".format(
    multiplica(40, 2, 500)))


