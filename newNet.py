import argparse
import os
import re
import sys
import csv
import random
from decimal import Decimal
import numpy as np


class Network(object):

	def __init__(self, structure):
		self.layers = len(structure)
		self.structure = structure
		self.weightMatrix = []
		self.biasMatrix = []

		for i in range(0, len(structure)-1):
			self.weightMatrix.append(np.array(np.random.randn(structure[i]*structure[i+1])).reshape(structure[i+1], structure[i]))
			self.biasMatrix.append(np.array(np.random.randn(structure[i+1])).reshape(structure[i+1], 1))

	def sigmoid(self, x):
		try:
			sig = (1.0/(1.0 + np.exp(-x)))
		except Warning:
			print("Error: "+str(x))
		return sig

	def dsigmoidDX(self, x):
		return self.sigmoid(x)*(1 - self.sigmoid(x))

	def compute(self, inputs):
		for layer, bias in zip(self.weightMatrix, self.biasMatrix):
			weightedSum = np.dot(layer, inputs) + bias
			inputs = self.sigmoid(weightedSum)
		return inputs

	def test(self, numSamples, testnumber):
		errorList = np.array([])
		correctList = np.array([])
		for row in self.rowlist[-testnumber:]:
			decision = np.array([float(row[-1])])
			inputs = np.array([[float(x)] for x in row[:-1]])
			inputs = np.multiply(np.array([[(1/100)], [(1/100)], [(1/10)], [(1/1000)]]), inputs)
			result = self.compute(inputs)
			final = 0 if result<0.5 else 1
			errorList = np.append(errorList, pow(abs(result-decision), 2.0))
			correctList = np.append(correctList, abs(final - decision))
		print("Percent Correct: " + str((1- (np.sum(correctList)/testnumber))*100.0)+"%")
		return np.sqrt(np.sum(errorList)/testnumber)

	def train_setup(self, dataFile, epochs, numSamples):
		self.weightUpdateMatrix = [np.zeros(x.shape) for x in self.weightMatrix]
		self.biasUpdateMatrix = [np.zeros(y.shape) for y in self.biasMatrix]
		self.epochs_arr = np.arange(epochs)
		self.totalError = np.array(np.zeros(epochs))
		self.epochError = np.array(np.zeros(numSamples))
		with open(dataFile, "r") as csvfile:
			reader = csv.reader(csvfile)
			self.rowlist = list(reader)
			

	def train(self, dataFile, learnRate, epochs, tolerance, numSamples, batchsize, plot=None):
		for i in range(epochs):
			self.run_epoch(learnRate, numSamples, batchsize, i)
		self.test(numSamples)
		return (self.epochs_arr, self.totalError)

	def run_epoch(self, learnRate, numSamples, tolerance, batchsize, i, testnumber):
		k = 0
		truthArray = np.array(np.zeros(numSamples))
		random.shuffle(self.rowlist)
		for row in self.rowlist:
			decision = np.array([float(row[-1])])
			inputs = np.array([[float(x)] for x in row[:-1]])
			inputs = np.multiply(np.array([[(1/100)], [(1/100)], [(1/10)], [(1/1000)]]), inputs)
			(weightChange, biasChange, result) = self.propagate(inputs, decision)
			self.weightUpdateMatrix = np.add(self.weightUpdateMatrix, weightChange)
			self.biasUpdateMatrix = np.add(self.biasUpdateMatrix, biasChange)
			self.epochError[k-1] = pow(abs(result - decision), 2.0)
			truthArray[k-1] = 1 if abs(result-decision) < tolerance else 0
			k+=1
			if k>numSamples:
				break
			if k%batchsize == 0:
				self.weightMatrix = np.subtract(self.weightMatrix, np.multiply(np.array([(learnRate/numSamples)]), self.weightUpdateMatrix))
				self.biasMatrix = np.subtract(self.biasMatrix, np.multiply(np.array([(learnRate/numSamples)]), self.biasUpdateMatrix))
		self.totalError[i] = self.test(numSamples, testnumber)
		print("Epoch "+str(i)+": "+str(self.totalError[i]) + " tolsum: "+str(np.sum(truthArray)))
		done = np.sum(truthArray)>len(truthArray)-1
		return (self.epochs_arr, self.totalError, done)

	def propagate(self, inputs, decision):
		weightUpdateMatrix = []
		biasUpdateMatrix = []
		weightUpdateMatrix = [np.zeros(x.shape) for x in self.weightMatrix]
		biasUpdateMatrix = [np.zeros(y.shape) for y in self.biasMatrix]
		sums = []
		outputs = [inputs]
		
		for layer, bias in zip(self.weightMatrix, self.biasMatrix):
			weightedSum = np.dot(layer, inputs) + bias
			sums.append(weightedSum)
			inputs = self.sigmoid(weightedSum)
			outputs.append(inputs)
		error = (outputs[-1] - decision)*self.dsigmoidDX(sums[-1])
		biasUpdateMatrix[-1] = error
		weightUpdateMatrix[-1] = np.dot(error, outputs[-2].transpose())
		
		i = -2
		for layer in reversed(self.weightMatrix[:-1]):
			error = error * self.weightMatrix[i+1].transpose() * self.dsigmoidDX(sums[i])
			biasUpdateMatrix[i] = error
			weightUpdateMatrix[i] = np.dot(error, outputs[i-1].transpose())
		return (weightUpdateMatrix, biasUpdateMatrix, outputs[-1])
		
def main():
	structure = []
	for i in range(1, len(sys.argv)):
		structure.append(int(sys.argv[i]))
	net = Network(structure)

if __name__ == '__main__':
	main()