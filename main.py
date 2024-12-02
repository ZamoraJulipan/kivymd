from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

KV = '''
FloatLayout:
    MDLabel:
        id: t
        text: "El tamaño es: "
        font_style: "H2"
    MDFlatButton:
        text: 'Revisar'
        font_style: "H4"
        on_press: app.medir()
'''

class main(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def medir(self):
        self.root.ids.t.text = str(Window.size)

main().run()
