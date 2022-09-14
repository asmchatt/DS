
import googletrans as Translator



string_txt :str = "yeh ghatiya service hain"
translator = Translator()
to_lang = 'en'
from_lang='mr'
text_to_translate = translator.translate(string_txt,
                                                     src= from_lang,
                                                     dest= to_lang)
print(f" printing here : {text_to_translate.text}")                                                     
                