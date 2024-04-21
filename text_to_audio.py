import pyttsx3

class TextToSpeech:
    engine: pyttsx3.Engine

    def __init__(self, voice, rate: int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_available_voices(self):
        voices = self.engine.getProperty('voices')
        
        for i, voice in enumerate(voices):
            
            language = voice.languages[0] if voice.languages else 'Unknown language'
            
            print(f'{i + 1} {voice.name} {voice.age}: {language} ({voice.gender}) [{voice.id}]')

    def text_to_speech(self, text: str, save: bool = False, file_name = 'output.mp3'):
        self.engine.say(text)
        print("I am speaking...")
        if save:
            self.engine.save_to_file(text, file_name)
        self.engine.runAndWait()
    