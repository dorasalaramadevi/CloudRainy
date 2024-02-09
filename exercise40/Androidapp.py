from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
 
 
class PopupApp(App):
def build(self):
button = Button(text='Click me to say hi to Gayathri!')
button.bind(on_press=self.show_popup)
return button
 
def show_popup(self, instance):
popup_content = Label(text='Hi Gayathri!')
popup = Popup(title='Greetings', content=popup_content, size_hint=(None, None), size=(400, 200))
popup.open()
 
 
if __name__ == '__main__':
PopupApp().run()
