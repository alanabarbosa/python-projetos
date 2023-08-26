import random

class RockPaperScissors:
    def __init__(self, user_name):
        self.user_name = user_name
        self.options = [('R', 'Pedra'), ('P', 'Papel'), ('T', 'Tesoura')]
        self.user_score = 0
        self.computer_score = 0

    def get_user_input(self):
        while True:
            user_input = input('Escolha uma das opções: \n(R) Pedra \n(P) Papel \n(T) Tesoura \nEscolha: ').upper()
            if user_input in [option[0] for option in self.options]:
                return user_input
            else:
                print('Opção inválida. Tente novamente.')

    def get_computer_input(self):
        return random.choice(self.options)[0]

    def get_winner(self, user_input, computer_input):
        if user_input == computer_input:
            return 'Empate'
        elif (user_input == 'R' and computer_input == 'T') or (user_input == 'P' and computer_input == 'R') or (user_input == 'T' and computer_input == 'P'):
            self.user_score += 1
            return f'{self.user_name} venceu'
        else:
            self.computer_score += 1
            return 'Máquina venceu'

    def play_game(self):
        while True:
            user_input = self.get_user_input()
            computer_input = self.get_computer_input()
            winner = self.get_winner(user_input, computer_input)

            print(f'\n{winner}\n-----------------------------------------------------')
            print(f'\nPontuação: \n{self.user_name}: {self.user_score}, Máquina: {self.computer_score}\n-----------------------------------------------------\n')

            play_again = input('Deseja jogar novamente? (S/N): ').upper()
            if play_again != 'S':
                break

user_name = input('Digite seu nome: ')
game = RockPaperScissors(user_name)
game.play_game()