from kivy.core.audio import SoundLoader


class Audio():

    def playAudio(filename):
        """Plays the given audio file"""
        SoundLoader.load(filename).play()
