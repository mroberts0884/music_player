from kivy.app import App
#require.require("2.3.0")
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.properties import BooleanProperty
from kivy.core.window import Window
import os
import random
from kivy.graphics import Rectangle, Color


Window.size = (400,600)
Window.clearcolor = 255,0,0


class MyBoxLayout(Widget):
    def play(self):
        self.song_list = ['music\LEEONA_-_LEEONA_-_Do_I.mp3', 'music\Soundstatues_-_Amnesia.mp3', 'music\Tab_-_Sake_Bomb_(feat._Jade_Gritty_&amp;_Aurc).mp3' ]
        self.music_list = random.randint(0,2)
        self.sound = SoundLoader.load((self.song_list[self.music_list]))
        if self.sound:
            print("Sound found at %s" % self.sound.source)
            print("Sound is %.3f seconds" % self.sound.length)
            self.sound.play()
    
    def stop(self):
        self.sound.stop()
        
    
class Musicplayer(App):
    def build(self):
        return MyBoxLayout()
    
if __name__ == '__main__':
    Musicplayer().run()