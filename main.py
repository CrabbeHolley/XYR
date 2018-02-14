import sys;
import pymysql;
from XYR import Ui_MainWindow;
from jubao import Ui_Dialog as Ui_Jubao;
from suspect import Ui_Dialog as Ui_Suspect;
from map import Ui_Form as Ui_Map;
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
    def suspect_in(self):
        self.addSuspect = suspectWidget()
        self.addSuspect.show()
    def map_find(self):
        self.findMap = mapWidget()
        self.findMap.show()
    def combobox_change(self):
        global selected
        selected = names[self.comboBox.currentIndex()][0]

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

class mapWidget(QtWidgets.QWidget,Ui_Map):
    def __init__(self):
        super(mapWidget,self).__init__()
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