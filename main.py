from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from kivy.uix.screenmanager import SlideTransition

from custom_classes import *
from settings import *


class MakiniApp(MDApp):
    def __init__(self, **kwargs):
        super(MakiniApp, self).__init__(**kwargs)
        self.screen_manager = ScreenManager()
        if os.path.exists("marker.txt"):
            f = open("marker.txt", 'w')
        else:
            self.screen_manager.add_widget(WelcomeScreen())
            f = open("marker.txt", 'a')

    def build(self):
        self.screen_manager.add_widget(SubjectListScreen())
        self.screen_manager.add_widget(MathStartScreen())
        self.screen_manager.add_widget(SelectOperationScreen())
        self.screen_manager.add_widget(QuizScreen())
        self.screen_manager.add_widget(FinalScoreScreen())

        self.screen_manager.add_widget(ScienceStartScreen())

        self.screen_manager.add_widget(FinancialLiteracyStartScreen())

        self.screen_manager.add_widget(ConservationStartScreen())
        return self.screen_manager

    def change_screen(self, screen_name):
        self.screen_manager.transition = SlideTransition()
        self.screen_manager.current = screen_name


if __name__ == "__main__":
    LabelBase.register(
        name="MPoppins",
        fn_regular=os.path.join(fn_path, "Poppins-Medium.ttf"),
    )
    LabelBase.register(
        name="BPoppins",
        fn_regular=os.path.join(fn_path, "Poppins-Bold.ttf"),
    )
    LabelBase.register(
        name="RPoppins",
        fn_regular=os.path.join(fn_path, 'Poppins-Regular.ttf'),
    )
    MakiniApp().run()

