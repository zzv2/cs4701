# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrum_sensing.ui'
#
# Created: Wed Dec  7 23:18:13 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(639, 738)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.network_params = QtGui.QGroupBox(self.centralwidget)
        self.network_params.setObjectName(_fromUtf8("network_params"))
        self.gridLayout = QtGui.QGridLayout(self.network_params)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.network_params)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.network_params)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.sigmoid_function = QtGui.QComboBox(self.network_params)
        self.sigmoid_function.setObjectName(_fromUtf8("sigmoid_function"))
        self.sigmoid_function.addItem(_fromUtf8(""))
        self.sigmoid_function.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.sigmoid_function, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.network_params)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.neurons_h2 = QtGui.QSpinBox(self.network_params)
        self.neurons_h2.setProperty("value", 5)
        self.neurons_h2.setObjectName(_fromUtf8("neurons_h2"))
        self.gridLayout.addWidget(self.neurons_h2, 1, 1, 1, 1)
        self.neurons_h1 = QtGui.QSpinBox(self.network_params)
        self.neurons_h1.setProperty("value", 10)
        self.neurons_h1.setObjectName(_fromUtf8("neurons_h1"))
        self.gridLayout.addWidget(self.neurons_h1, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.network_params)
        self.training_params = QtGui.QGroupBox(self.centralwidget)
        self.training_params.setObjectName(_fromUtf8("training_params"))
        self.gridLayout_3 = QtGui.QGridLayout(self.training_params)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.training_params)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.training_params)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.training_params)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.num_epochs = QtGui.QSpinBox(self.training_params)
        self.num_epochs.setMaximum(1000000)
        self.num_epochs.setProperty("value", 100)
        self.num_epochs.setObjectName(_fromUtf8("num_epochs"))
        self.gridLayout_3.addWidget(self.num_epochs, 0, 1, 1, 1)
        self.learning_rate = QtGui.QDoubleSpinBox(self.training_params)
        self.learning_rate.setDecimals(4)
        self.learning_rate.setMaximum(1.0)
        self.learning_rate.setSingleStep(0.001)
        self.learning_rate.setProperty("value", 0.01)
        self.learning_rate.setObjectName(_fromUtf8("learning_rate"))
        self.gridLayout_3.addWidget(self.learning_rate, 2, 1, 1, 1)
        self.training_tolerance = QtGui.QDoubleSpinBox(self.training_params)
        self.training_tolerance.setDecimals(7)
        self.training_tolerance.setMaximum(1.0)
        self.training_tolerance.setSingleStep(1e-06)
        self.training_tolerance.setProperty("value", 1e-05)
        self.training_tolerance.setObjectName(_fromUtf8("training_tolerance"))
        self.gridLayout_3.addWidget(self.training_tolerance, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.training_params)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout.addWidget(self.label_13)
        self.train_button = QtGui.QPushButton(self.centralwidget)
        self.train_button.setObjectName(_fromUtf8("train_button"))
        self.verticalLayout.addWidget(self.train_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.epoch_loss_plot = QtGui.QWidget(self.centralwidget)
        self.epoch_loss_plot.setMinimumSize(QtCore.QSize(0, 300))
        self.epoch_loss_plot.setMaximumSize(QtCore.QSize(16777215, 600))
        self.epoch_loss_plot.setObjectName(_fromUtf8("epoch_loss_plot"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.epoch_loss_plot)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout.addWidget(self.epoch_loss_plot)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.neurons_h1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_13.setNum)
        QtCore.QObject.connect(self.neurons_h2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_13.setNum)
        QtCore.QObject.connect(self.sigmoid_function, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.label_13.setText)
        QtCore.QObject.connect(self.num_epochs, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_13.setNum)
        QtCore.QObject.connect(self.learning_rate, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), self.label_13.setNum)
        QtCore.QObject.connect(self.training_tolerance, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), self.label_13.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.network_params.setTitle(_translate("MainWindow", "Network Params", None))
        self.label.setText(_translate("MainWindow", "Number of neurons in\n"
"Hidden Layer 1", None))
        self.label_2.setText(_translate("MainWindow", "Number of neurons in\n"
"Hidden Layer 2", None))
        self.sigmoid_function.setItemText(0, _translate("MainWindow", "logsig", None))
        self.sigmoid_function.setItemText(1, _translate("MainWindow", "other", None))
        self.label_5.setText(_translate("MainWindow", "Sigmoid function in\n"
"Hidden Layers", None))
        self.training_params.setTitle(_translate("MainWindow", "Training Params", None))
        self.label_3.setText(_translate("MainWindow", "Learning Rate", None))
        self.label_11.setText(_translate("MainWindow", "Num Epochs", None))
        self.label_4.setText(_translate("MainWindow", "Training tolerance", None))
        self.label_13.setText(_translate("MainWindow", "TextLabel", None))
        self.train_button.setText(_translate("MainWindow", "Train", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

