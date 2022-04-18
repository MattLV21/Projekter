from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty

class WidgetsExamble(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty(str(count))
    text_input_str = StringProperty("foot")
    # slider_value_txt = StringProperty(str(50))

    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
        self.my_text = f"{self.count}"

    def on_toggle_button_state(self, widget):
        print(widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True
    
    def on_switch_active(self, widget):
        print("switch", str(widget.active))
    
    #def on_slider_value(self, widget):
    #    print("Slider:", str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))
    
    def on_text_validate(self, widget):
        self.text_input_str = widget.text

        

class StackLayoutExamble(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 100):
            #size = dp(100) + i * 10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

#class GridLayoutExamble(GridLayout):
#    pass

class AnchorLayoutExamble(AnchorLayout):
    pass

class BoxLayoutExamble(BoxLayout):
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()