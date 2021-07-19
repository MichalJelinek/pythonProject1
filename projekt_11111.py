TEXTS = ['''
Situated  .   about 10 miles west of Kemmerer, 
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
and steepen abruptly. Overlying them and extending bob
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


user_data = dict(bob='123', ann='pass123', mike='password123', liz='pass123')
separator = "-" * 40

# user verification
username = input("username: ")
if username not in user_data.keys():
    print(f"Username {username} does not exist. Exiting program.")
else:
    password = input("password: ")
    print(separator)
    if password != user_data[username]:
        print(f"Invalid password. Exiting program.")
    else:
        # say hello
        n_texts = len(TEXTS)
        print(f"Welcome to the app, {username}\n We have {n_texts} texts to be analyzed.")
        print(separator)

        # text selection
        while True:
            try:
                text_number = int(input(f"Enter a number btw. 1 and {n_texts} to select: "))
                break
            except ValueError:
                print("Input is not numeric.")

        if text_number - 1 not in range(n_texts):
            print("Invalid text number. Exiting program.")
        else:
            print(separator)

            # text evaluation
            text = TEXTS[text_number - 1].split(" ")
            cleaned_text = [word.strip(".,:?!\n\r ") for word in text]
            cleaned_text = [item for item in cleaned_text if item != '']

            n_len = {}
            n_words = len(cleaned_text)
            n_titlecase = n_uppercase = n_lowercase = n_numbers = sum_numbers = n_rest = 0
            for word in cleaned_text:
                if word.isalpha():
                    n_titlecase += 1 if word.istitle() or word.isupper() else 0
                    n_uppercase += 1 if word.isupper() else 0
                    n_lowercase += 1 if word.islower() else 0
                elif word.isnumeric():
                    n_numbers += 1
                    sum_numbers += int(word)
                else:
                    n_rest += 1
                word_length = len(word)
                n_len[word_length] = n_len.setdefault(word_length, 0) + 1

            print(f"There are {n_words} words in the selected text.")
            print(f"There are {n_titlecase} titlecase words.")
            print(f"There are {n_uppercase} uppercase words.")
            print(f"There are {n_lowercase} lowercase words.")
            print(f"There are {n_numbers} numeric strings.")
            print(f"The sum of all the numbers {sum_numbers}")

            # word length graph plotting
            print(separator)
            print("LEN|  OCCURENCES  |NR.")
            print(separator)

            max_length = max(n_len.keys())
            for length in range(max_length):
                length += 1  # fix indexing from zero
                s_length = (len(str(max_length)) - len(str(length)) + 1) * " " + str(length)  # indent fix
                n_len.setdefault(length, 0)  # non existing dict keys fix
                print(f"{s_length}|{n_len[length] * '*' + (14 - n_len[length]) * ' '}|{n_len[length]}")



