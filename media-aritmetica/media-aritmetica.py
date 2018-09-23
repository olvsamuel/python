''' Faça um algoritmo que receba três notas,
calcule e mostre a média aritmética entre elas.  '''


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 < 0 or nota2 < 0 or nota3 < 0 :
    print("As notas devem ser maiores ou iguais a zero")
else :
    media = (nota1 + nota2 + nota3) / 3
    print("A média aritmética é: ", media)
