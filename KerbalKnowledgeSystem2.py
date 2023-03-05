# Form implementation generated from reading ui file 'KerbalKnowledgeSystem.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QSize
import Inference
import DeltaVMap
import DeltaVGraph

def FillStartingPosition(ComboBox):
    nameList = DeltaVMap.GetNameList()

    for key in nameList.keys():
        ComboBox.addItem(nameList[key], key)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1471, 859)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RoundTrip = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.RoundTrip.setGeometry(QtCore.QRect(30, 450, 121, 23))
        self.RoundTrip.setObjectName("RoundTrip")
        self.Aerobreaking = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.Aerobreaking.setGeometry(QtCore.QRect(30, 470, 121, 23))
        self.Aerobreaking.setObjectName("Aerobreaking")
        self.PlaneChange = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.PlaneChange.setGeometry(QtCore.QRect(30, 490, 121, 23))
        self.PlaneChange.setObjectName("PlaneChange")
        self.DeltaVList = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.DeltaVList.setGeometry(QtCore.QRect(30, 90, 301, 311))
        self.DeltaVList.setWidgetResizable(True)
        self.DeltaVList.setObjectName("DeltaVList")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 299, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.DeltaVList.setWidget(self.scrollAreaWidgetContents)
        self.StartingLocation = QtWidgets.QComboBox(parent=self.centralwidget)
        self.StartingLocation.setGeometry(QtCore.QRect(30, 420, 181, 25))
        self.StartingLocation.setObjectName("StartingLocation")
        self.StartingLocation.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.DeltaVLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.DeltaVLabel.setGeometry(QtCore.QRect(30, 20, 91, 17))
        self.DeltaVLabel.setObjectName("DeltaVLabel")
        self.DeltaVNumber = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.DeltaVNumber.setGeometry(QtCore.QRect(30, 50, 201, 26))
        self.DeltaVNumber.setMaximum(999999999)
        self.DeltaVNumber.setObjectName("DeltaVNumber")
        self.AddDeltaV = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AddDeltaV.setGeometry(QtCore.QRect(250, 50, 80, 25))
        self.AddDeltaV.setObjectName("AddDeltaV")
        self.Graph = QtWidgets.QWidget(parent=self.centralwidget)
        self.Graph.setGeometry(QtCore.QRect(370, 20, 501, 501))
        self.Graph.setObjectName("Graph")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Custom Linking
        FillStartingPosition(self.StartingLocation)
        self.StartingLocation.setStyleSheet("combobox-popup: 0;")
        self.AddDeltaV.clicked.connect(self.printing)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kerbal Knowledge System"))
        self.RoundTrip.setText(_translate("MainWindow", "Round Trip"))
        self.Aerobreaking.setText(_translate("MainWindow", "Aerobraking"))
        self.PlaneChange.setText(_translate("MainWindow", "Plane Change"))
        self.DeltaVLabel.setText(_translate("MainWindow", "Input Delta-V:"))
        self.AddDeltaV.setText(_translate("MainWindow", "Add Delta-V"))

    #custom Functions
    def printing(self):
        print("Combobox: " + str(self.StartingLocation.itemData(self.StartingLocation.currentIndex())))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())