
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


a = 20
mezera = ' '
pomlcka = '-'
delka_pomlcky = 80
pocet_slov_velky = 0
pocet_slov_zacetek_velky = 0
pocet_slov_maly = 0
pocet_slov_cislice = 0
soucet = 0
uzivatele = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
pocet_pismen = {}
serazeny = {}


username = input("Uzivatelské jméno: ")
password = input("Heslo: ")
print(pomlcka * delka_pomlcky)

if uzivatele.get(username) == (password):
    print('Welcome to the app, ' + (username) + ' We have 3 texts to be analyzed.')

    print(pomlcka * delka_pomlcky)

    number = int(input('Enter a number btw. 1 and 3 to select: '))

    if int(number) < 4 and int(number) > 0:
        print(pomlcka * delka_pomlcky)
        rozdeleni_stringu = TEXTS[number - 1].split()
        pocet_slov = len(rozdeleni_stringu)
        pocet_slov_4 = 0

        for n in range(pocet_slov):
            slovo = rozdeleni_stringu[n].strip('.,!:?')
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

        print('There are ', (pocet_slov), ' words in the selected text.')
        print('There are ', (pocet_slov_zacetek_velky), ' titlecase words.')
        print('There are ', (pocet_slov_velky), ' uppercase words.')
        print('There are ', (pocet_slov_maly), ' lowercase words.')
        print('There are ', (pocet_slov_cislice), ' numeric strings.')
        print('The sum of all the numbers ', (soucet))
        print(pomlcka * delka_pomlcky)
        print('LEN|      OCCURENCES       |NR.')
        print(pomlcka * delka_pomlcky)

        for klic, val in sorted(pocet_pismen.items()):
            if klic < 10:
                print('', klic, '|', '*' * val, mezera * (a - val), '|', +val)
            else:
                print(klic, '|', '*' * val, mezera * (a - val), '|', +val)
    else:
        print('Enter a number btw. 1 and 3, exit')

else:
    print('Heslo, nebo uživatelské jméno je špatně!')