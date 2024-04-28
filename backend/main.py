# backend\main.py
from recorder import main as record_audio
from speech_recognition import main as recognize_speech

def main():
    # Record audio and save to a file
    print("Recording audio")
    record_audio()
    print("Done recording audio")

    # Perform speech recognition on the recorded audio
    print("Doing speech to text")
    recognized_text = recognize_speech()
    print(f"Recognized text: {recognized_text}")

if __name__ == "__main__":
    main()