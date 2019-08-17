# import python module for your system 
import os
import sys
# defaul import PyQt5 
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
# import SplashScreen class - show a splash with text 
from SplashScreen import SplashScreen

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    '''
    this is the tray icon application 
    1. show a splash with text with Cmd-1
    2. exit with Exit 
    '''
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        #create the menu
        menu = QtWidgets.QMenu(parent)

        #create the exit function
        exitAction = menu.addAction("Exit")
        cmd1Action = menu.addAction("Cmd-1")
        self.setContextMenu(menu)
        #triggered exit 
        exitAction.triggered.connect(self.exit)
        #triggered exit 
        cmd1Action.triggered.connect(self.cmd1)
        
    def quit(self):
        QtCore.QCoreApplication.exit() 
    # create the exit application 
    def exit(self):
        QtCore.QCoreApplication.exit()
    # create a command 1 
    def cmd1(self):
        print("command 1")
        self.splash = SplashScreen()
        self.splash.showMessage("Test...")
        self.splash.show()
# start the application
def main(image):
    app = QtWidgets.QApplication(sys.argv)
    #movie = QMovie("alia.gif")
    w = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon(image), w)

    trayIcon.show()

    #app.processEvents()
    sys.exit(app.exec_())
if __name__ == '__main__':
    on=r'icons/eye.ico'# ADD PATH OF YOUR ICON HERE .png works
    main(on)
