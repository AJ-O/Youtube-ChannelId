import sys
import urllib.request

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from functools import partial
from getChannels import extractData


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 450
        self.top = 80
        self.width = 350
        self.height = 300
        self.initUI()
    
    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        data = extractData()
        imgSrcList = data['imgSrc']
        subCountList = data['subscriberCount']
        channelTitleList = data['channelTitles']
        channelIdList = data['channelIdList']


        for i in range(3):

            data = urllib.request.urlopen(imgSrcList[i]).read()
            image = QImage()
            image.loadFromData(data)

            imageLabel = QLabel(self)
            imageLabel.resize(90, 90)
            pixmap = QPixmap(image)
            pixmap_changed = pixmap.scaled(90, 90)
            imageLabel.setPixmap(pixmap_changed)
            imageLabel.move(10, (i * 100))

            title = QLabel(channelTitleList[i], self)
            title.move(125, (10 + (i * 100)))

            sub = QLabel(subCountList[i], self)
            sub.move(125, (30 + (i *100)))

            button = QPushButton('THIS ONE', self)
            button.move(220, (20 + (i * 100)))
            button.clicked.connect(partial(self.on_click, channelIdList[i]))

        self.show()
    
    def on_click(self, id):

        print("Here's your selected channels id: ", id)
        print("Ok Bye!")
        QCoreApplication.instance().quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())