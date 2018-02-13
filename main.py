import sys;
import pymysql;
from XYR import Ui_MainWindow;
from jubao import Ui_Dialog as Ui_Jubao;
from suspect import Ui_Dialog as Ui_Suspect;
from PyQt5 import QtWidgets,QtCore;

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        for row in names:
            self.comboBox.addItem(row[1])
    def action_in(self):
        self.addSuspectAction = jubaoWidget()
        self.addSuspectAction.show()
        print(selected)
    def suspect_in(self):
        self.addSuspect = suspectWidget()
        self.addSuspect.show()

class jubaoWidget(QtWidgets.QDialog,Ui_Jubao):
    def __init__(self):
        super(jubaoWidget,self).__init__()
        self.setupUi(self)
    def back(self):
        self.close()

class suspectWidget(QtWidgets.QDialog,Ui_Suspect):
    def __init__(self):
        super(suspectWidget,self).__init__()
        self.setupUi(self)
    def back(self):
        self.close()


db = pymysql.connect("localhost","root","crab1996","suspect",0,None,"utf8")
cursor = db.cursor()
cursor.execute("select * from suspect_position")
names = cursor.fetchall()

selected = "0001"
app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
db.close()
sys.exit(app.exec_())