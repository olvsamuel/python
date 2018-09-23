''' Faça um algoritmo que receba o salário de um funcionário,
calcule e mostre o novo salário, sabendo-se que este sofreu
um aumento de 25%.   '''


salario =  float(input("Digite o salário do funcionário: "))


''' testando se o salário inserido é menor que zero '''
if salario < 0 :
    print('O salário não pode ser negativo!')
else:
    salario = salario * 1.25
    print ('O salário com acréscimo de 25% é de: ' , salario)
