from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

kv = '''
MDFloatLayout:
    md_bg_color: 0.73,0.75,0.72,1
    MDIconButton:
        pos_hint: {'left':1,'top': 1}
        icon: 'arrow-left-bold-circle-outline'
        icon_color: 1,0,0,1
    MDLabel:
        padding_x: dp(10)
        text: 'Suma y resta'
        color: 'purple'
        font_size: sp(30)
        pos_hint: {'center_y': 0.92}#0.87
    MDLabel:
        id: sumamatriz
        padding_x: dp(10)
        text: "Para la suma y la resta se debe cumplir que tengan el mismo tamaño. Es decir, la misma cantidad de filas y columnas. Y se suma o resta directamente con el elemento que esté en la misma posición, así:"
        halign: 'left'
        pos_hint: {'center_y':0.83}
    Image:
        source: 'sumamatriz.png'
        pos_hint: {'center_y':0.6}
'''

#Window.size = (720,1465)
class main(MDApp):
    def build(self):
        return Builder.load_string(kv)
    #def on_start(self):
        an,al = Window.size
        y = float((an*al*0.77)/(750000))
        pos = {'center_y':y}
        self.root.ids.sumamatriz.pos_hint = pos
        for nombre,tipo in self.root.ids.items():
            print(f'{nombre} y {tipo}')

main().run()
