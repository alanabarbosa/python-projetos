import random

while True:
    rand_num = random.getrandbits(8)
    print(rand_num)
    number = input("Digite um número: ")
    if number.isdigit():       
        if int(number) == rand_num:
            print('Parabéns, você acertou!')
        else:
            print('Você errou!')
    else:
        print("Por favor, digite apenas números.")