import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenu

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

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
    def exit(self):
        QtCore.QCoreApplication.exit()
        
    def cmd1(self):
        print("command 1")

def main(image):
    app = QtWidgets.QApplication(sys.argv)
    #movie = QMovie("alia.gif")
    w = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon(image), w)

    trayIcon.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    on=r'icons/eye.ico'# ADD PATH OF YOUR ICON HERE .png works
    main(on)
