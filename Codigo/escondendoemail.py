import copy


def easy_do():
    while True:
        email = str(input('Digite seu e-mail >: ')).strip().lower()
        analisando_string = email.count('@')
        if analisando_string > 1:
            print(f'\033[33mVocê digitou {analisando_string} @. Tente Novamente\033[m ')
            continue

        elif '@' in email:
            if len(email) < 14:
                print('\033[31mE-mail muito curto, tente novamente! seu e-mail deve ter pelo menos 14 letras.\033[m')
            else:
                verificando = copy.copy(email).split('@')[1]  # aqui estou copiando o email orginal e removendo tudo antes do @ para verificar se é gmail ou hotmail
                copia1_email = copy.copy(email).split(
                    '@')  # aqui estou seprando antes e o pós @ em listas, basta da um print para entender
                tam_email = copia1_email[0]  # aqui estou pegando o email antes do @ sem o gmail.com/hotmail.com
                dominio = copia1_email[1]
                len_email = len(tam_email)  # aqui estou verificando o tamanho do email antes do @
                subtraindo_um = len_email - 1  # estou removendo 1 do tamanho do len para mostra o tamanho correto do email, com a 1 letra
                primeira_letra = copia1_email[0][0]
                if verificando == 'gmail.com' or verificando == 'hotmail.com':
                    censurado = '*' * subtraindo_um  # aqui estou multiplicando o tamanho de * pelo tamanho do subitraindo 1 para por como * censurado

                    print(f'{primeira_letra}{censurado}@{dominio}')
                while True:
                    continuar = str(input('''\033[33mDeseja Continuar?\033[m
                    Digite:
                    \033[32m[1] SIM\033[m
                    \033[36m[2] NÃO\033[m
                    '''))
                    if continuar == '1':
                        break
                    elif continuar == '2':
                        print('Obrigado.')
                        return False
                    else:
                        print('Opção Invalida. Tente Novamente!')
                        continue
        else:
            print('\033[31mTente Novamente!\033[m')
            continue


easy_do()