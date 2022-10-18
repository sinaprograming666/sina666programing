from cProfile import label
from cgitb import text
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Myapp(App):
    def ozarb(self,instance):
        self.lbl3.text=str(int(self.txt1.text) * int(self.txt2.text))

    def build(self):
       lbl1=Label(text="number:")
       self.txt1=TextInput(multiline=False)
       lbl2=Label(text="number:")
       self.txt2=TextInput(multiline=False)
       zarb=Button(text="*")
       zarb.bind(on_press=self.ozarb)
       taghsim=Button(text="/")
       jam=Button(text="+")
       menha=Button(text="-")
       mosavi=Button(text="=")
       self.lbl3=Label(text=" ")
       box=BoxLayout(orientation='vertical')
       box.add_widget(lbl1)
       box.add_widget(self.txt1)
       box.add_widget(lbl2)
       box.add_widget(self.txt2)
       box.add_widget(zarb)
       box.add_widget(taghsim)
       box.add_widget(jam)
       box.add_widget(menha)
       box.add_widget(mosavi)
       box.add_widget(self.lbl3)
       return box

Myapp().run()