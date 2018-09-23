import math

while True :

    ''' pegando valores de a, b e c '''
    a = int(input("Digite a: "))
    b = int(input("Digite b: "))
    c = int(input("Digite c: "))

    ''' calculando a raiz de delta '''
    x =(b*2)-(4ac)

    ''' testando se a raiz é negativa, se não for, faz o cálculo '''
    if x < 0 :
        print ("\nRaiz negativa,\nDigite novamente:\n ")
    else :

        x = math.sqrt(x)
        x1 =(-b+x)/(2a)
        x2 =(-b-x)/(2*a)

        print  (x1, x2)
        exit()