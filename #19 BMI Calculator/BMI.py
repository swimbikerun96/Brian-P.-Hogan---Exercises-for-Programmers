import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.widget import Widget
import math

Builder.load_file('UI.kv')

class MyGrid(Widget):
    #Print to the screen the weight selected by the user
    def weight_display(self, *args):
        if self.ids.metric.active == True:
            self.ids.weight_slide.max = 150
            message = str(int(self.ids.weight_slide.value)) + " kilograms"
            self.ids.weight_label.text = message
        elif self.ids.imperial.active == True:
            self.ids.weight_slide.max = 300
            message = str(int(self.ids.weight_slide.value)) + " pounds"
            self.ids.weight_label.text = message
        elif self.ids.metric.active == False and self.ids.imperial.active == False:
            self.ids.weight_label.text = "Please select\na unit of measurement!"
    #Print to the screen the height selected by the user
    def height_display(self, *args):
        if self.ids.metric.active == True:
            self.ids.height_slide.max = 2.15
            self.ids.height_slide.step = .1
            message = str(round(self.ids.height_slide.value,2)) + " meters"
            self.ids.height_label.text = message
        elif self.ids.imperial.active == True:
            self.ids.height_slide.max = 84
            self.ids.height_slide.step = 1
            feet = math.floor(self.ids.height_slide.value / 12)
            inches = int(self.ids.height_slide.value % 12)
            self.ids.height_label.text = str(feet) + " feet and " + str(inches) + " inches"
        elif self.ids.imperial.active == False and self.ids.metric.active == False:
            self.ids.height_label.text = "Please select\na unit of measurement!"
    #Clear all Labels as a means of resetting the application
    def clear(self):
        self.ids.weight_label.text = ''
        self.ids.weight_slide.value = 0
        self.ids.height_label.text = ''
        self.ids.height_slide.value = 0
        self.ids.output.text = ''
    #Calculate and display BMI
    def calc(self, *args):
        try:
            if self.ids.imperial.active == True:
                weight = self.ids.weight_slide.value
                if weight == 0:
                    raise ZeroDivisionError
                height = self.ids.height_slide.value
                bmi = str(round(((weight/(height * height)) * 703),2))
                self.ids.output.text = f'Your BMI is {bmi}.'
                if 18.5 <= float(bmi) <= 25:
                    self.ids.output.color = "#56fc03"
                else:
                    self.ids.output.color = "#fc0303"
            elif self.ids.metric.active == True:
                weight = self.ids.weight_slide.value
                height = self.ids.height_slide.value
                bmi = str(round(weight / (height * height),2))
                if 18.5 <= float(bmi) <= 25:
                    self.ids.output.color = "#56fc03"
                else:
                    self.ids.output.color = "#fc0303"
                if weight == 0:
                    raise ZeroDivisionError
                self.ids.output.text = f'Your BMI is {bmi}.'
        except ZeroDivisionError:
            self.ids.output.color = "#ffffff"
            self.ids.output.text = 'Select Values for Both Height and Weight'
                        
class BMIApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    BMIApp().run()
