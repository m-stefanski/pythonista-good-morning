import sys


class TTS:

    speak_function = None

    def __init__(self):
        # If running recent version of Pythonista on iOS
        if 'Pythonista3' in sys.base_exec_prefix:
            import speech

            def announce(text):
                speech.say(text, "pl_PL")

        # If running Pydroid 3 on Android
        # elif 'pydroid3' in sys.base_exec_prefix:

        # Other cases
        else:
            def announce(text):
                print(text)

        self.speak_function = announce

    def speak(self, text):
        self.speak_function(text)
