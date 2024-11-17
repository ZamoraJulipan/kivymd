from kivymd.app import MDApp
from kivy.lang import Builder

class main(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

main().run()