import sys, random
from PyQt4.QtGui import QApplication, QMainWindow, QVBoxLayout
from PyQt4 import QtCore, QtGui
from PyQt4.uic import loadUiType
from ANN import *
import numpy as np

from spectrum_sensing import Ui_MainWindow
# generate with 'pyuic4 -x spectrum_sensing.ui -o spectrum_sensing.py'

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
	FigureCanvasQTAgg as FigureCanvas,
	NavigationToolbar2QT as NavigationToolbar)

# TODO: import polosyscode.py
# from polosyscode import PoloskysClass

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

class MplCanvas(FigureCanvas):
	"""Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
	def __init__(self, parent=None, width=9, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		# We want the axes cleared every time plot() is called
		self.axes.hold(False)

		self.init_epoch_loss_plot()
		FigureCanvas.__init__(self, fig)

		self.setParent(parent)
		# Create the navigation toolbar, tied to the canvas
		self.mpl_toolbar = NavigationToolbar(self, self)

		expanding = QtGui.QSizePolicy.Expanding
		FigureCanvas.setSizePolicy(self, expanding, expanding)
		FigureCanvas.updateGeometry(self)

	def init_epoch_loss_plot(self):
		self.epoch_loss_plot([0], [0])

	def epoch_loss_plot(self, x, y, color='r'):
		self.axes.plot(x,y, color)
		self.axes.set_xlabel('Epochs')
		self.axes.set_ylabel('Loss')

	def update_epoch_loss(self, epochs, loss):
		# Test data
		n = 100
		loss = [ random.randint(0, 10) for i in range(n) ]
		epochs = [i for i in range(n)]

		self.epoch_loss_plot(epochs, loss)
		self.draw()

class Main(QMainWindow, Ui_MainWindow):
	def __init__(self, ):
		super(Main, self).__init__()
		self.setupUi(self)
		self.setupConnections()
		self.getParams()

		# Setup Cognitive Engine
		self.CognitiveEngine = Network()


	def setupConnections(self):
		self.dc = MplCanvas(self.epoch_loss_plot)
		QtCore.QObject.connect(self.train_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.train)
		# QtCore.QObject.connect(self.neurons_h1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.callback)
		# QtCore.QObject.connect(self.neurons_h2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.callback)
		# QtCore.QObject.connect(self.sigmoid_function, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.callback)
		# QtCore.QObject.connect(self.num_epochs, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.callback)
		# QtCore.QObject.connect(self.learning_rate, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), self.callback)
		# QtCore.QObject.connect(self.training_tolerance, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), self.callback)

	def getParams(self):
		self._neurons_h1 = self.neurons_h1.value()
		self._neurons_h2 = self.neurons_h2.value()
		self._sigmoid_function = str(self.sigmoid_function.currentText())
		self._num_epochs = self.num_epochs.value()
		self._learning_rate = self.learning_rate.value()
		self._training_tolerance = self.training_tolerance.value()
		self._num_samples = self.num_samples.value()

		print("neurons_h1", self._neurons_h1)
		print("neurons_h2", self._neurons_h2)
		print("sigmoid_function", self._sigmoid_function)
		print("num_epochs", self._num_epochs)
		print("learning_rate", self._learning_rate)
		print("training_tolerance", self._training_tolerance)
		print("num_samples", self._num_samples)


	def train(self):
		# Get Parameters from Input Fields
		self.getParams()
		if self._neurons_h2 >0:
			numHiddenLayers = 2
		else:
			numHiddenLayers = 1
		# Run Training Algorithm
		epochs, loss = self.CognitiveEngine.main(
			1,
			numHiddenLayers,
			4,
			[self._neurons_h1, self._neurons_h2],
			#_sigmoid_function,
			self._learning_rate,
			self._num_epochs,
			self._training_tolerance,
			self._num_samples
		)

		# Update Epoch Loss Graph
		# TODO: get epochs, loss
		# epochs, loss = None, None
		self.dc.update_epoch_loss(epochs, loss)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())