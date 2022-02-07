from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder
import pw

Builder.load_file('UI.kv')

#Dictionary to match up returned values from function to statements for the user
strength_dict = {
    0 : "You need at least on character to start",
    1 : "is a very weak password.",
    2 : "is a weak password.",
    3 : "is complex, yet short. Consider revising.",
    4 : "is a strong password.",
    5 : "is a very strong password.",
    6 : "is long, yet simple. Consider revising."
    }

class PassWordGrid(Widget):
    #Connect to first file to leverage the function for our GUI
    def strength_check(self):
        password = self.ids.input.text
        strength = pw.passwordValidator(password)
        if len(password) == 0:
            output = f'{strength_dict[strength]}'
        else:
            output = f'"{password}" {strength_dict[strength]}'
        self.ids.output.text = output

class PasswordValidator(App):
    def build(self):
        return PassWordGrid()

if __name__ == "__main__":
    PasswordValidator().run()
