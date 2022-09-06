from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy import Config

from kivy.uix.screenmanager import SlideTransition

from custom_classes import *
from settings import *


class MakiniApp(MDApp):
    def __init__(self, **kwargs):
        super(MakiniApp, self).__init__(**kwargs)
        self.screen_manager = ScreenManager()
        # if os.path.exists("marker.txt"):
        #     f = open("marker.txt", 'w')
        # else:
        #     self.screen_manager.add_widget(WelcomeScreen())
        #     f = open("marker.txt", 'a')

    def build(self):
        self.screen_manager.add_widget(SplashScreen())
        self.screen_manager.add_widget(WelcomeScreen())

        self.screen_manager.add_widget(SubjectListScreen())

        # Mathematics
        self.screen_manager.add_widget(MathStartScreen())
        self.screen_manager.add_widget(SelectOperationScreen())
        self.screen_manager.add_widget(QuizScreen())
        self.screen_manager.add_widget(FinalScoreScreen())

        # Science
        self.screen_manager.add_widget(ScienceStartScreen())
        self.screen_manager.add_widget(ScienceUnitListScreen())
        self.screen_manager.add_widget(ScienceSubTopicScreen())
        self.screen_manager.add_widget(ScienceContentScreen())
        # self.screen_manager.add_widget(ScienceSubTopicDetailScreen())

        # Financial Literacy
        self.screen_manager.add_widget(FinancialLiteracyStartScreen())

        # Conversation
        self.screen_manager.add_widget(ConversationScreen())

        # Conservation
        self.screen_manager.add_widget(ConservationStartScreen())
        return self.screen_manager

    def change_screen(self, screen_name):
        self.screen_manager.transition = SlideTransition()
        self.screen_manager.current = screen_name


if __name__ == "__main__":
    # Config.set('graphics', 'fullscreen', 0)
    # Config.set('graphics', 'window_state', 'visible')
    # Config.write()
    Config.set('kivy', 'keyboard_mode', 'systemandmulti')

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
