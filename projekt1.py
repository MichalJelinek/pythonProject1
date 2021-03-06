TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
         red, purple, yellow and gray beds of the Wasatch 
         Formation. Eroded portions of these horizontal 
         beds slope gradually upward from the valley floor 
         and steepen abruptly. Overlying them and extending 
         to the top of the butte are the much steeper 
         buff-to-white beds of the Green River Formation, 
         which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
         a portion of the largest deposit of freshwater fish 
         fossils in the world. The richest fossil fish deposits 
         are found in multiple limestone layers, which lie some 
         100 feet below the top of the butte. The fossils 
         represent several varieties of perch, as well as 
         other freshwater genera and herring similar to those 
         in modern oceans. Other fish such as paddlefish, 
         garpike and stingray are also present.''']

# nacteni promenych
a = 20
mezera = ' '
pomlcka = '-' * 80
pocet_slov_velky = pocet_slov_zacetek_velky = pocet_slov_maly = pocet_slov_cislice = soucet = 0

uzivatele = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
pocet_pismen = {}
serazeny = {}

# zapis do promenych username a password
username = input("Uzivatelské jméno: ")
password = input("Heslo: ")
print(pomlcka)

if uzivatele.get(username) == password:
    print('Welcome to the app, ' + username + ' We have 3 texts to be analyzed.')

    print(pomlcka)

    number = input('Enter a number btw. 1 and 3 to select: ')

    if number.isnumeric():
        if 4 > int(number) > 0:
            print(pomlcka)

            rozdeleni_stringu = TEXTS[int(number) - 1].split()
            ocisteno = [slovo.strip(".,:?!\n\r ") for slovo in rozdeleni_stringu]
            ocisteno = [slovo for slovo in ocisteno if slovo]

            pocet_slov = len(ocisteno)

            for slovo in ocisteno:
                if slovo.istitle():
                    pocet_slov_zacetek_velky += 1
                elif slovo.isupper():
                    pocet_slov_velky += 1
                elif slovo.islower():
                    pocet_slov_maly += 1
                elif slovo.isnumeric():
                    pocet_slov_cislice += 1
                    soucet += int(slovo)
                pocet_pismen[len(slovo)] = pocet_pismen.get(len(slovo), 0) + 1

            print('There are ', pocet_slov, ' words in the selected text.')
            print('There are ', pocet_slov_zacetek_velky, ' titlecase words.')
            print('There are ', pocet_slov_velky, ' uppercase words.')
            print('There are ', pocet_slov_maly, ' lowercase words.')
            print('There are ', pocet_slov_cislice, ' numeric strings.')
            print('The sum of all the numbers ', soucet)
            print(pomlcka)
            print('LEN|      OCCURENCES       |NR.')
            print(pomlcka)

            for klic, val in sorted(pocet_pismen.items()):
                if klic < 10:
                    print('', klic, '|', '*' * val, mezera * (a - val), '|', +val)
                else:
                    print(klic, '|', '*' * val, mezera * (a - val), '|', +val)
        else:
            print('Enter a number btw. 1 and 3, exit')
    else:
        print('Enter a number btw. 1 and 3, exit')
else:
    print('Heslo, nebo uživatelské jméno je špatně!')
