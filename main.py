from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class JarvisApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.label = Label(text="Jarvis System Offline", font_size=26)
        btn = Button(text="Turn On Jarvis", size_hint=(1, 0.3), font_size=20)
        btn.bind(on_press=self.start_jarvis)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def start_jarvis(self, instance):
        self.label.text = "Jarvis Online & Ready!"

if __name__ == '__main__':
    JarvisApp().run()
