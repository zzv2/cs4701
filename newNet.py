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
		# print(self.weightMatrix)
		# print(self.biasMatrix)

	def sigmoid(self, x):
		#x = np.arange(Decimal(30), Decimal(90))
		try:
			sig = (1.0/(1.0 + np.exp(-x)))
		except Warning:
			print("THis is whats fucking up: "+str(x))
		return sig

	def dsigmoidDX(self, x):
		return self.sigmoid(x)*(1 - self.sigmoid(x))

	def compute(self, inputs):
		for layer, bias in zip(self.weightMatrix, self.biasMatrix):
			weightedSum = np.dot(layer, inputs) + bias
			inputs = self.sigmoid(weightedSum)
		return inputs

	def test(self, rowlist, numSamples):
		errorList = np.array([])
		correctList = np.array([])
		for row in rowlist[numSamples:(numSamples+100)]:
			decision = np.array([float(row[-1])])
			inputs = np.array([[float(x)] for x in row[:-1]])
			inputs = np.multiply(np.array([[(1/100)], [(1/100)], [(1/10)], [(1/1000)]]), inputs)
			result = self.compute(inputs)
			print("result: "+str(result)+" decision: "+str(decision))
			final = 0 if result<0.5 else 1
			errorList = np.append(errorList, abs(result-decision))
			correctList = np.append(correctList, abs(final - decision))
		print("Total Error: " + str(np.sum(errorList)))
		print("Total Incorrect: " + str(np.sum(correctList)))

	def train(self, dataFile, learnRate, epochs, tolerance, numSamples, batchsize):
		weightUpdateMatrix = []
		biasUpdateMatrix = []
		weightUpdateMatrix = [np.zeros(x.shape) for x in self.weightMatrix]
		biasUpdateMatrix = [np.zeros(y.shape) for y in self.biasMatrix]
		totalError = np.array(np.zeros(epochs))
		epochError = np.array(np.zeros(numSamples))
		with open(dataFile, "r") as csvfile:
			reader = csv.reader(csvfile)
			rowlist = list(reader)
			#random.shuffle(rowlist)
			for i in range(0, epochs):
				k = 0
				csvfile.seek(0)
				for row in rowlist:
					decision = np.array([float(row[-1])])
					inputs = np.array([[float(x)] for x in row[:-1]])
					inputs = np.multiply(np.array([[(1/100)], [(1/100)], [(1/10)], [(1/1000)]]), inputs)
					(weightChange, biasChange, result) = self.propagate(inputs, decision)
					weightUpdateMatrix = np.add(weightUpdateMatrix, weightChange)
					biasUpdateMatrix = np.add(biasUpdateMatrix, biasChange)
					epochError[k-1] = pow(abs(result - decision), 2.0)
					k+=1
					if k>numSamples:
						break
					if k%batchsize == 0:
						self.weightMatrix = np.subtract(self.weightMatrix, np.multiply(np.array([(learnRate/numSamples)]), weightUpdateMatrix))
						self.biasMatrix = np.subtract(self.biasMatrix, np.multiply(np.array([(learnRate/numSamples)]), biasUpdateMatrix))
				print("Epoch "+str(i)+": "+str(np.sum(epochError)))
				totalError[i] = np.sum(epochError)
			self.test(rowlist, numSamples)
			return (np.array([i for i in range(0, len(totalError))]), totalError)

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
		# print(weightUpdateMatrix)
		# print(biasUpdateMatrix)
		return (weightUpdateMatrix, biasUpdateMatrix, outputs[-1])
		
def main():
	structure = []
	for i in range(1, len(sys.argv)):
		structure.append(int(sys.argv[i]))
	net = Network(structure)
	#net.propagate(np.array([[1.0],[1.0]]), np.array([0.0]))
	#net.train("trainData.csv", 0.01, 300, 1e-5, 2000, 200)

if __name__ == '__main__':
	main()