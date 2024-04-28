# backend\main.py
from recorder import main as record_audio
from speech_recognition import main as recognize_speech
from client_auth import client

def speech_text(): 
    # Record audio and save to a file
    print("Recording audio")
    record_audio()
    print("Done recording audio")

    # Perform speech recognition on the recorded audio
    print("Doing speech to text")
    recognized_text = recognize_speech()
    print(f"Recognized text: {recognized_text}")
    return recognized_text

def main():
    # Record audio and save to a file
    r_text = speech_text() 
    bool_variable = False

    while(len(r_text) > 280): 
        print("For the love of god stop yapping and try again")
        r_text = speech_text()

    while(bool_variable == False):
        print("Is this to your liking? ")
        choice = input("Y or N: ")
        if(choice == 'Y'):
            bool_variable = True
            print("Creating Tweet:")
            client.create_tweet(text = r_text, user_auth = True)
            print("Tweeted")
        else:
            r_text = speech_text() 

if __name__ == "__main__":
    main()