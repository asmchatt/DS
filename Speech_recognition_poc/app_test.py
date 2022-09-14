from flask import Flask, render_template, request, redirect
#import speech_recognition as sr
# Importing necessary modules required
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

app = Flask(__name__)

check_messages=[]


@app.route("/", methods=["GET", "POST"])
def index():
            transcript:str = ""
        
        # if request.method == "GET":
        #     speechText_str = request.form.get("speechText")
        #     #transcript=""+ speechText_str
        #     print(f"Printing  transcript inside get {speechText_str}")

        #if request.method == "POST":
            print("FORM DATA RECEIVED")
            # getting input with name = fname in HTML form
            # Creating Recogniser() class object
            recog1 = spr.Recognizer() 
            # Creating microphone instance
            mc = spr.Microphone() 
            # Capture Voice
            with mc as source:
                print("Speak 'hello' to initiate the Translation !")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                recog1.adjust_for_ambient_noise(source, duration=0.2)
                audio = recog1.listen(source)
                MyText = recog1.recognize_google(audio)
                MyText = MyText.lower()
            
            # Here initialising the recorder with
            # hello, whatever after that hello it
            # will recognise it.
            #if 'hello' in MyText:
                
            # Translator method for translation
                translator = Translator()
                
                # short form of english in which
                # you will speak
                #from_lang = 'en'
                from_lang = 'hi'
                
                # In which we want to convert, short
                # form of hindi
                #to_lang = 'hi'
                to_lang = 'en'
                
                with mc as source:
                    
                    print("Speak a stentence...")
                    recog1.adjust_for_ambient_noise(source, duration=0.2)
                    
                    # Storing the speech into audio variable
                    audio = recog1.listen(source)
                    
                    # Using recognize.google() method to
                    # convert audio into text
                    get_sentence = recog1.recognize_google(audio)
            
                    # Using try and except block to improve
                    # its efficiency.
                    try:
                        
                        # Printing Speech which need to
                        # be translated.
                        print("Phase to be Translated :"+ get_sentence)
            
                        # Using translate() method which requires
                        # three arguments, 1st the sentence which
                        # needs to be translated 2nd source language
                        # and 3rd to which we need to translate in
                        text_to_translate = translator.translate(get_sentence,
                                                                src= from_lang,
                                                                dest= to_lang)
                        
                        # Storing the translated text in text
                        # variable
                        text = text_to_translate.text
                        print("printing the non english text into english ",text )
            
                        # Using Google-Text-to-Speech ie, gTTS() method
                        # to speak the translated text into the
                        # destination language which is stored in to_lang.
                        # Also, we have given 3rd argument as False because
                        # by default it speaks very slowly
                        speak = gTTS(text=text, lang=to_lang, slow= False)
            
                        # Using save() method to save the translated
                        # speech in capture_voice.mp3
                        speak.save("captured_voice.mp3")    
                        
                        # Using OS module to run the translated voice.
                        os.system("start captured_voice.mp3")
            
                    # Here we are using except block for UnknownValue
                    # and Request Error and printing the same to
                    # provide better service to the user.
                    except spr.UnknownValueError:
                        print("Unable to Understand the Input")
                        
                    except spr.RequestError as e:
                        print("Unable to provide Required Output".format(e))
     
            return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    #print(f" aftre the page has been run , print the check_messages {check_messages}")