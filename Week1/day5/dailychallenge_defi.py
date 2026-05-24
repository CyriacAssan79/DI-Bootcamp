#Défi 1
mot = input('Listez vos mots, vous pouvez les séparer par des virgules : ')

mot_list = mot.split(',') #The words is divided according to the décimal point
mot_list = sorted(mot_list) #The list have been range with sorted function 
print(mot_list)

#Defi

def long(phrase): #This function finds the longest word in a sentence
    phrase = phrase.split(' ') #The words is divided according to the décimal point
    long_string= max(phrase, key=len) #max return the longest words accordind to len
    print(f'La plus chaine est {long_string}')


phrase = "Margaret's toy is a pretty doll."
long(phrase)