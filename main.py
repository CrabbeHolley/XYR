import sys;
import pymysql;
import threading;
import tornado.web;
from XYR import Ui_MainWindow;
from jubao import Ui_Dialog as Ui_Jubao;
from suspect import Ui_Dialog as Ui_Suspect;
from map import Ui_Form as Ui_Map;
from PyQt5 import QtWidgets,QtCore,QtGui;
from tornado.options import define, options;

define("port", default=8000, help="run on the given port", type=int)

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
        global index
        index = self.comboBox.currentIndex()

class jubaoWidget(QtWidgets.QDialog,Ui_Jubao):
    def __init__(self):
        super(jubaoWidget,self).__init__()
        self.setupUi(self)
        for row in names:
            self.suspect.addItem(row[1])
        global index,jubaoIndex
        self.suspect.setCurrentIndex(index)
        jubaoIndex = index
    def back(self):
        self.close()
    def anonymous(self):
        if self.radioButton.isChecked():
            self.Rname.clear()
            self.Rname.setEnabled(False)
        else:
            self.Rname.setEnabled(True)
    def changeSuspect(self):
        global jubaoIndex
        jubaoIndex = self.suspect.currentIndex()
    def addEvidence(self):
        db_jubao = pymysql.connect("localhost", "root", "crab1996", "suspect", 0, None, "utf8")
        cursor = db_jubao.cursor()
        Rname = self.Rname.text()
        if self.radioButton.isChecked():
            Rname = "匿名"
        sql = "insert into evidence(Sname,Rname,Record,PID) values('%s','%s','%s','%s')" % (names[jubaoIndex][1],Rname,self.content.toPlainText(),names[jubaoIndex][0])
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        db_jubao.commit()
        db_jubao.close()
        reply = QtWidgets.QMessageBox.information(self,"成功","信息录入成功",QtWidgets.QMessageBox.Yes)
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
        global longitude,latitude,index
        suspectNow = names[index]
        longitude = suspectNow[2]
        latitude = suspectNow[3]
        self.label_2.setText(str(suspectNow[2]))
        self.label_4.setText(str(suspectNow[3]))
    def back(self):
        self.close()

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        global longitude,latitude
        self.render('map.html', noun1=longitude, noun2=latitude)

class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        tornado.options.parse_command_line()
        app = tornado.web.Application(
            handlers=[(r'/', IndexHandler), (r'/map', PoemPageHandler)]
        )
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    threadTronado = myThread(1, "threadTornado")
    threadTronado.start()
    db = pymysql.connect("localhost", "root", "crab1996", "suspect", 0, None, "utf8")
    cursor = db.cursor()
    cursor.execute("select * from suspect_position")
    names = cursor.fetchall()
    db.commit()
    db.close()

    index = 0 #XYR界面选中的嫌疑人
    longitude = 0.0
    latitude = 0.0
    jubaoIndex = 0 #举报界面选中的嫌疑人

    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())