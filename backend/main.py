# backend\main.py
from backend.recorder import main as record_audio
from backend.speech_recognition import main as recognize_speech

def main():
    # Record audio and save to a file
    record_audio("output.wav")

    # Perform speech recognition on the recorded audio
    recognized_text = recognize_speech("output.wav")
    print(f"Recognized text: {recognized_text}")

if __name__ == "__main__":
    main()