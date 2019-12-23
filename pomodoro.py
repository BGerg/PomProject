#Pomodoro time app
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import *

class Buttons(RelativeLayout):
    def __init__(self, **kwargs):
        super(Buttons, self).__init__(**kwargs)


        button_height = 100
        button_width = 200

        with self.canvas:
            #Progress bar backgorund
            Color(0.26, 0.26, 0.26)
            Ellipse(pos=(225, 200), size=(350, 350))
            #Progress bar foreground
            Color(0, 0, 0)
            Ellipse(pos=(260, 235), size=(280, 280))

        btn1 = Button(text ='START',
                    font_size = 55,
                    size = (button_width,button_height),
                    pos = (20,20),
                    background_color = (0, 245, 0, 1),
                    size_hint =(None,None))
        btn2 = Button(text='STOP',
                    font_size = 55,
                    pos = (300,20),
                    background_color = (0, 0, 255, 1),
                    size = (button_width,button_height),
                    size_hint =(None,None))
        btn3 = Button(text ='RESET',
                    font_size =24,
                    pos = (580,20),
                    background_color = (245, 0, 0, 1),
                    size = (button_width,button_height),
                    size_hint = (None,None))

        btn1.bind(on_press= lambda a:print("btn1 ok"))
        btn2.bind(on_press= lambda a:print("btn2 ok"))
        btn3.bind(on_press= lambda a:print("btn2 ok"))

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)

class PomodoroApp(App):
    def build(self):
        return Buttons()

if __name__ == "__main__":
    PomodoroApp().run()
