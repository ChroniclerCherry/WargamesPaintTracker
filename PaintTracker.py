from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import csv
from kivy.properties import ListProperty
from kivy.properties import NumericProperty


class ColoursBox(BoxLayout):
    colour = ListProperty([0,0,0])
    index = NumericProperty()

    def __init__(self,index_id,name,company,colour,owned):
        BoxLayout.__init__(self)
        self.index = index_id
        self.ids.name.text = name
        self.ids.company.text = company
        self.colour = self.hex_to_rgb(colour)

        if owned == 'Y':
            self.ids.owned.state ='down'
        elif owned == 'N':
            self.ids.unowned.state ='down'



    def hex_to_rgb(self,value):
        value = value.lstrip('#')
        lv = len(value)
        return list(int(value[i:i + lv // 3], 16)/255 for i in range(0, lv, lv // 3))


class PaintTrackerApp(App):

    data = ListProperty(None)

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

    def save_data(self):
        with open('PaintList.csv','w') as csvfile:
                writer = csv.writer(csvfile)

                writer.writerow(["Company", "Paint Name", "HEX Code", "Owned"])

                for row in self.data:
                    writer.writerow(row)

    def build(self):
        root = self.root

        self.load_data()

        for c in range(len(self.data)):
            root.ids.grid.add_widget(ColoursBox(c,
                                                self.data[c][0],
                                                self.data[c][1],
                                                self.data[c][2],
                                                self.data[c][3]))

    def update_ownership(self, owned_state,index,instance):

        if owned_state == self.data[index][3]:
            instance.state = 'down'
        else:
            self.data[index][3] = owned_state



if __name__ == '__main__':
    PaintTrackerApp().run()
