import sys, random, time, threading
from PyQt4.QtGui import QApplication, QMainWindow, QVBoxLayout
from PyQt4 import QtCore, QtGui
from PyQt4.uic import loadUiType
from newNet import *
import numpy as np


from spectrum_sensing import Ui_MainWindow
# generate with 'pyuic4 -x spectrum_sensing.ui -o spectrum_sensing.py'

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
	FigureCanvasQTAgg as FigureCanvas,
	NavigationToolbar2QT as NavigationToolbar)

from matplotlibwidget import MatplotlibWidget

# TODO: import polosyscode.py
# from polosyscode import PoloskysClass

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

class Main(QMainWindow, Ui_MainWindow):
	def __init__(self, ):
		super(Main, self).__init__()
		self.setupUi(self)
		self.setup()
		self.getParams()

	def setup(self):
		# Connections
		QtCore.QObject.connect(self.train_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.train)
		self.lock = threading.Lock()
		self.epochs, self.loss = None, None

	def update_epoch_loss_plot(self, x, y, color='r'):
		with self.lock:
			self.epoch_loss_plot.axes.plot(x, y, color)
			self.epoch_loss_plot.axes.set_xlabel('Epochs')
			self.epoch_loss_plot.axes.set_ylabel('Loss')
			self.epoch_loss_plot.axes.set_title('Learning Curve')
			self.epoch_loss_plot.draw()

	def getParams(self):
		self._neurons_h1 = self.neurons_h1.value()
		self._neurons_h2 = self.neurons_h2.value()
		self._sigmoid_function = str(self.sigmoid_function.currentText())
		self._num_epochs = self.num_epochs.value()
		self._learning_rate = self.learning_rate.value()
		self._training_tolerance = self.training_tolerance.value()
		self._num_samples = self.num_samples.value()
		self._batch_size = self.batch_size.value()

		print("neurons_h1", self._neurons_h1)
		print("neurons_h2", self._neurons_h2)
		print("sigmoid_function", self._sigmoid_function)
		print("num_epochs", self._num_epochs)
		print("learning_rate", self._learning_rate)
		print("training_tolerance", self._training_tolerance)
		print("num_samples", self._num_samples)
		print("batch_size", self._batch_size) # how frequently update weights

	def train(self):
		# Get Parameters from Input Fields
		self.getParams()

		# if self._neurons_h2 > 0:
		# 	self.ANN = Network([4,self._neurons_h1, self._neurons_h2, 1])
		# else:
		# 	self.ANN = Network([4, self._neurons_h1, 1])

		# # Run Training Algorithm
		# self.ANN.train_setup("trainData.csv", self._num_epochs, self._num_samples)
		# for i in range(self._num_epochs):
		# 	self.lock.acquire()
		# 	epochs, loss = self.ANN.run_epoch(self._learning_rate, self._num_samples, self._batch_size, i)
		# 	self.lock.release()
		# 	# print(len(epochs))
		# 	# self.update_epoch_loss_plot(epochs, loss)
		# 	thread = threading.Thread(target=self.update_epoch_loss_plot, args=(epochs, loss))
		# 	thread.daemon = True
		# 	thread.start()
		# 	print("update plot...")
		# 	time.sleep(3)
		# self.ANN.test(numSamples)

		# epochs, loss = self.ANN.train(
		# 	"trainData.csv",
		# 	self._learning_rate,
		# 	self._num_epochs,
		# 	self._training_tolerance,
		# 	self._num_samples,
		# 	self._batch_size
		# )

		# Update Epoch Loss Graph
		for a in range(10):
			# self.update_epoch_loss_plot(epochs, loss)
			data_thread = threading.Thread(target=self.get_epoch_loss, args=())
			# data_thread.daemon = True
			data_thread.start()
			data_thread.join()

			plot_thread = threading.Thread(target=self.update_epoch_loss_plot, args=(self.epochs, self.loss))
			# plot_thread.daemon = True
			plot_thread.start()
			plot_thread.join()
			print("updated plot...")
			self.centralwidget.repaint()

	def get_epoch_loss(self):
		with self.lock:
			n = 100
			loss = [ random.randint(0, 10) for i in range(n) ]
			epochs = [i for i in range(n)]
			time.sleep(.5)
			self.epochs, self.loss = epochs, loss

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())