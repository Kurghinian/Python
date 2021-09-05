import pyttsx3
friend = pyttsx3.init()
def aa():
    speech = input(" Say Somethings: ")
    friend.say(speech)
    friend.runAndWait()
    if speech == "exit":
        exit

    aa()
aa()
