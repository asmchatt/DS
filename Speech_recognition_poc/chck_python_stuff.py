
import googletrans as Translator
import googletrans as Trans


#print(Translator.LANGUAGES)
language_dict:dict = Translator.LANGUAGES

print(type(Translator.LANGUAGES))

print(language_dict.keys())

##if language_dict.values() =="hindi":
for k, v in language_dict.items():
    #print(f"printing  key {k} , value , {v}")
    if v =="marathi":
        print("Eureka ")
        break 

string_txt :str = "yeh ghatiya service hain"
translator = Trans()
to_lang = 'en'
from_lang='hi'
text_to_translate = translator.translate(string_txt,
                                                     src= from_lang,
                                                     dest= to_lang)
print(f" printing here, the translated etxt  : {text_to_translate.text}")                                                     
                