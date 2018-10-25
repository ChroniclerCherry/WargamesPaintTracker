from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import csv
from kivy.properties import ReferenceListProperty


class ColoursBox(BoxLayout):
    def __init__(self,name,company,colour,owned):
        BoxLayout.__init__(self)
        self.ids.name.text = name
        self.ids.company.text = company

        self.colour = ReferenceListProperty(self.hex_to_rgb(colour))


    def hex_to_rgb(self,value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


class PaintTrackerApp(App):

    def load_data(self):
        self.data = []

        with open('PaintList.csv','r') as csvfile:
                reader = csv.reader(csvfile)

                first_line = True

                for row in reader:
                    if first_line:
                        first_line = False
                    else:
                        self.data.append(row)


    def build(self):
        root = self.root

        self.load_data()

        data = self.data

        for c in range(len(data)):
            root.ids.grid.add_widget(ColoursBox(data[c][0],  data[c][1],data[c][2], data[c][3]))


if __name__ == '__main__':
    PaintTrackerApp().run()
