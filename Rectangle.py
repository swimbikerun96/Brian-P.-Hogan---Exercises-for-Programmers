import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
import Conversion as c

Builder.load_file('rectangle.kv')


class MyGrid(Widget):

    def populate1(self):
        #Populates the length label at the bottom of the window
        length = self.ids.length.text
        if len(length) == 0:
            self.ids.output1.text = ""
        else:
            self.ids.output1.text = f"length: {length}"

    def populate2(self):
        #populates the width label at the bottom of the window
        width = self.ids.width.text
        if len(width) == 0:
            self.ids.output2.text = ""
        else:
            self.ids.output2.text = f"width: {width}"

    def segue1(self):
        #focuses the other text input and changes text color within the field
        self.ids.length.foreground_color = "#f5b105"
        self.ids.width.foreground_color = "#000000"
        self.ids.width.focus = True
        
    def segue2(self):
        #focuses the other text input and changes text color within the field
        self.ids.width.foreground_color = "#f5b105"
        self.ids.length.foreground_color = "#000000"
        self.ids.length.focus = True

    def area(self):
        
        if self.ids.imperial.active is False and self.ids.metric.active is False:
            #Checks to make sure that the user has checked a box unit of measurement
            self.ids.output3.text = "Please select a unit of measurement"

        elif self.ids.imperial.active is True and self.ids.metric.active is True:
            #Checks to make sure that the user cannot get an area if both checkboxes are checked
            self.ids.output3.text = "Only One System of Measurement at a Time!"
            
        elif self.ids.imperial.active is True:
            #Produces an area statement for when the imperial checkbox is checked
            try:
                w = int(self.ids.width.text)
                l = int(self.ids.length.text)
                a = w * l
                self.ids.output3.text = f"with a width of {w} feet,\nand a length of {l} feet,\nyour area is {a} square feet!"
                self.ids.convert.background_color = "#f5b105"
                self.ids.convert.text = "See Metric Equivalent"
            except ValueError:
                self.ids.output3.text = "Please Enter Both Length and Width"
                
        elif self.ids.metric.active is True:
            #Produces an area statement for when the metric checkbox is checked
            try:
                w = int(self.ids.width.text)
                l = int(self.ids.length.text)
                a = w * l
                self.ids.output3.text = f"with a width of {w} meters,\nand a length of {l} meters,\nyour area is {a} square meters!"
                self.ids.convert.background_color = "#f5b105"
                self.ids.convert.text = "See Imperial Equivalent"
            except ValueError:
                self.ids.output3.text = "Please Enter Both Length and Width"

    def convert(self):
        if self.ids.imperial.active is True:
            #convert imperial input to metric in the output statement
            l = self.ids.length.text
            w = self.ids.width.text
            metric_conversion = c.metric(l, w)
            self.ids.output3.text = f"Metric area is {metric_conversion} meters squared!"
            self.ids.reset.background_color = "#408c11"
            self.ids.reset.text = "Reset"
        elif self.ids.metric.active is True:
            #convert metric input to imperial in the output statement
            l = self.ids.length.text
            w = self.ids.width.text
            imperial_conversion = c.imperial(l, w)
            self.ids.output3.text = f"Imperial area is {imperial_conversion} feet squared!"
            self.ids.reset.background_color = "#408c11"
            self.ids.reset.text = "Reset"

    def reset(self):
        #reset all of the input fields
        self.ids.width.text = ""
        self.ids.length.text = ""
        self.ids.imperial.active = False
        self.ids.metric.active = False
        self.ids.length.focus = True
        self.ids.convert.text = "Convert"

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
