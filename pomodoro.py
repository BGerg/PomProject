#Pomodoro time app
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import *
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.clock import Clock
from playsound import playsound
import time
from kivy.core.text import Label as CoreLabel


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)


        self.minutes = 10
        self.seconds = self.minutes*60
        self.minlen = 60
        self.gro = 360/(self.seconds)
        percentage = 20
        button_height = 100
        button_width = 200
        self.draw(0.0001)
        self.buttons(False)
        self.time_counter()

    def time_counter(self):
        premin = ""
        presec = ""
        if self.minlen > 0:
            self.minlen -= 1
        else:
            self.minutes -= 1
            self.minlen = 59


        self.refresh_text()

    def refresh_text(self):
        premin = ""
        presec = ""
        if self.minutes < 10 :
            premin = "0"
        if self.minlen < 10 :
            presec = "0"

        timetext = premin+str(self.minutes-1)+":"+presec+str(self.minlen)
        self.add_widget(Label(text=timetext,font_size= 60,  pos=(350,350)))

    def printer(self,dt):

        if self.percentage < 360:
            self.draw(self.percentage+self.gro)
            self.buttons(True)
            self.time_counter()
        else:
            self.draw(0.0001)
            playsound('SteelBellC6.wav')
            self.buttons(False)
            Clock.unschedule(self.printer)




    def start(self, instance):
        Clock.schedule_interval(self.printer, 1)
        self.buttons(True)


    def stop(self, instance):
        Clock.unschedule(self.printer)
        self.buttons(False)

    def reset(self, instance):
        self.minlen = 60
        Clock.unschedule(self.printer)
        self.draw(0.0001)
        self.buttons(False)
        self.refresh_text()

    def timeplus(self,instance):
        self.minutes += 5
        self.draw(self.percentage)
        self.buttons(False)
        self.refresh_text()

    def timeminus(self,instance):
        if self.minutes > 5:
            self.minutes -= 5
        self.draw(self.percentage)
        self.buttons(False)
        self.refresh_text()



    def buttons(self, state):

        button_height = 100
        button_width = 200

        btn1 = Button(text = 'START',
                        font_size = 55,
                        size = (button_width,button_height),
                        pos = (20,20),
                        background_color = (0, 245, 0, 1),
                        size_hint =(None,None))
        btn2 = Button(text = 'STOP',
                        font_size = 55,
                        pos = (300,20),
                        background_color = (0, 0, 255, 1),
                        size = (button_width,button_height),
                        size_hint =(None,None))
        btn3 = Button(text = 'RESET',
                        font_size =24,
                        pos = (580,20),
                        background_color = (245, 0, 0, 1),
                        size = (button_width,button_height),
                        size_hint = (None,None))

        btn4 = Button(text = 'Time +5 min',
                        font_size =14,
                        pos = (40,375),
                        background_color = (245, 0, 0, 1),
                        size = (100,50),
                        size_hint = (None,None))

        btn5 = Button(text = 'Time -5 min',
                        font_size =14,
                        pos = (40,325),
                        background_color = (245, 0, 0, 1),
                        size = (100,50),
                        size_hint = (None,None))



        btn1.disabled = state

        btn1.bind(on_press = self.start)
        btn2.bind(on_press = self.stop)
        btn3.bind(on_press = self.reset)
        btn4.bind(on_press = self.timeplus)
        btn5.bind(on_press = self.timeminus)

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)


    def draw(self, percentage):
        self.percentage = percentage
        with self.canvas:
            self.canvas.clear()

            #Progress bar backgorund
            Color(0.26, 0.26, 0.26)
            Ellipse(pos=(225, 200), size=(350, 350))
            #Circular progress line
            Color(1, 0, 0)
            Ellipse(pos=(225, 200), size=(350, 350),
                    angle_end=(self.percentage))
            #Progress bar foreground
            Color(0, 0, 0)
            Ellipse(pos=(260, 235), size=(280, 280))





class PomodoroApp(App):
    def build(self):
        return MyWidget()

if __name__ == "__main__":
    PomodoroApp().run()
