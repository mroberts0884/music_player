import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class Musicplayer(App):
    def build(self):
       return Label(text='Hello World')

if __name__ == '__main__':
    Musicplayer().run()