import random

user = 0
computer = 0

user_name = input('Digite seu nome: ')

options = ['R', 'P', 'T']

while True:
    random_choice = random.randint(0, 2)

    user_input = input('Escolha uma das opções: \n(R) Pedra \n(P) Papel \n(T) Tesoura \nEscolha: ').upper()  

    verification = options[random_choice]
    
    if user_input == verification:
        print('\nDeu empate\n')
    elif user_input == 'R' and verification == 'T':
        print('\nvocê venceu\n')
        user += 1
    elif user_input == 'P' and verification == 'R':
        print('\nVocê perdeu\n')
        computer += 1
    elif user_input == 'T' and verification == 'P':
        print('\nvocê venceu\n')
        user += 1        

    print(f'\nPontuação: \n{user_name}: {user}, Máquina: {computer}\n')
