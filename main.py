import string
import random
import locale

# store all characters in lists
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

texts = [
    [
        "How many characters do you want in your password? ",
        "Quantos caracteres você deseja na sua senha? ",
    ],
    [
        "Password security level (1 - Basic, 2 - Strong) ? ",
        "Nível de segurança da senha (1 - Básica, 2  - Forte)? ",
    ],
    [
        "The password must be at least eight characters long.",
        "A senha deve ter pelo menos oito caracteres.",
    ],
    [
        "The password must be at least two or more characters long.",
        "A senha deve ter pelo menos dois ou mais caracteres.",
    ],
    ["Please, Enter numbers only.", "Por favor insira apenas números."],
    ["Please, Enter your number again: " "Por favor, digite seu número novamente: "],
    ["Strong Password: ", "Senha forte: "],
    ["Password: ", "Senha: "],
]

## set language by system language
language = 1 if locale.getlocale()[0] == "pt_BR" else 0
passwordSecurityLevel = int(input(texts[1][language]))

user_input = input(texts[0][language])
while True:
    try:
        characters_number = int(user_input)

        if passwordSecurityLevel == 1:
            if characters_number <= 1:
                print(texts[5][language] + "\n")
                user_input = input(texts[5][language])
            else:
                break
        else:
            if characters_number < 16:
                print(texts[3][language] + "\n")
                user_input = input(texts[5][language])
            else:
                break
    except:
        print(texts[4][language] + "\n")
        user_input = input(texts[0][language])

# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

result = []

if passwordSecurityLevel == 1:
    for x in range(characters_number):
        if x < len(s3) - 1:
            result.append(s3[x])
        else:
            y = random.randint(0, len(s3) - 1)
            result.append(s3[y])
else:
    # calculate 30% & 20% of number of characters
    part1 = round(characters_number * (30 / 100))
    part2 = round(characters_number * (20 / 100))

    for x in range(part1):
        result.append(s1[x])
        result.append(s2[x])

    for x in range(part2):
        result.append(s3[x])
        result.append(s4[x])

# shuffle result
random.shuffle(result)

# join result
password = "".join(result)
if passwordSecurityLevel == 1:
    print(texts[6][language], password)
else:
    print(texts[7][language], password)
