import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_string(
    """
<MyGrid>:
    GridLayout:
        cols: 1
        size: root.width, root.height

        Label:
            font_size: 32
            id: output

        TextInput:
            id: input
            halign: "center"
            focus: True
            font_size: 32
            on_text: root.present()
            """
    )

class MyGrid(Widget):
    def present(self):
        i = len(self.ids.input.text)
        if i == 0:
            self.ids.output.text = "Please Input a string!"
        elif i == 1:
            self.ids.output.text = f'"{self.ids.input.text}" is {str(i)} character'
        else:
            self.ids.output.text = f'"{self.ids.input.text}" has {str(i)} characters'

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
