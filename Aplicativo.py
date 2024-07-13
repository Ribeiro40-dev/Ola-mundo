
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Test(App):
    def build(self): 
        box = BoxLayout()
        
        return Button(text='Projeto Saúde')

Test().run() 