
import kivy
from kivy.app import App
from kivymd.app import MDApp

from kivymd.uix.relativelayout import MDRelativeLayout

from kivy.uix.label import Label
#from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from PIL import Image
from pytesseract import pytesseract
from tkinter.filedialog import askopenfile

from kivy.core.window import Window

Window.size = (500,500)
##################################################################################################

class MyApp(MDApp):
    def filechooser(self,event):
        self.file=askopenfile(mode="r",filetypes=[("png files","*.png")])
        self.imgFile=self.file.name

        self.locationLabel.text=self.imgFile
        self.locationLabel.pos_hint={"center_x": 0.5, "center_y": 0.2}

        self.ExtractButton.disabled=False
        self.chooseButton.disabled=True

##################################################################################################
    def extractText(self,event):
        self.path_to_tessaract=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        path_to_img= self.imgFile

        #point tessarct cmd totesseract.exe
        pytesseract.tesseract_cmd=self.path_to_tessaract

        img=Image.open(path_to_img)

        #Extract text from img
        text=pytesseract.image_to_string(img)
        print(text)
        self.imgtext.text=text








##################################################################################################
    def build(self):

        # Create a layout to hold your widgets
        layout = MDRelativeLayout(md_bg_color= [150/255,170/255,30/255])
##################################################################################################### img
        self.imgtext = TextInput(text="",
                         size_hint=(None, None),
                         pos_hint={"center_x": 0.5, "center_y": 0.62},
                         height=340,width=480,
                         font_size=25,
                         foreground_color=(0,0.5,0))
        layout.add_widget(self.imgtext)
##################################################################################################### button
        self.chooseButton = Button(text="Select Img",
                                 size_hint=(0.2, 0.1),
                                 pos_hint={"center_x": 0.4, "center_y": 0.07},
                                 disabled=False,
                                 font_size=24,
                                 background_color=(0, 1, 0),
                                 on_press=self.filechooser)
        layout.add_widget(self.chooseButton)
##################################################################################################### button
        self.ExtractButton = Button(text="Extract text",
                                   size_hint=(0.2, 0.1),
                                   pos_hint={"center_x": 0.65, "center_y": 0.07},
                                   disabled=True,
                                   font_size=24,
                                   background_color=(0, 1, 0),
                                   on_press=self.extractText)
        layout.add_widget(self.ExtractButton)
##################################################################################################### location label
        self.locationLabel = Label(text="",
                                    size_hint=(1,1),
                                    pos_hint={"center_x": 0.5, "center_y": 20},
                                    font_size=20,
                                    color=(0, 0, 1))
        layout.add_widget(self.locationLabel)

        return layout


# layouts
if __name__ == "__main__":
    MyApp().run()




