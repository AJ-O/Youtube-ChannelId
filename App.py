import sys
import urllib.request

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from functools import partial
from getChannels import extractData

#This file is to create a widget to show subscriber count, channel title and image of the channel
#so that the user selects the channel they wanted and get that channels' Id
class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.title = 'Youtube ChannelId'
        self.left = 450
        self.top = 80
        self.width = 350
        self.height = 300
        self.initUI()
    
    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #getting all the data returned by the extractData function of the getChannels file
        data = extractData()
        imgSrcList = data['imgSrc']
        subCountList = data['subscriberCount']
        channelTitleList = data['channelTitles']
        channelIdList = data['channelIdList']
        times = len(data['subscriberCount'])

        for i in range(times):
            
            #open the url contained in the imageSrcList and get the image

            data = urllib.request.urlopen(imgSrcList[i]).read()
            image = QImage()
            image.loadFromData(data)

            imageLabel = QLabel(self)#image needs to be embedded in a label
            imageLabel.resize(90, 90)#set the size of the label
            pixmap = QPixmap(image)
            pixmap_changed = pixmap.scaled(90, 90)#scale the image received from the imgage source to 90 * 90
            imageLabel.setPixmap(pixmap_changed)#Embed the image in the label
            imageLabel.move(10, (i * 100))

            title = QLabel(channelTitleList[i], self)
            title.move(125, (10 + (i * 100)))

            sub = QLabel(subCountList[i], self)
            sub.move(125, (30 + (i *100)))

            button = QPushButton('THIS ONE', self)
            button.move(220, (20 + (i * 110)))
            button.clicked.connect(partial(self.on_click, channelIdList[i]))#partial to pass the channelId as argument when button is clicked

        self.show()
    
    def on_click(self, id):

        print("Here's your selected channels id: ", id)
        print("Ok Bye!")
        QCoreApplication.instance().quit()#Quit once the id is selected by the user

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())