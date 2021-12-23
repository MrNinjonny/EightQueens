from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class board(GridLayout):
    def __init__(self):
        # 0 represent unknown
        GridLayout.__init__(self)
        self.problem = [-1]*8
        self.cols = 8
        self.all = list()
        self.button = Button(text='Next solution')
        self.button.bind(on_press=self.click)
        self.bruteForce(0)
        self.add_board()
        self.add_widget(self.button)
    ''' Returns the first cell that is unknown'''

    def possiblePlacing(self, index):
        if self.problem.count(self.problem[index]) > 1:
            return False
        for i in range(len(self.problem)):
            if index - self.problem[index] == i - self.problem[i] and self.problem[i] != -1 and i != index:
                return False
            if index + self.problem[index] == i + self.problem[i] and self.problem[i] != -1 and i != index:
                return False
        return True

    def bruteForce(self, index):
        if index == 8:
            if self.problem not in self.all:
                self.all.append(self.problem)
                self.problem = [-1]*8
                return True
            else:
                return False
        for i in range(len(self.problem)):
            self.problem[index] = i
            if self.possiblePlacing(index):
                if self.bruteForce(index+1):
                    return True
        self.problem[index] = -1
        return False

    def add_board(self):
        for j in range(len(self.problem)):
            for i in range (len(self.problem)):
                if i == self.all[len(self.all)-1][j]:
                    self.add_widget(Image(source = 'pics/queen.jpg'))
                else:
                    self.add_widget(Image(source = 'pics/blenk.jpg'))

    def click(self,touch):
        self.bruteForce(0)
        self.clear_widgets()
        self.add_board()
        self.add_widget(self.button)

class TestApp(App):
    def build(self):
        self.title = '8 Queens'
        return board()
TestApp().run()
