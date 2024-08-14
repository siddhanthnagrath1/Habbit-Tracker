from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class Habit(BoxLayout):
    def __init__(self, habit_name, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.habit_label = Label(text=habit_name)
        self.add_widget(self.habit_label)

class HabitTracker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.habit_list = BoxLayout(orientation='vertical')
        self.add_widget(self.habit_list)

        self.add_habit_button = Button(text='Add Habit')
        self.add_habit_button.bind(on_press=self.show_add_habit_popup)
        self.add_widget(self.add_habit_button)

    def show_add_habit_popup(self, instance):
        content = BoxLayout(orientation='vertical')
        self.new_habit_input = TextInput(hint_text='Habit name')
        content.add_widget(self.new_habit_input)
        
        add_button = Button(text='Add')
        add_button.bind(on_press=self.add_habit)
        content.add_widget(add_button)
        
        self.popup = Popup(title='Add New Habit', content=content, size_hint=(0.8, 0.5))
        self.popup.open()

    def add_habit(self, instance):
        habit_name = self.new_habit_input.text
        if habit_name:
            self.habit_list.add_widget(Habit(habit_name))
            self.popup.dismiss()

class HabitTrackerApp(App):
    def build(self):
        return HabitTracker()

if __name__ == '__main__':
    HabitTrackerApp().run()
