''' Faça um algoritmo que receba dois números
maiores que zero, calcule e mostre um elevado ao outro. '''


valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

''' testando se os valores sao maiores que zero '''
if valor1 < 0 or valor2 < 0 :
    print("Os números devem ser maiores que zero!")
else :
    resultado = valor1 ** valor2
    print(resultado)
