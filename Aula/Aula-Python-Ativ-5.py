numero1 = int(input('Digite o número: '))

def calcular(numero):
    def duplicar(numero):
        return numero * 2
    def triplicar(numero):
        return numero * 3
    def quadruplicar(numero):
        return numero * 4
   
    resultado_duplicar = duplicar(numero)
    resultado_triplicar = triplicar(numero)
    resultado_quadruplicar = quadruplicar(numero)

    return resultado_duplicar, resultado_triplicar, resultado_quadruplicar

print(calcular(numero1))