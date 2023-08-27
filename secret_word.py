secret_lyrics = 'javascript'
correct_lyrics = ''

loser = 0

while True:
    word_letter = input("Digite uma letra: ")

    if len(word_letter) > 1:
        print('Digite apenas uma letra.')
        continue

    if word_letter in secret_lyrics:
        correct_lyrics += word_letter
    else:        
        loser += 1
        if loser == 15:
            print('\nVocê perdeu todas as tentativas\n')
            play_again = input('Deseja jogar novamente? (S/N): ').upper()
            if play_again != 'S':
                break

    for secret_lyric in secret_lyrics:
        if secret_lyric in correct_lyrics:
            print(secret_lyric)
        else:
            print('*')