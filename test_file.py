from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.app import MDApp

kv = '''
#:import hex_color kivy.utils.get_color_from_hex

<CircularProgressBar>:
    canvas.before:
        Color:
            rgb: 1, 0, 0, .7
        Line:
            width: root.bar_width
            ellipse: (self.x, self.y, self.width, self.height, 0, 360)
    canvas.after:
        Color:
            rgb: hex_color("#00a18d")
        Line:
            width: root.bar_width
            ellipse: (self.x, self.y, self.width, self.height, 0, root.set_value*3.6)

    MDLabel:
        text: root.text
        font_size: "50sp"
        pos_hint: {"center_x": .45, "center_y": .5}
        halign: "center"
        color: 0, 0, 0, .8
     

MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    CircularProgressBar:
        id: percentage_score
        size_hint: None, None
        size: 160, 160
        pos_hint: {"center_x": .5, "center_y": .5}
        score: 2
'''


class CircularProgressBar(AnchorLayout):
    """ Implements the circular progress bar """
    score = NumericProperty(80)
    bar_width = NumericProperty(10)
    set_value = NumericProperty(80)
    text = StringProperty("80%")
    duration = NumericProperty(1.5)
    counter = 0

    def __int__(self, **kwargs):
        print("initialized")
        super(CircularProgressBar, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)

    def animate(self, *args):
        Clock.schedule_interval(self.percentage_counter, self.duration/self.score)

    def percentage_counter(self, *args):
        print("Called")
        if self.counter < self.score:
            print("running")
            self.counter += 1
            self.text = f"{self.counter}%"
            self.set_value = self.counter
        else:
            Clock.unschedule(self.percentage_counter)


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


MainApp().run()