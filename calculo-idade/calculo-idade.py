''' Faça um algoritmo que receba o ano de nascimento de uma pessoa
e o ano atual. Calcule e mostre:
    a) A idade dessa pessoa.
    b) Quantos anos essa pessoa terá em 2018. '''


anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

''' testando se os anos sao menores que zero '''
if anoNascimento < 0 or anoAtual < 0 :
    print("Os anos devem ser maiores que zero!")
else :
    ''' testando se o ano de nascimento é maior que o ano atual '''
    if anoNascimento > anoAtual :
        print("Essa pessoa ainda não nasceu!")
    else :
        ''' testando se o ano de nascimento é maior que 2018 '''
        if anoNascimento > 2018 :
            idade = anoAtual - anoNascimento
            print("A idade da pessoa é: ", idade, " anos.")
        else :
            idade = anoAtual - anoNascimento
            print("A idade da pessoa é: ", idade, " anos.")
            idade2018 = 2018 - anoNascimento
            print("A idade da pessoa em 2018 é: ", idade2018, " anos.")
