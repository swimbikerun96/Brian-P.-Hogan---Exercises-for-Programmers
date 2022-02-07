import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder

def ftc(degrees):
    f = degrees
    c = (f-32) * (5/9)
    return f'The temperature in Celsius is {round(c,2)}'
def ftk(degrees):
    f = degrees
    k = (((f - 32) * 5)/9) + 273.15
    return f'The temerature in Kelvin is {round(k,2)}'
#Function for Celsius To Fahrenheit
def ctf(degrees):
    c = degrees
    f = ((c*9)/5) + 32
    return f'The temperature in Fahrenheit is {round(f,2)}'
#Function for Celsius to Kelvin
def ctk(degrees):
    c = degrees
    k = c + 273.15
    return f'The Temperature in Kelvin is {round(k,2)}'
#Function for Kelvin to Fahrenheit
def ktf(degrees):
    k = degrees
    f = (((k-273.15)*9)/5) + 32
    return f'The Temperature in Fahrenheit is {round(f,2)}'
#Function for Kelvin to Celsius
def ktc(degrees):
    k = degrees
    c = k - 273.15
    return f'The Temperature in Celsius is {round(c,2)}'

Builder.load_file('UI.kv')
class MyGrid(Widget):
    #function to reset the slider when a new checkbox is selected
    def clear(self):
        if self.ids.kelvin.active == True:
            self.ids.temp.min = -273.16
            self.ids.temp.max = 273.15
            self.ids.temp.value = -273.15
        elif self.ids.celsius.active == True:
            self.ids.temp.min = -19
            self.ids.temp.max = 100
            self.ids.temp.value = -18
        elif self.ids.fahrenheit.active == True:
            self.ids.temp.min = -1
            self.ids.temp.max = 212
            self.ids.temp.value = 0
        elif self.ids.celsius.active == False and self.ids.fahrenheit.active == False and self.ids.kelvin.active == False:
            self.ids.temp.value = self.ids.temp.min
            self.ids.output.text = 'Make Sure to Select a Scale!'
    #function to set label with temperature value
    def set_label(self,*args):
        if self.ids.fahrenheit.active == True:
            if self.ids.temp.value < 0:
                self.ids.output.text = 'Use the Slider To Set The Temperature!'
            else:
                #To Celsius
                tc = ftc(self.ids.temp.value)
                #To Kelvin
                tk = ftk(self.ids.temp.value)
                self.ids.output.text = f'{round(self.ids.temp.value,2)}° F\n{tc}°\n{tk}°'
        elif self.ids.kelvin.active == True:
            if self.ids.temp.value == -273.16:
                self.ids.output.text = 'Use the Slider To Set The Temperature!'
            else:
                #To Fahrenheit
                tf = ktf(self.ids.temp.value)
                #To Celsius
                tc = ktc(self.ids.temp.value)
                self.ids.output.text = f'{round(self.ids.temp.value,2)}° K\n{tf}°\n{tc}°'
        elif self.ids.celsius.active == True:
            if self.ids.temp.value == -19:
                self.ids.output.text = 'Use the Slider To Set The Temperature!'
            else:
                #To Fahrenheit
                tf = ctf(self.ids.temp.value)
                #To Kelvin
                tk = ctk(self.ids.temp.value)
                self.ids.output.text = f'{round(self.ids.temp.value,2)}° C\n{tf}°\n{tk}°'
        else:
            self.ids.output.text = 'Make Sure to Select a Scale!'
class TemperatureApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    TemperatureApp().run()
