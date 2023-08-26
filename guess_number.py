import random

win = 0

while True:
    rand_num = random.getrandbits(2)
    number = input("Digite um número: ")

    if number.isdigit():       
        if int(number) == rand_num:
            print('\nParabéns, você acertou! \n')
            win += 1
            print(f'\nPontuação: {win}\n')

            question = input('Quer jogar novamente? (S/N) ')

            if question.upper() == 'S':
                continue    
            else:
                exit()                

        else:
            print('\nVocê errou! \n')
            question = input('Quer jogar novamente? (S/N) ')

            if question.upper() == 'S':
                continue
            else:
                exit()   
    else:
        print("\nPor favor, digite apenas números.\n")
