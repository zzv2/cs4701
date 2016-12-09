# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrum_sensing.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(873, 824)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Training = QtGui.QWidget()
        self.Training.setObjectName(_fromUtf8("Training"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.Training)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.network_params = QtGui.QGroupBox(self.Training)
        self.network_params.setObjectName(_fromUtf8("network_params"))
        self.gridLayout = QtGui.QGridLayout(self.network_params)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sigmoid_function = QtGui.QComboBox(self.network_params)
        self.sigmoid_function.setObjectName(_fromUtf8("sigmoid_function"))
        self.sigmoid_function.addItem(_fromUtf8(""))
        self.sigmoid_function.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.sigmoid_function, 2, 1, 1, 1)
        self.neurons_h1 = QtGui.QSpinBox(self.network_params)
        self.neurons_h1.setMinimum(1)
        self.neurons_h1.setProperty("value", 10)
        self.neurons_h1.setObjectName(_fromUtf8("neurons_h1"))
        self.gridLayout.addWidget(self.neurons_h1, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.network_params)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.network_params)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.network_params)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.neurons_h2 = QtGui.QSpinBox(self.network_params)
        self.neurons_h2.setProperty("value", 5)
        self.neurons_h2.setObjectName(_fromUtf8("neurons_h2"))
        self.gridLayout.addWidget(self.neurons_h2, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.network_params)
        self.training_params = QtGui.QGroupBox(self.Training)
        self.training_params.setObjectName(_fromUtf8("training_params"))
        self.gridLayout_3 = QtGui.QGridLayout(self.training_params)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_11 = QtGui.QLabel(self.training_params)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.training_params)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.training_params)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.learning_rate = QtGui.QDoubleSpinBox(self.training_params)
        self.learning_rate.setDecimals(4)
        self.learning_rate.setMaximum(1.0)
        self.learning_rate.setSingleStep(0.001)
        self.learning_rate.setProperty("value", 0.01)
        self.learning_rate.setObjectName(_fromUtf8("learning_rate"))
        self.gridLayout_3.addWidget(self.learning_rate, 2, 1, 1, 1)
        self.num_epochs = QtGui.QSpinBox(self.training_params)
        self.num_epochs.setMaximum(1000000)
        self.num_epochs.setProperty("value", 100)
        self.num_epochs.setObjectName(_fromUtf8("num_epochs"))
        self.gridLayout_3.addWidget(self.num_epochs, 0, 1, 1, 1)
        self.training_tolerance = QtGui.QDoubleSpinBox(self.training_params)
        self.training_tolerance.setDecimals(7)
        self.training_tolerance.setMaximum(1.0)
        self.training_tolerance.setSingleStep(1e-06)
        self.training_tolerance.setProperty("value", 1e-05)
        self.training_tolerance.setObjectName(_fromUtf8("training_tolerance"))
        self.gridLayout_3.addWidget(self.training_tolerance, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.training_params)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)
        self.num_samples = QtGui.QSpinBox(self.training_params)
        self.num_samples.setMinimum(100)
        self.num_samples.setMaximum(100000)
        self.num_samples.setSingleStep(100)
        self.num_samples.setProperty("value", 1000)
        self.num_samples.setObjectName(_fromUtf8("num_samples"))
        self.gridLayout_3.addWidget(self.num_samples, 5, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.training_params)
        self.train_button = QtGui.QPushButton(self.Training)
        self.train_button.setObjectName(_fromUtf8("train_button"))
        self.verticalLayout_4.addWidget(self.train_button)
        self.groupBox = QtGui.QGroupBox(self.Training)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.epoch_loss_plot = QtGui.QWidget(self.groupBox)
        self.epoch_loss_plot.setMinimumSize(QtCore.QSize(0, 400))
        self.epoch_loss_plot.setMaximumSize(QtCore.QSize(16777215, 600))
        self.epoch_loss_plot.setObjectName(_fromUtf8("epoch_loss_plot"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.epoch_loss_plot)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_3.addWidget(self.epoch_loss_plot)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.tabWidget.addTab(self.Training, _fromUtf8(""))
        self.Test = QtGui.QWidget()
        self.Test.setObjectName(_fromUtf8("Test"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.Test)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.test_button = QtGui.QPushButton(self.Test)
        self.test_button.setObjectName(_fromUtf8("test_button"))
        self.verticalLayout_5.addWidget(self.test_button)
        self.tabWidget.addTab(self.Test, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.network_params.setTitle(_translate("MainWindow", "Network Params", None))
        self.sigmoid_function.setItemText(0, _translate("MainWindow", "logsig", None))
        self.sigmoid_function.setItemText(1, _translate("MainWindow", "other", None))
        self.label.setText(_translate("MainWindow", "Number of neurons in\n"
"Hidden Layer 1", None))
        self.label_2.setText(_translate("MainWindow", "Number of neurons in\n"
"Hidden Layer 2", None))
        self.label_5.setText(_translate("MainWindow", "Sigmoid function in\n"
"Hidden Layers", None))
        self.training_params.setTitle(_translate("MainWindow", "Training Params", None))
        self.label_11.setText(_translate("MainWindow", "Num Epochs", None))
        self.label_3.setText(_translate("MainWindow", "Learning Rate", None))
        self.label_4.setText(_translate("MainWindow", "Training tolerance", None))
        self.label_6.setText(_translate("MainWindow", "Number of Samples", None))
        self.train_button.setText(_translate("MainWindow", "Train", None))
        self.groupBox.setTitle(_translate("MainWindow", "Learning Curve", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Training), _translate("MainWindow", "Training", None))
        self.test_button.setText(_translate("MainWindow", "Test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Test), _translate("MainWindow", "Test", None))

