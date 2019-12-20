#Pomodoro time app
from kivy.app import App
from kivy.uix.button import Button

class PomodoroApp(App):
    def build(self):
        return Button(text='Start', font_size=24, size =(200,100), size_hint=(None,None))

PomodoroApp().run()
