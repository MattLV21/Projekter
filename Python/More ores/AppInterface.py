from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

from AutoMation import *
import threading


class MainWidget(GridLayout):
    combo_state = StringProperty("Not active")
    adventure_state = StringProperty("Not active")
    w = StringProperty(str(win32gui.GetWindowText(window)))

    def Combo_Click(self):
        x = threading.Thread(target=ComboAutoClick())
        x.start()
        
    def Adventure_Click(self):
        x = threading.Thread(target=AdventureAutoClick())
        x.start()

class MoreOresApp(App):
    pass

if __name__ == "__main__":
    MoreOresApp().run()