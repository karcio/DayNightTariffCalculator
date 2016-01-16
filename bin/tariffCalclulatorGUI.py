'''
Created on Jan 13, 2016
simple day/night tariff calculator
@author: karcio
'''
import sys

from PyQt4 import QtGui

import design


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate) 

    
    def calculate(self):
        dayTariffCost = self.lineEdit.text()
        D_TARIFF_COST = float(dayTariffCost)
        
        nightTariffCost = self.lineEdit_2.text()
        N_TARIFF_COST = float(nightTariffCost)
        
        counterReading = self.lineEdit_3.text()
        cr = float(counterReading)
        
        day = cr * 0.625 * D_TARIFF_COST
        night = cr * 0.375 * N_TARIFF_COST
        
        calculation = day + night 
        
        self.label_6.setText("%.2f" % float(calculation * 30))
        self.label_7.setText("%.2f" % float(calculation * 360))
       
               
def main():
    app = QtGui.QApplication(sys.argv)  
    form = ExampleApp()                 
    form.show()                         
    app.exec_()                        

if __name__ == '__main__':              
    main()