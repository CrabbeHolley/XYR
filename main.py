import sys;
from XYR import Ui_MainWindow;
from jubao import Ui_Dialog;
from PyQt5 import QtWidgets,QtCore;

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
    def action_in(self):
        self.addSuspectAction = jubaoWidget()
        self.addSuspectAction.show()

class jubaoWidget(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(jubaoWidget,self).__init__()
        self.setupUi(self)
    def back(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())