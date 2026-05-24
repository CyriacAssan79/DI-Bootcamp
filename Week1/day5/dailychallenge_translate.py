import asyncio #In the last python version, it's recommended use asyncio to use googletrans
from googletrans import Translator #In googletrans, we import Translator

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
english_translate = {} #This dictionnary store french words like key and her english translate like value

async def translate():
  translator = Translator() #We call Translator class and we store in translator
  for french in french_words : #we go through the list and translate each words in english
    result = await translator.translate(french, dest='en')
    english_translate[french] =result.text
  print(english_translate)

asyncio.run(translate()) #execute translate function asynchronously