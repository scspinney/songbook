import speech_recognition as sr
import re
import pyttsx3
import subprocess
import requests

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/enter_chorus', methods=['GET', 'POST'])
# def enter_chorus():
#     if request.method == 'POST':
#         # Process the submitted lyrics and redirect to the main page
#         pass
#     else:
#         return render_template('enter_chorus.html')


def listen_for_chorus(r,engine):
    """Listens for the chorus and returns the lyrics as a string."""
    print("Say the chorus: ")
    with sr.Microphone() as source:
        # Listen until the keyword is spoken
        while True:
            audio = r.listen(source)

            # Convert the chorus to text
            try:
                chorus = r.recognize_google(audio)
                print("Chorus: " + chorus)
            except Exception as e:
                print("Sorry, I couldn't understand you.")

            # Check if the keyword was spoken
            if "end" in chorus or "finished" in chorus:
                break

    # Use a regular expression to remove the keyword from the lyrics
    chorus = re.sub(r"\b(end|finished)\b", "", chorus)

    # Read the verse back to you
    engine.say(chorus)
    engine.runAndWait()

    return chorus


def listen_for_verses(r,engine):
    """Listens for the verses and returns a list of lyrics as strings."""
    # Initialize the list of verses
    verses = []

    # Listen for each verse
    num_verses = input("How many verses does the song have? ")
    for i in range(int(num_verses)):
        print(f"Say verse {i+1}: ")
        with sr.Microphone() as source:
            while True:
                audio = r.listen(source)

                # Convert the verse to text
                try:
                    verse = r.recognize_google(audio)
                    print(f"Verse {i+1}: " + verse)
                    verses.append(verse)
                except Exception as e:
                    print("Sorry, I couldn't understand you.")
                
                # Check if the keyword was spoken
                if "end" in verse or "finished" in verse:
                    break
                
                # Read the verse back to you
                engine.say(verse)
                engine.runAndWait()
    # Use a regular expression to remove the keyword from the lyrics
    verses = [re.sub(r"\b(end|finished)\b", "", verse) for verse in verses]

    return verses


def create_latex_songbook(chorus,verses,name="songbook"):
    # Use latex to create the songbook
    with open(f"{name}.tex", "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\begin{document}\n")
        f.write("\\section*{Lyrics}\n")

        # Write the chorus and verses to the songbook
        f.write("\\subsection*{Chorus}\n")
        f.write(chorus + "\n")
        for i, verse in enumerate(verses):
            f.write("\\subsection*{{Verse {}}}".format(i+1))
            f.write(verse + "\n")

        f.write("\\end{document}")



if __name__ == '__main__':
    #app.run()


# Set up the speech recognition
r = sr.Recognizer()
engine = pyttsx3.init()
name="songbook"

chorus = listen_for_chorus(r,engine)
verses = listen_for_verses(r,engine)
create_latex_songbook(chorus,verses,name)


# Compile the tex file using pdflatex
#subprocess.run(["pdflatex", f"{name}.tex"])
