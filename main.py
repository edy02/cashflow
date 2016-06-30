import sys
from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from window import Ui_MainWindow
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
import csv
import time

CZ_TIME = int(time.time()+60*60*2)
UTC_TIME = 0
DATE = 1
TIME = 2
THING = 3
BILL = 4
CASH = 5


class Mysql:
    def __init__(self):
        
        self.engine = create_engine('mysql://root:4842130@localhost:3306/cashflow')
        self.conn = self.engine.connect()
        self.meta = MetaData()
        
        # Table templates
        self.cashflow = Table('cashflow', self.meta,
                         Column('id', Integer, primary_key = True),
                         Column('utc_time', Integer),
                         Column('date', String(15)),
                         Column('time', String(15)),
                         Column('thing', String(100)),
                         Column('bill', Integer),
                         Column('cash', Integer)
                         )
        
#         self.drop_tables()
        self.meta.create_all(self.engine)
            
    def populate(self, data):
        for move in data:
#             print data
            ins = self.cashflow.insert().values(utc_time = move[UTC_TIME],
                                                date = move[DATE],
                                                time= move[TIME],
                                                thing = move[THING],
                                                bill = move[BILL],
                                                cash = move[CASH]
                                                )
            result = self.conn.execute(ins)
            print result
            
    def drop_tables(self):
        self.meta.drop_all(self.engine)

class Main(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.connect(self.ui.btnZapis, SIGNAL("clicked()"), self.btnZapis_Clicked)
        self.connect(self.ui.btnSmazat, SIGNAL("clicked()"), self.btnSmazat_Clicked)
        self.connect(self.ui.btnPrepocitat, SIGNAL("clicked()"), self.btnPrepocitat_Clicked)
        #self.connect(self.ui.tblVypis, SIGNAL(""), self.tableWidget_Pressed)
        
        # Define classes of widgets
        self.mysql = Mysql()
        self.vypis = Vypis(self.ui.tblVypis)        
        self.matplot = MatPlot(self.ui.matplot)
        
        # Do start functions
        self.starting()
        
    def starting(self):
        # Write out data to table widget
        self.vypis.writeOutData()
        
        # Plot the cashflow
        x = self.vypis.get_allCash()
        self.matplot.plot(x)
        
        # Populate database
#         data = self.vypis.get_csvData()
#         self.mysql.populate(data)
           
        
    def reload(func):
        def magic(self):
            func(self)
            self.matplotCashflow2()
        return magic
            
    #@reload
    def btnSmazat_Clicked(self):
        row = self.ui.tblVypis.currentRow()
        self.ui.tblVypis.removeRow(row)
        # is needed to recount all items
        self.vypis.recount()
       
    def btnPrepocitat_Clicked(self):
        self.vypis.recount()
    
    def countCsvFile(self):
        with open('cashflow.csv', 'r') as f:
            rowCount = 0
            for lastrow in csv.reader(f):
                rowCount += 1
            return rowCount
        
    def get_lastRow(self):
        with open('cashflow.csv', 'r') as f:
            lastrow = None
            self.rowCount = 0
            for lastrow in csv.reader(f):
                self.rowCount += 1
                pass
            return lastrow
             
    def btnZapis_Clicked(self):
        with open('cashflow.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';', lineterminator='\n')
            
            date = time.strftime("%d:%m",time.gmtime(CZ_TIME))
            hour = time.strftime("%H:%M",time.gmtime(CZ_TIME))
            # current money
            money = int(self.get_lastRow()[0].split(";")[-2])
            predmet = self.ui.txtPredmet.text()
            pohyb = int(self.ui.spinBoxPohyb.text())
            writer.writerow([CZ_TIME, date, hour, predmet, pohyb, money + pohyb, None])
        self.vypis.writeOutData()


class Vypis:
    def __init__(self, tblVypis):
        self.tblVypis = tblVypis
        
    def countCsvFile(self):
        with open('cashflow.csv', 'r') as f:
            rowCount = 0
            for lastrow in csv.reader(f):
                rowCount += 1
            return rowCount
        
    def writeOutData(self):
        # write csv to table
        csvRows = self.countCsvFile()
        #if not empty, remove all
        self.tblVypis.setRowCount(0)
        self.tblVypis.setRowCount(csvRows)
        with open('cashflow.csv' ,'r') as f:
            reader = csv.reader(f, delimiter = ';')
            rowCount = -1
            for row in reader:
                rowCount += 1
                for columnCount in xrange(self.tblVypis.columnCount()):
                    self.tblVypis.setItem(rowCount,columnCount, QtGui.QTableWidgetItem(row[columnCount+1]))
    
    def get_csvData(self):
        data = []
        with open('cashflow.csv' ,'r') as f:
            reader = csv.reader(f, delimiter = ';')
            for row in reader:
                utc_time = row[UTC_TIME]
                date = row[DATE]
                time = row[TIME]
                thing = row[THING]
                bill = row[BILL]
                cash = row[CASH]
                data.append([utc_time, date, time, thing, bill, cash])
#                 print data
        return data
                
    def recount(self):
        for row in xrange(self.tblVypis.rowCount()):
            if row == 0:
                continue
            last_money = int(self.tblVypis.item(row-1, CASH).text())
            current_bill = int(self.tblVypis.item(row, BILL).text())
            current_money = last_money + current_bill
            self.tblVypis.setItem(row, CASH, QtGui.QTableWidgetItem(str(current_money)))
        
    def get_allCash(self):
        cash = []
        for row in xrange(self.tblVypis.rowCount()):
            cash.append(float(self.tblVypis.item(row, 4).text()))
        return cash
    
#     def get_all(self):
#         all = []
#         for row in xrange(self.tblVypis.rowCount()):
#             utc_time = float(self.tblVypis.item(row, UTC_TIME).text())
#             date = self.tblVypis.item(row, DATE).text()
#             time = self.tblVypis.item(row, TIME).text()
#             bill = float(self.tblVypis.item(row, BILL).text())
#             cash = float(self.tblVypis.item(row, CASH).text())
#             all.append([utc_time,])
    
class MatPlot:
    def __init__(self, matplot):
        self.matplot = matplot

    def plot(self, x):
        self.matplot.axes.plot(x)
    
    def matplotCashflowClear(self):
        self.matplot.axes.cla()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
    
    