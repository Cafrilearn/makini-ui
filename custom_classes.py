import random

from kivy.clock import Clock
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.utils import rgba, get_color_from_hex
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior, FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout


class WelcomeScreen(Screen):
    def current_slide(self, index):
        for slide in range(3):
            if index == slide:
                self.ids[f"slide{index}"].color = get_color_from_hex('#00A18D')
            else:
                self.ids[f"slide{slide}"].color = rgba(233, 237, 240, 255)

    def next(self):
        self.ids.carousel.load_next(mode='next')

    def prev(self):
        self.ids.carousel.load_previous()


class SubjectListScreen(Screen):
    pass


class SearchBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class Card(MDCard):
    image_source = StringProperty()
    title_text = StringProperty()
    description = StringProperty()
    background_color = ListProperty([1, 1, 1, 1])


class SubjectCard(MDCard):
    heading_text = StringProperty()
    description_text = StringProperty()
    icon_name = StringProperty()


class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    """ Implements a material design v3 card. """
    text = StringProperty()


class MathStartScreen(Screen):
    """ Implements the Mathematics start Screen """


class SelectOperationScreen(Screen):
    """ Implements the Select Operation in the math subject """


class OperationButton(FakeRectangularElevationBehavior, Button):
    """ Implements the Op button for the mathematical operations """
    bg_color = ListProperty([1, 1, 1, 1])
    background_img = StringProperty()
    description = StringProperty()


class OptionButton(Button):
    """ Implements the option button for the mathematical quiz """
    bg_color = ListProperty([1, 1, 1, 1])


class QuizScreen(Screen):
    """ Implements the Quiz Screen """
    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.answer = None
        self.selected_sign = ""
        self.correct = 0
        self.wrong = 0
        self.score = 0
        self.qn_number = 1

    def select_sign(self, sign):
        self.manager.current = 'quiz'
        self.selected_sign = sign
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        self.manager.get_screen('quiz').ids.question.text = f"{num1} {sign} {num2} = ?"

        if sign == "+":
            self.answer = str(num1 + num2)
        elif sign == "–":
            self.answer = str(num1 - num2)
        elif sign == "×":
            self.answer = str(num1 * num2)
        elif sign == "÷":
            self.answer = str(round((num1 / num2), 2))

        option_list = [self.answer]
        option_len = 1
        while option_len < 4:
            option = 0
            if sign == "+":
                option = random.randint(1, 20)
            elif sign == "–":
                option = random.randint(-10, 10)
            elif sign == "×":
                option = random.randint(1, 100)
            elif sign == "÷":
                option = str(round(random.uniform(1, 10), 2))
            if option not in option_list:
                option_list.append(option)
            else:
                option_len -= 1
            option_len += 1

        random.shuffle(option_list)
        for i in range(1, 5):
            self.manager.get_screen('quiz').ids[f"option_{i}"].text = str(option_list[i - 1])

    def get_id(self, instance):
        for id, widget in enumerate(reversed(instance.parent.children), start=1):
            if widget.__self__ == instance:
                return f"option_{id}"

    def quiz(self, option, instance):
        if option == self.answer:
            self.ids[self.get_id(instance)].bg_color = [0, 1, 0, 1]
            option_id_list = [f"option_{i}" for i in range(1, 5)]
            option_id_list.remove(self.get_id(instance))
            for option_id in option_id_list:
                self.ids[option_id].disabled = True
            self.correct += 1
        else:
            for i in range(1, 5):
                if self.ids[f"option_{i}"].text == self.answer:
                    self.ids[f"option_{i}"].bg_color = [0, 1, 0, 1]
                else:
                    self.ids[f"option_{i}"].disabled = True
            self.ids[self.get_id(instance)].bg_color = [1, 0, 0, 1]
            self.ids[self.get_id(instance)].disabled_color = [1, 1, 1, 1]
            self.wrong += 1

    def next_question(self):
        self.select_sign(self.selected_sign)
        self.qn_number += 1
        self.ids.question_number.text = f"{self.qn_number} of 10"
        for i in range(1, 5):
            self.ids[f"option_{i}"].disabled = False
            self.ids[f"option_{i}"].bg_color = (40/255, 6/255, 109/255, 1)
            self.ids[f"option_{i}"].disabled_color = (1, 1, 1, .3)

    def replay(self):
        self.correct = 0
        self.wrong = 0
        self.manager.current = 'select_operation'

    def final_score(self):
        if self.correct == 0 and self.wrong == 0:
            self.manager.current = 'select_operation'
        else:
            for i in range(1, 5):
                self.ids[f"option_{i}"].disabled = False
                self.ids[f"option_{i}"].bg_color = (40 / 255, 6 / 255, 109 / 255, 1)
                self.ids[f"option_{i}"].disabled_color = (1, 1, 1, .3)
            percentage_score = round((self.correct/(self.correct + self.wrong)) * 100)
            final_score_screen = self.manager.get_screen('final_score')
            final_score_screen.correct.text = f"{self.correct} out of {self.correct + self.wrong}"
            final_score_screen.wrong.text = f"{self.wrong} Wrong"
            final_score_screen.ids.correct_text.text = f"{self.correct} Correct"
            final_score_screen.ids.percentage_score.score = percentage_score

            self.manager.current = 'final_score'


class FinalScoreScreen(Screen):
    """ Implements the final score screen """


class CircularProgressBar(AnchorLayout):
    """ Implements the circular progress bar """
    score = NumericProperty(80)
    bar_width = NumericProperty(10)
    set_value = NumericProperty(80)
    text = StringProperty("80%")
    duration = NumericProperty(1.5)
    counter = 0

    def __int__(self, **kwargs):
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


class ScienceStartScreen(Screen):
    """ Implements the Science start screen """


class FinancialLiteracyStartScreen(Screen):
    """ Implements the Financial Literacy start screen """


class ConservationStartScreen(Screen):
    """ Implements the Conservation start screen """
