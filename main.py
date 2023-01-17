from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_string("""
<ColorWidget>:
    BoxLayout:
        size: (360,800)
        orientation: 'vertical'

        Label:
            id: lbl
            text: 'Цвет'
            font_size: 20

        TextInput:
            id: tb
            font_size: 20
            padding_y: 30
            halign: 'center'
        
        Button:
            text: '#ff0000'
            font_size: 20
            background_normal: ''
            background_color: (1,0,0,1)
            on_press:
                lbl.text = 'Красный'
                tb.text = '#ff0000'
            
        Button:
            text: '#ff8800'
            font_size: 20
            background_normal: ''
            background_color: (1,0.53,0,1)
            on_press:
                lbl.text = 'Оранжевый'
                tb.text = '#ff8800'
        
        Button:
            text: '#ffff00'
            font_size: 20
            background_normal: ''
            background_color: (1,1,0,1)
            on_press:
                lbl.text = 'Желтый'
                tb.text = '#ffff00'
        
        Button:
            text: '#00ff00'
            font_size: 20
            background_normal: ''
            background_color: (0,1,0,1)
            on_press:
                lbl.text = 'Зелёный'
                tb.text = '#00ff00'
        
        Button:
            text: '#00ffff'
            font_size: 20
            background_normal: ''
            background_color: (0,1,1,1)
            on_press:
                lbl.text = 'Голубой'
                tb.text = '#00ffff'
        
        Button:
            text: '#0000ff'
            font_size: 20
            background_normal: ''
            background_color: (0,0,1,1)
            on_press:
                lbl.text = 'Синий'
                tb.text = '#0000ff'
        
        Button:
            text: '#ff00ff'
            font_size: 20
            background_normal: ''
            background_color: (1,0,1,1)
            on_press:
                lbl.text = 'Фиолетовый'
                tb.text = '#ff00ff'
""")
class ColorWidget(BoxLayout):
    pass

class myApp(App):
    def build(self):
        Window.size = (360, 800)
        return ColorWidget()
        
if __name__=="__main__":
    myApp().run()
