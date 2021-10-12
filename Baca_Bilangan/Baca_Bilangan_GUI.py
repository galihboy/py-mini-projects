# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_bacaBilangan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

'''
Github: https://github.com/galihboy/
Web: http://galih.eu
'''


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 164)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label.setObjectName("label")
        self.txtAngka = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAngka.setGeometry(QtCore.QRect(100, 10, 171, 20))
        self.txtAngka.setObjectName("txtAngka")
        self.tombolBaca = QtWidgets.QPushButton(self.centralwidget)
        self.tombolBaca.setGeometry(QtCore.QRect(280, 9, 75, 23))
        self.tombolBaca.setObjectName("tombolBaca")
        self.txtOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtOutput.setGeometry(QtCore.QRect(11, 40, 341, 81))
        self.txtOutput.setObjectName("txtOutput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # aktifasi proses baca angka masukan
        self.tombolBaca.clicked.connect(self.BacaBilangan)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Galih Hermawan - Baca Bilangan"))
        self.label.setText(_translate("MainWindow", "Masukkan angka"))
        self.tombolBaca.setText(_translate("MainWindow", "Baca"))
        self.txtAngka.setPlaceholderText(_translate("MainWindow", "bilangan bulat"))
        self.txtOutput.setPlaceholderText(_translate("MainWindow", "... hasil baca..."))
        #self.txtOutput.setEnabled(False)
        self.txtOutput.setReadOnly(True)
        
    # kotak dialog kustom
    def Pesan(self, ikon, judul, teks):
        kotakPesan = QtWidgets.QMessageBox(ikon, judul, teks)
        kotakPesan.exec()
     
    def BacaBilangan(self):
        angka = self.txtAngka.text()
        boolValid = CekAngka(angka)
        
        if boolValid:
            hasil = BacaAngka(angka)
            hasil = FixBugsNol(hasil)
            self.txtOutput.setPlainText(hasil)
        else:
            self.Pesan(QtWidgets.QMessageBox.Warning, "Kesalahan!", "Angka masukan harus berupa bilangan bulat.")
     
if __name__ == "__main__":
    import sys
    from libBacaBilangan import BacaAngka, FixBugsNol, CekAngka
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
