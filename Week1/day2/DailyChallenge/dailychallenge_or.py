#Exerice 1
birthdays = {
    "Assan" : "2002/01/24",
    "Cyriac" : "2005/04/24",
    "Junior" : "2003/01/2",
    "Koffi" : "2010/02/1",
    "Yann" : "2005/01/24",
}

print("You can look up the birthdays of the people in the list!")

nom = input("Entrer votre nom : ")

for key, value in birthdays.items():
    if key == nom :
        print(f'Votre date d\'anniversaire est le {value}')

# Exerice 2
birthdays = {
    "Assan" : "2002/01/24",
    "Cyriac" : "2005/04/24",
    "Junior" : "2003/01/2",
    "Koffi" : "2010/02/1",
    "Yann" : "2005/01/24",
}

print("Voici tous les noms présent : ")
for key, value in birthdays.items():
    print(key)

name = input("Entrer votre nom : ")

is_name = ""

for key, value in birthdays.items():
    if key == name :
        print(f'Votre date d\'anniversaire est le {value}')
        is_name = key

if(len(is_name)==0) :
    print("Désolé, nous n'avons pas trouvé votre nom")

# Exerice 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Entrer votre nom : ")

for all_name in range(0,len(names)) :
    if names[all_name] == user_name :
        print(f"Votre nom est {names[all_name]} et votre index est {all_name}")
        break