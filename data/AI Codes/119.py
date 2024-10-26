import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    print("Text-to-Speech Converter")
    text = input("Enter text: ")
    text_to_speech(text)

if __name__ == "__main__":
    main()
