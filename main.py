import sys;
import pymysql;
import random;
import threading;
import tornado.web;
from XYR import Ui_MainWindow;
from jubao import Ui_Dialog as Ui_Jubao;
from suspect import Ui_Dialog as Ui_Suspect;
from map import Ui_Form as Ui_Map;
from guiji import Ui_Form as Ui_Guiji;
from selected import Ui_Form as Ui_Select;
from PyQt5 import QtWidgets,QtCore;
from tornado.options import define, options;

define("port", default=8000, help="run on the given port", type=int)

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
    def action_in(self):
        self.addSuspectAction = jubaoWidget()
        self.addSuspectAction.show()
    def suspect_in(self):
        self.addSuspect = suspectWidget()
        self.addSuspect.show()
    def map_find(self):
        self.findMap = mapWidget()
        self.findMap.show()
    def guiji_find(self):
        self.findGuiji = guijiWidget()
        self.findGuiji.show()
    def suspect_select(self):
        self.suspectSelect = selectWidget()
        self.suspectSelect.show()
    def find_action(self):
        global index
        db_find = pymysql.connect("localhost", "root", "crab1996", "suspect", 0, None, "utf8")
        cursor = db_find.cursor()
        selected = names[index]
        sql = "select * from evidence where PID='%s'" % (selected[0])
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        rows = cursor.fetchall()
        count = cursor.rowcount
        self.table.setRowCount(count)
        self.table.setColumnCount(2)
        self.table.setColumnWidth(1, 630)
        self.table.setHorizontalHeaderLabels(['姓名', '笔录'])
        now = 0
        for row in rows:
            newItem = QtWidgets.QTableWidgetItem(row[2])
            self.table.setItem(now, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem(row[3])
            self.table.setItem(now, 1, newItem)
            now = now+1
        self.table.resizeRowsToContents()

class selectWidget(QtWidgets.QWidget,Ui_Select):
    def __init__(self):
        super(selectWidget,self).__init__()
        self.setupUi(self)
    def search_suspect(self):
        db_search = pymysql.connect("localhost", "root", "crab1996", "suspect", 0, None, "utf8")
        cursor = db_search.cursor()
        searchName = self.lineEdit.text()
        sql = "select * from people WHERE name='%s'" % searchName;
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        rows = cursor.fetchall()
        count = cursor.rowcount
        self.tableWidget.setRowCount(count)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['身份证号码','姓名','性别','现住址','户籍所在地'])
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 170)
        now = 0;
        for row in rows:
            newItem = QtWidgets.QTableWidgetItem(row[0])
            self.tableWidget.setItem(now, 0 ,newItem)
            newItem = QtWidgets.QTableWidgetItem(row[1])
            self.tableWidget.setItem(now, 1, newItem)
            newItem = QtWidgets.QTableWidgetItem(row[2])
            self.tableWidget.setItem(now, 2, newItem)
            newItem = QtWidgets.QTableWidgetItem(row[3])
            self.tableWidget.setItem(now, 3, newItem)
            newItem = QtWidgets.QTableWidgetItem(row[4])
            self.tableWidget.setItem(now, 4, newItem)
            now = now+1
        self.tableWidget.resizeRowsToContents()
        db_search.close()
    def sure(self):
        sel = self.tableWidget.currentRow()
        if sel==-1:
            self.close()
            return
        peopleId = self.tableWidget.item(sel,0)
        hasSuspect = False
        global index,names
        now = 0
        for name in names:
            if name[5]==peopleId.text():
                hasSuspect = True
                index = now
                window.suspectButton.setText(name[1])
            now = now+1
        if hasSuspect==False:
            QtWidgets.QMessageBox.warning(self, "提示", "选定人没有犯案记录！")
            return
        self.close()



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
        if Rname=="":
            QtWidgets.QMessageBox.warning(self,"提示","请填入举报人姓名或选择匿名举报")
            return
        if self.content.toPlainText()=="":
            QtWidgets.QMessageBox.warning(self, "提示", "请填入举报行为")
            return
        sql = "insert into evidence(Sname,Rname,Record,PID) values('%s','%s','%s','%s')" % (names[jubaoIndex][1],Rname,self.content.toPlainText(),names[jubaoIndex][0])
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        db_jubao.commit()
        db_jubao.close()
        QtWidgets.QMessageBox.information(self,"成功","信息录入成功",QtWidgets.QMessageBox.Yes)
        self.close()

class suspectWidget(QtWidgets.QDialog,Ui_Suspect):
    def __init__(self):
        super(suspectWidget,self).__init__()
        self.setupUi(self)
        now = QtCore.QDate.currentDate()
        self.dateEdit.setDate(now)
        self.dateEdit.setMaximumDate(now)
    def back(self):
        self.close()
    def sure(self):
        db_suspect = pymysql.connect("localhost", "root", "crab1996", "suspect", 0, None, "utf8")
        cursor = db_suspect.cursor()
        Sname = self.name.text()
        id = self.idEdit.text()
        date = self.dateEdit.text()
        PID = self.PIDEdit.text()
        if Sname=="" or id=="" or PID=="":
            QtWidgets.QMessageBox.warning(self,"提示","请填写全部信息")
            return
        sql = "select * from people where PeopleID='%s' and name='%s'" % (PID,Sname)
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        if cursor.rowcount<=0:
            QtWidgets.QMessageBox.warning(self, "提示", "请输入正确的身份证号")
            return
        sql = "insert into suspect_position(PID,name,outTime,PeopleID) values('%s','%s','%s','%s')" % (id,Sname,date,PID)
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        QtWidgets.QMessageBox.information(self, "成功", "信息录入成功", QtWidgets.QMessageBox.Yes)
        db_suspect.commit()
        db_suspect.close()
        self.close()
    def closeEvent(self, QCloseEvent):
        global names
        db_close = pymysql.connect("localhost", "root", "crab1996", "suspect", 0, None, "utf8")
        cursor = db_close.cursor()
        cursor.execute("select * from suspect_position")
        names = cursor.fetchall()

class mapWidget(QtWidgets.QWidget,Ui_Map):
    def __init__(self):
        super(mapWidget,self).__init__()
        self.setupUi(self)
        global longitude,latitude,index,guiji
        guiji = False
        suspectNow = names[index]
        longitude = suspectNow[2]
        latitude = suspectNow[3]
        if index==0:
            longitude = 116.5101
            latitude = 39.6915 #青云里小区
        elif index==1:
            longitude = 117.7414
            latitude = 38.9968 #天津港客运站
        self.label_2.setText(str(longitude))
        self.label_4.setText(str(latitude))
    def back(self):
        self.close()

class guijiWidget(QtWidgets.QWidget,Ui_Guiji):
    def __init__(self):
        super(guijiWidget,self).__init__()
        self.setupUi(self)
        global longitude,latitude,index,guiji,startLong,startLa
        guiji = True
        suspectNow = names[index]
        longitude = suspectNow[2]
        latitude = suspectNow[3]
        startLong = longitude + random.uniform(-1.5, 1.5)
        startLa = latitude + random.uniform(-1, 1)
        guijiInformation = ""
        if index==0:
            startLong = 116.3851
            startLa = 39.8709 #北京南站
            longitude = 116.5101
            latitude = 39.6915 #青云里小区
            guijiInformation = "嫌疑人从北京南站，最后到达了青云里小区"
        elif index==1:
            startLong = 117.0688
            startLa = 39.0627 #天津南站
            longitude = 117.7414
            latitude = 38.9968 #天津港客运站
            guijiInformation = "嫌疑人从天津南站，最后到达了天津港客运站"
        self.information.setPlainText(guijiInformation)
    def back(self):
        self.close()

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        global longitude,latitude,guiji,startLa,startLong
        self.render('map.html', noun1=longitude, noun2=latitude, noun3=startLong, noun4=startLa, noun5=guiji)

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
    guiji = False
    threadTronado = myThread(1, "threadTornado")
    threadTronado.start()
    db = pymysql.connect("localhost", "root", "crab1996", "suspect", 0, None, "utf8")
    cursor = db.cursor()
    cursor.execute("select * from suspect_position")
    names = cursor.fetchall()
    for s in names:
        long = random.uniform(113,122)
        la = random.uniform(22,40)
        sql = "update suspect_position set longitude='%f',latitude='%f' where PID='%s'" % (long,la,s[0])
        cursor.execute(sql)
    db.commit()
    cursor.execute("select * from suspect_position")
    names = cursor.fetchall()
    db.commit()
    db.close()

    index = 0 #XYR界面选中的嫌疑人
    longitude = 0.0
    latitude = 0.0
    startLong = 0.0
    startLa = 0.0
    jubaoIndex = 0 #举报界面选中的嫌疑人
    guijiInformation = ""

    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())