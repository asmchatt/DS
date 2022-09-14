from flask import Flask, render_template, request, redirect
import speech_recognition as sr
# Importing necessary modules required
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os
import check_sentiment

app = Flask(__name__)

check_messages=[]


@app.route("/", methods=["GET", "POST"])
def index():
        transcript:str = ""
        # speechText_str:str = request.form.get("speechText")
        # transcript=""+ speechText_str
        # print(f"Printing  transcript--1 {transcript}")
        
        # speechText_str = request.form.get("speechText")
        # print("printing speechtext before ",speechText_str)
        if request.method == "GET":
            speechText_str = request.form.get("speechText")
            #transcript=""+ speechText_str
            print(f"Printing  transcript inside get {speechText_str}")

        if request.method == "POST":
            print("FORM DATA RECEIVED")
            # getting input with name = fname in HTML form
            speechText_str = request.form.get("speechText")
            #transcript=""+ speechText_str
            print(f"Printing  transcript inside post {speechText_str}")

            # if "file" not in request.files:
            #     return redirect(request.url)

            # file = request.files["file"]
            # if file.filename == "":
            #     return redirect(request.url)

            # if file:
            #     recognizer = sr.Recognizer()
            #     audioFile = sr.AudioFile(file)
            #     with audioFile as source:
            #         data = recognizer.record(source)
            #     transcript = recognizer.recognize_google(data, key=None)

        ###logic for talking 
        # print("Start talking in headphone")    
        # r = sr.Recognizer()
        # with sr.Microphone() as source:
        #     print("Talk")
        #     audio_text = r.listen(source)
        #     r.pause_threshold = 0.9 
        #     print("Time over, thanks")
        #     # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
        # try:
        #     # using google speech recognition
        #     print("Text: "+r.recognize_google(audio_text))
        #     text:str=r.recognize_google(audio_text)
        #     #print("Text in hindi: "+r.recognize_google(audio_text, language ='hi-In'))
        #     check_messages.append(text)
        # except:
        #     print("Sorry, I did not get that")    
        ## call the check_sentiment.py 
        # print("printing before calling check_sentiment.py")
        # #os.system('check_sentiment.py')
        # check_sentiment.capture_sentiment()
        # print("printing aftre  calling check_sentiment.py")
        if request.method == 'POST':
            if request.form.get('action1') == 'VALUE1':
                print("printing before calling check_sentiment.py")
                check_sentiment.capture_sentiment()
                print("printing aftre  calling check_sentiment.py")
                
        
        return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    print(f" aftre the page has been run , print the check_messages {check_messages}")
    