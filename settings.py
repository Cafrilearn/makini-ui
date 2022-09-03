import os
from os.path import join

from kivy.core.window import Window
from kivy.lang import Builder

# Define fonts path
fn_path = join(os.getcwd(), 'assets', 'fonts')

# Define Window size
# Window.fullscreen = True
Window.size = (800, 480)

Builder.load_file("kivy-files/welcome.kv")
Builder.load_file("kivy-files/subject-list.kv")

Builder.load_file("kivy-files/mathematics/start.kv")
Builder.load_file("kivy-files/mathematics/select_operation.kv")
Builder.load_file('kivy-files/mathematics/quiz.kv')
Builder.load_file('kivy-files/mathematics/final_score.kv')
Builder.load_file("kivy-files/mathematics/progressbar.kv")

Builder.load_file("kivy-files/science/start.kv")
Builder.load_file("kivy-files/science/unit-list.kv")
Builder.load_file("kivy-files/science/sub-topics.kv")
Builder.load_file("kivy-files/science/sub-topic-detail.kv")
Builder.load_file("kivy-files/science/content.kv")

Builder.load_file("kivy-files/financial literacy/start.kv")

Builder.load_file("kivy-files/conservation/start.kv")

Builder.load_file("kivy-files/conversation.kv")
