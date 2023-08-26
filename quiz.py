start = input('Quer começar? (S/N) ')

if start == 'S':
    print('\n Começando... \n')

    def quiz():
        questions = {
            "Questão 01: \nO que é Python? \nPython é uma linguagem de programação de alto nível, interpretada e orientada a objetos. Ela é conhecida por sua sintaxe clara e concisa, bem como por sua grande biblioteca padrão." : True,
            "Questão 02: \nComo verificar se o que o usuário digitou no input é uma string em Python? \nPara verificar se o que o usuário digitou no input é uma string em Python, você pode usar a função isinstance() ou a função type(). A função isinstance() verifica se um objeto é uma instância de uma classe ou de uma subclasse. A função type() retorna o tipo do objeto. Para mais informações, consulte a minha resposta anterior." : False,
            "Questão 03: \nO que é PEP 8? \nPEP 8 é um guia de estilo para código Python. Ele define as diretrizes para escrever código Python legível e consistente. O guia abrange tópicos como convenções de nomenclatura, indentação, comentários e espaçamento em branco.": False,
            "Questão 04: \nO que é pip? \nPip é um gerenciador de pacotes para Python. Ele permite instalar, atualizar e remover pacotes Python facilmente. Pip é usado para instalar pacotes de terceiros que não estão incluídos na biblioteca padrão do Python.": True,
            "Questão 05: \nO que são módulos em Python? \nMódulos em Python são arquivos contendo definições e instruções Python. Eles podem ser importados em outros arquivos Python para reutilização de código. A biblioteca padrão do Python contém muitos módulos úteis para tarefas comuns de programação." : True
        }
        correct_answers = 0

        for question, condition in questions.items():
            print(question, '\n')

            user_input = input( f'Verdadeiro ou Falso? (V/F): ')

            if user_input.upper() == 'V':
                if condition:
                    print('Parabéns, você acertou! \n')
                    correct_answers += 1
                else:
                    print('Você errou \n')
            elif user_input.upper() == 'F':
                if condition:
                    print('Você errou \n')
                else:
                    print('Parabéns, você acertou! \n')
                    correct_answers += 1

            print(f'Você acertou {correct_answers} perguntas')
      
    quiz()
else:
    print('Você precisa iniciar o quiz para acessar as perguntas!')











