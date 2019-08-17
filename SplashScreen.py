from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSplashScreen

class SplashScreen(QtWidgets.QSplashScreen):
    """Class to define a splash screen to show loading progress"""
    def __init__(self):
        QtWidgets.QSplashScreen.__init__(
            self,QtGui.QPixmap("icons/eye.ico"))
        QtWidgets.QApplication.flush()
        #QtGui.QPixmap(os.environ["images"] + "/images/splash.jpg"))
    def showMessage(self, msg):
        """Procedure to update message in splash"""
        align = QtCore.Qt.Alignment(QtCore.Qt.AlignBottom |
                                    QtCore.Qt.AlignRight |
                                    QtCore.Qt.AlignAbsolute)
        color = QtGui.QColor(QtCore.Qt.white)
        QtWidgets.QSplashScreen.showMessage(self, msg, align, color)
        QtWidgets.QApplication.processEvents()
 
    def clearMessage(self):
        QtWidgets.QSplashScreen.clearMessage(self)
        QtWidgets.QApplication.processEvents()
