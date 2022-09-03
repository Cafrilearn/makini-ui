import math
import random
from threading import Thread
from time import sleep

import pygame.event
from kivy.clock import Clock
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex as hex_color
from kivy.utils import rgba, get_color_from_hex
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior, FakeRectangularElevationBehavior
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from pygame import mixer

from db import db


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
    """ Implements the subject list screen """
    def __init__(self, **kwargs):
        super(SubjectListScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.list_subjects, 0)

    def list_subjects(self, *args):
        for subject in db:
            self.ids.subject_list.add_widget(
                Card(
                    background_color=hex_color(db[subject]["bg_color"]),
                    image_source=db[subject]['image'],
                    title_text=subject.title(),
                    description=db[subject]['description']
                )
            )


class SearchBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class Card(MDCard):
    image_source = StringProperty()
    title_text = StringProperty()
    description = StringProperty()
    background_color = ListProperty([1, 1, 1, 1])


class UnitCard(MDCard):
    subject = StringProperty()
    unit = StringProperty()
    unit_description = StringProperty()


class SubTopicCard(MDCard):
    subtopic_title = StringProperty()
    subject = StringProperty()
    completion = StringProperty()
    progress = NumericProperty()
    subtopic_description = StringProperty()


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

            final_score_screen.ids.circular_progress_bar.clear_widgets()

            final_score_screen.ids.circular_progress_bar.add_widget(
                CircularProgressBar(
                    score=percentage_score,
                    text=str(percentage_score)+"%",
                    set_value=percentage_score
                )
            )
            self.manager.current = 'final_score'


class CircularProgressBar(AnchorLayout):
    """ Implements the circular progress bar """
    score = NumericProperty(80)
    bar_width = NumericProperty(10)
    set_value = NumericProperty(80)
    text = StringProperty("100%")
    duration = NumericProperty(1.5)
    counter = 0

    def __int__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)

    def animate(self, *args):
        Clock.schedule_interval(self.percentage_counter, self.duration/self.score)

    def percentage_counter(self, *args):
        if self.counter < self.score:
            self.counter += 1
            self.text = f"{self.counter}%"
            self.set_value = self.counter
        else:
            Clock.unschedule(self.percentage_counter)


class FinalScoreScreen(Screen):
    """ Implements the final score screen """


class ScienceStartScreen(Screen):
    """ Implements the Science start screen """


class FinancialLiteracyStartScreen(Screen):
    """ Implements the Financial Literacy start screen """


class ConservationStartScreen(Screen):
    """ Implements the Conservation start screen """


class ScienceUnitListScreen(Screen):
    """ Implements the Science Unit List screen """

    def __init__(self, **kwargs):
        super(ScienceUnitListScreen, self).__init__(**kwargs)
        self.subject_title = StringProperty()

    def list_units(self, subject):
        subject = subject.lower()

        if subject == "mathematics":
            self.manager.transition = SlideTransition()
            self.manager.current = "Mathematics"
        else:
            self.subject_title = StringProperty(subject)
            self.ids.subject_title.text = subject.upper()
            self.ids.welcome_message.text = db[subject]['description']
            self.ids.welcome_image.source = db[subject]['image']
            self.ids.unit_list.clear_widgets()
            self.manager.current = 'ScienceUnitListScreen'

            for i in range(3, len(db[subject])):
                self.ids.unit_list.add_widget(
                    UnitCard(
                        unit=list(db[subject].keys())[i].title(),
                        unit_description=db[subject][list(db[subject].keys())[i]]['description'],
                    )
                )


class ScienceSubTopicScreen(Screen):
    """ Implements the Science Sub Topic Screen """
    completion = StringProperty('50% remaining')
    progress = NumericProperty(50)

    def __init__(self, **kwargs):
        super(ScienceSubTopicScreen, self).__init__(**kwargs)

    def selected_unit(self, instance, unit):
        self.ids.subtopic_grid.clear_widgets()

        subject = instance.parent.parent.parent.parent.parent.ids.subject_title.text.lower()
        unit = unit.lower()

        subtopics_dict = db[subject][unit]
        subtopics_keys = list(db[subject][unit].keys())[1:]

        for subtopic in subtopics_keys:
            self.ids.subtopic_grid.add_widget(
                SubTopicCard(
                    completion=self.completion.upper(),
                    progress=self.progress,
                    subject=subject,
                    subtopic_title=subtopic.title(),
                    subtopic_description=subtopics_dict['description']
                )
            )

        self.ids.welcome_title.text = unit.upper()
        self.ids.welcome_description.text = db[subject][unit]['description']
        self.ids.welcome_image.source = db[subject]['image']

        self.manager.current = "ScienceSubTopicScreen"


class LabelCard(MDCard):
    label_text = StringProperty()


class Content(MDFloatLayout):
    """ Implements the content of the Science Sub Topic Detail screen """


class ScienceContentScreen(Screen):
    """ Implements the Science Content screen """
    def __init__(self, **kwargs):
        super(ScienceContentScreen, self).__init__(**kwargs)
        self.song_length = None
        mixer.init()

        self.subject = None
        self.unit = None
        self.subtopic = None
        self.subtopic_content = None
        self.headings = None
        self.song = None
        self.played = False
        self.t = Thread(target=self.check_music_pos, args=(self.song,))

    def go_back(self, *args):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ScienceSubTopicScreen'
        self.stop_music()

    def display_content(self, instance, subtopic):
        self.ids.sections_grid.clear_widgets()
        self.ids.content_detail.clear_widgets()

        self.subject = instance.subject
        self.unit = instance.parent.parent.parent.parent.parent.ids.welcome_title.text.lower()
        self.subtopic = subtopic.lower()
        self.subtopic_content = db[self.subject][self.unit][self.subtopic]

        self.headings = list(self.subtopic_content['content'].keys())

        for i in range(len(self.headings)):
            self.ids.sections_grid.add_widget(
                NavigationButton(
                    text=self.headings[i].title(),
                )
            )

        self.ids.sections_grid.add_widget(
            NavigationButton(
                text=f"Back to SubTopics",
                line_color=hex_color("#00a18d"),
                text_color=hex_color("#00a18d"),
            )
        )

        self.ids.content_detail.add_widget(
            ContentDetail(
                heading=self.headings[0].upper(),
                content=self.subtopic_content['content'][self.headings[0]]['content'],
                image=self.subtopic_content['content'][self.headings[0]]['image'],
            )
        )
        self.load_music(self.headings[0])

        self.manager.transition = SlideTransition()
        self.manager.current = "ScienceContentScreen"

    def seek_content(self, heading):
        heading = heading.lower()
        self.ids.content_detail.clear_widgets()
        self.stop_music()
        self.load_music(heading)
        self.ids.content_detail.add_widget(
            ContentDetail(
                heading=heading.upper(),
                content=self.subtopic_content['content'][heading]['content'],
            )
        )

    def check_music_pos(self, song, *args):

        while True:
            current = pygame.mixer.music.get_pos()/1000
            percentage = (current/self.song_length)*100
            self.ids.audio_progress_bar.value = percentage

            if abs(current - self.song_length) <= 1:
                self.played = False
                self.ids.audio_progress_bar.value = 100
                self.ids.play_pause_replay_button.icon = "replay"
                break
            else:
                sleep(.1)

    def stop_music(self):
        self.ids.play_pause_replay_button.icon = "play-circle-outline"
        self.played = False
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    def load_music(self, heading):
        self.song = mixer.Sound(self.subtopic_content['content'][heading]['audio'])
        self.song_length = self.song.get_length()
        mixer.music.load(self.subtopic_content['content'][heading]['audio'])
        self.t = Thread(target=self.check_music_pos, args=(self.song,))
        self.t.daemon = True
        mixer.music.set_volume(0.5)

    def audio_controller(self):
        option = self.ids.play_pause_replay_button.icon

        if option == "replay":
            mixer.music.play()
            if self.t.is_alive():
                pass
            else:
                self.t = Thread(target=self.check_music_pos, args=(self.song,))
                self.t.daemon = True
                self.t.start()
            self.played = True
            self.ids.play_pause_replay_button.icon = "pause-circle-outline"

        elif option == "play-circle-outline" and self.played:
            mixer.music.unpause()
            self.ids.play_pause_replay_button.icon = "pause-circle-outline"

        elif option == "play-circle-outline" and not self.played:
            self.t.start()
            mixer.music.play()
            self.ids.play_pause_replay_button.icon = "pause-circle-outline"
            self.played = True

        elif option == "pause-circle-outline":
            mixer.music.pause()
            self.ids.play_pause_replay_button.icon = "play-circle-outline"

    def on_leave(self):
        self.stop_music()


class NavigationButton(MDFlatButton):
    """ Implements the Navigation Button """
    text = StringProperty()
    subtopic = StringProperty()
    line_color = ListProperty([0, 0, 0, .9])
    text_color = ListProperty([0, 0, 0, .7])

    def on_release(self):
        if 'back' in self.text.lower():
            self.parent.parent.parent.parent.parent.go_back()
        else:
            self.parent.parent.parent.parent.parent.seek_content(self.text)


class ContentDetail(BoxLayout):
    heading = StringProperty("4. Cells in mammals")
    image = StringProperty("assets/images/science/science lab.png")
    content = StringProperty()


class ScrollableLabel(ScrollView):
    text = StringProperty("")
