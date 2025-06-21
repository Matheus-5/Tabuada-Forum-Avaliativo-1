print('TABUADA')
while True:
    #definindo qual a operação desejada:
    print()
    op=int(input('Qual operação deseja? 1=MULTIPLICAÇÃO, 2=DIVISÃO, 3=ADIÇÃO, 4=SUBTRAÇÃO: '))

    #Código para operação de multiplicação:
    if op==1:
        num=int(input('De qual número você deseja ver a tabuada? '))
        tab=int(input('Quantas multiplicações deseja? '))
        n=1
        print()
        print('TABUADA DE MULTIPLICAÇÃO DO NÚMERO',num,':')
        print()
        for x in range(tab):
            print(num,'x',n,'=',num*n)
            n+=1

    #Código para operação de divisão:
    elif op==2:
        num=int(input('De qual número você deseja ver a tabuada? '))
        tab=int(input('Quantos divisões deseja? '))
        n=1
        print()
        print('TABUADA DE DIVISÃO DO NÚMERO',num,':')
        print()
        for x in range(tab):
            print(num,'÷',n,'=',num/n)
            n+=1

    #Código para operação de adição:
    elif op==3:
        num=int(input('De qual número você deseja ver a tabuada? '))
        tab=int(input('Quantos adições deseja? '))
        n=1
        print()
        print('TABUADA DE ADIÇÃO DO NÚMERO',num,':')
        print()
        for x in range(tab):
            print(num,'+',n,'=',num+n)
            n+=1

    #Código para operação de subtração:
    elif op==4:
        num=int(input('De qual número você deseja ver a tabuada? '))
        tab=int(input('Quantos subtrações deseja? '))
        n=1
        print()
        print('TABUADA DE SUBTRAÇÃO DO NÚMERO',num,':')
        print()
        for x in range(tab):
            print(num,'-',n,'=',num-n)
            n+=1
    else: break
