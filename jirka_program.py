##### 1. část #####

user_db = '''\
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
'''
line_number = 0 # Aktuální číslo řádku
line_to_skip = 0 # Řádky k přeskočení
delimiter_count = 0 # Počet oddělovačů
username_word = '' # String pro jméno uživatele
password_word = '' # String pro heslo uživatele
access_granded = False # Vstup povolen


username = input("Zadejte jméno: ")
password = input("Zadejte heslo: ")

for char in user_db:
    # Čítač řádků
    if (ord(char) == 10): # 10 = číslo znaku pro nový řádek
        line_number += 1
        # Reset počtu oddělovačů ( | ) a proměnné pro jméno a heslo
        delimiter_count = 0
        username_word = '' # String pro jméno uživatele
        password_word = '' # String pro heslo uživatele
        continue
    
    # Pokud se jendá o hlavičku, tak přeskočit
    #if (line_number == 1):
    #    continue
    
    # Pokud řádek začíná na +, tak označit jako řádek k přeskočení a následně přeskočit
    if (char == '+'):
        line_to_skip = line_number
    if (line_number == line_to_skip):
        # Pokud začal 3. řádek na +, tak opustit cyklus
        if (line_to_skip == 3):
            break
        continue
    
    if (char == '|'):
        delimiter_count += 1;
        if (delimiter_count == 3):
            # Jméno i heslo je ořezáno, jméno je case-insensitive
            if ((username.strip().lower() == username_word.strip().lower()) and (password.strip() == password_word.strip())):
                access_granded = True
                break
        continue
    
    if (delimiter_count == 1):
        username_word += char
        
    if (delimiter_count == 2):
        password_word += char
    
    #print(char, line_number, username_word, password_word)
    
if (not access_granded):
    print('Špatně zadané jméno či heslo')
    exit()
print('Vítejte, uživateli ' + username + '\n')

word_count = 0
word_capital_count = 0
word_upper_count = 0
word_lower_count = 0
number_count = 0
number_sum = 0
words_length = {}

##### 2. část #####
predefined_text = [
    'Předdefinovaný text 1',
    'Předdefinovaný text 2',
    'Předdefinovaný text 3'
]

while (True):
    try:
        selected_text = int(input("Zadejte číslo textu (1-3): "))
        selected_text -= 1
        if ((selected_text < 0) or (selected_text > 2)):
            print("Zadejte prosím číslo od 1 - 3.")
            continue
        break
    except ValueError:
        print("Zadejte prosím platné číslo.")
    
print('\nAnalýza textu:\n')
value = ''
value_has_upper = False
value_has_capital = False
value_has_lower = False
value_is_number = True

# Příprava stringu
input_text = predefined_text[selected_text]
input_text = input_text.strip() + ' ' # Na konec přidat mezeru pro vyhodnocení posledního slova/čísla

for char in input_text:
    # Zpracování
    if (char == ' '):
        value = value.strip()
        if (value == ''):
            continue
        
        # Ověření čísla
        if (value_is_number):            
            number_count += 1
            number_sum += int(value)
        # Jedná se o slovo
        else:
            word_count += 1
            # Uppercase:
            if (value_has_upper and not value_has_lower):
                word_upper_count += 1
            # Lowercase:
            elif (value_has_lower and not value_has_upper):
                word_lower_count += 1
            # Kapitálky:
            elif (value_has_capital):
                word_capital_count += 1
            # Pro graf četnosti délek slov (nikoli čísel):
            if (len(value) in words_length):
                words_length[len(value)] += 1
            else:
                words_length[len(value)] = 1
        
        # reset hodnot pro následné vyhodnocení
        value_has_upper = False
        value_has_capital = False
        value_has_lower = False
        value_is_number = True
        value = ''
        continue
        
    value += char
    
    # Ověření, že jde o číslo
    if (value_is_number):  
        try:
            int(char)
        except ValueError:
            value_is_number = False
    # Pokud se nejedná o číslo, tak rozeznat velké/malé písmena + kapitálku
    if (not value_is_number):
        # Nastavovat pouze pokud ještě stav uppercasu nebyl nastaven a jedná se o upercase
        if ((not value_has_upper) and (char == char.upper())):
            value_has_upper = True
            # O kapitálku se jedná pouze pokud je velké písmeno na první pozici
            if (len(value) == 1):
                value_has_capital = True
        # To samé, jako u uppercasu, ale naopak
        elif ((not value_has_lower) and (char == char.lower())):
            value_has_lower = True
    
# Vykreslení napočtených hodnot
print('Počet slov: ' + str(word_count))
print('Počet kapitálek: ' + str(word_capital_count))
print('Počet slov lowercase: ' + str(word_upper_count))
print('Počet slov uppercase: ' + str(word_lower_count))
print('Počet čísel: ' + str(number_count))
print('Suma čísel: ' + str(number_sum))
    
##### 3. část #####
print('\nGraf:')
# Seřazení podle hodnoty ve slovníku (dictionary)
words_length = dict(sorted(words_length.items()))

# Zjištění maximální délky pro hvězdy (*)
max_length = 0;
for length_key in words_length:
    if (max_length < int(words_length[length_key])):
        max_length = int(words_length[length_key])

# Vykreslení grafu
for length_key in words_length:
    single = words_length[length_key]
    print(
        str(length_key).ljust(5) + '| ' +
        ("*" * single).ljust(max_length + 1) + '| ' +
        str(single)
    )





