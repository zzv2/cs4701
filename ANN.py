import argparse
import os
import re
import sys
import csv
import random
from decimal import Decimal
import numpy as np

class HiddenNeuron(object):
	inWeights = []
	upWeights = []
	bias = 0
	upBias = 0
	output = 0
	wegihtedSum = 0
	error = 0

	def __init__(self, inWeights, upWeights, bias, upBias, output, weightedSum, error):
		self.inWeights = inWeights
		self.upWeights = upWeights
		self.bias = bias
		self.upBias = upBias
		self.output = output
		self.weightedSum = weightedSum
		self.error = error

class InputNeuron(object):
	output = 0

	def __init__(self, output):
		self.output = output

class OutputNeuron(object):
	inWeights = []
	upWeights = []
	bias = 0
	upBias = 0
	output = 0
	weightedSum = 0
	error = 0

	def __init__(self, inWeights, upWeights, bias, upBias, output, weightedSum, error):
		self.inWeights = inWeights
		self.upWeights = upWeights
		self.bias = bias
		self.upBias = upBias
		self.output = output
		self.weightedSum = weightedSum
		self.error = error

class Network():
	#def __init__(self):
		#self.main()

	def sigmoid(self, x):
		#x = np.arange(Decimal(30), Decimal(90))
		try:
			sig = (1.0/(1.0 + np.exp(-x)))
		except Warning:
			print("THis is whats fucking up: "+str(x))
		return sig

	def dsigmoidDX(self, x):
		return self.sigmoid(x)*(1 - self.sigmoid(x))

	def backPropagation(self, layers, decision, learnRate, tolerance, numSamples):
		#do shit here
		size = len(layers.keys())
		output_neuron = layers["layer" + str(size-1)][0]
		output_neuron.error= (2*(output_neuron.output - decision)*self.dsigmoidDX(output_neuron.weightedSum))
		output_neuron.upBias += output_neuron.error
		#print("output: " + str(dsigmoidDX(output_neuron.weightedSum)))
		# print("decision: " + str(decision))
		#print("error: "+ str(output_neuron.error))
		for i in range(0, len(output_neuron.inWeights)):
			nabla = output_neuron.error * layers["layer" + str(size-2)][i].output
			#print("GAY output: "+str(layers["layer" + str(size-2)][i].output))
			# if nabla < 0:
			#print("NABLA: " + str(nabla))
			output_neuron.upWeights[i] += nabla
			#print("outputUPW: " + str(output_neuron.upWeights[i]))

		for j in range(2, size):
			currentLayer = layers["layer" + str(size-j)]
			prevLayer = layers["layer" + str(size-j+1)]
			nextLayer = layers["layer" + str(size-j-1)]
			for k in range(0, len(currentLayer)):
				sigPrime = self.dsigmoidDX(currentLayer[i].weightedSum)
				for m in range(0, len(prevLayer)):
					currentLayer[k].error += (prevLayer[m].error * prevLayer[m].inWeights[k] * sigPrime)
				currentLayer[k].upBias += currentLayer[k].error
				for n in range(0, len(nextLayer)):
					# print("N: "+str(n))
					# print("nextout: "+str(nextLayer[n].output))
					nabla1 = currentLayer[k].error * nextLayer[n].output
					# if nabla1<0:
					# 	print("NABLA1: "+str(nabla1))
					currentLayer[k].upWeights[n] +=  nabla1
		# for x in range(1, size):
		# 	upLayer = layers["layer" + str(x)]
		# 	for y in range(0, len(upLayer)):
		# 		#print(upLayer[y].upWeights)
		# 		upLayer[y].inWeights = upLayer[y].upWeights
		# print("bprop")
		# print(layers["layer2"][0].upWeights)
		return layers



	def forwardPropagation(self, layers):
		#do shit here
		size = len(layers.keys())
		for x in range(1, size):
			currentLayer = layers["layer" + str(x)]
			prevLayer = layers["layer" + str(x-1)]
			for y in range(0, len(currentLayer)):
				weightedS = 0.0
				for i in range(0, len(prevLayer)):
					weightedS += currentLayer[y].inWeights[i] * prevLayer[i].output
				currentLayer[y].weightedSum = weightedS + currentLayer[y].bias
				#print("WeightedSum: "+  str(currentLayer[y].weightedSum))
				currentLayer[y].output = self.sigmoid(currentLayer[y].weightedSum)
				# print("currinW:")
				# print(currentLayer[y].inWeights)
				#print("currLayer Output: " + str(currentLayer[y].output))
		decision = layers["layer" + str(size-1)][0].output
		return (layers, decision)

	def printWeights(self, layers):
		size = len(layers.keys())
		for i in range(1, size):
			currentLayer = layers["layer"+str(i)]
			for j in range(0, len(currentLayer)):
				print("layer"+str(i)+" node"+str(j))
				print(currentLayer[j].inWeights, currentLayer[j].bias)

	def test(self, layers, rowlist, numSamples):
		numInputs = 4
		neuronList = []
		errorList = np.array(np.ones(100))
		correctList = np.array(np.ones(100))
		for i in range(numSamples, numSamples+100):
			decision = float(rowlist[i][-1])
			for j in range(0, numInputs):
				if j == 3:
					neuronList.append(InputNeuron(float(rowlist[i][j])/1000))
				elif j == 2:
					neuronList.append(InputNeuron(float(rowlist[i][j])/10))
				else:
					neuronList.append(InputNeuron(float(rowlist[i][j])))
			layers["layer0"] = neuronList
			neuronList = []
			(layers, result) = self.forwardPropagation(layers)
			final = 0 if result<0.5 else 1
			errorList[i-numSamples] = abs(result-decision)
			correctList[i-numSamples] = abs(final - decision)
		print("Total Error: " + str(np.sum(errorList)))
		print("Total Incorrect: " + str(np.sum(correctList)))


	def train(self, network, dataFile, learnRate, epochs, tolerance, numSamples):
		layers = network
		# print(layers["layer2"][0].inWeights)
		# print(layers["layer2"][0].upWeights)
		numInputs = 4
		neuronList = []
		totalError = np.array(np.ones(epochs))
		epochError = np.array(np.ones(numSamples))
		with open(dataFile, "r") as csvfile:
			reader = csv.reader(csvfile)
			rowlist = list(reader)
			random.shuffle(rowlist)
			for i in range(0, epochs):
				# if i >=epochs:
				# 	break
				k = 0
				csvfile.seek(0)
				for row in rowlist:
					decision = float(row[-1])
					for j in range(0, numInputs):
						if j == 3:
							neuronList.append(InputNeuron(float(row[j])/1000))
						elif j == 2:
							neuronList.append(InputNeuron(float(row[j])/10))
						else:
							neuronList.append(InputNeuron(float(row[j])))
					layers["layer0"] = neuronList
					neuronList = []
					(layers, result) = self.forwardPropagation(layers)
					epochError[k] = pow(abs(result - decision), 2.0)
					layers = self.backPropagation(layers, decision, learnRate, tolerance, numSamples)
					k+=1
					if k >=numSamples:#
						size = len(layers.keys())
						for x in range(1, size):
							upLayer = layers["layer" + str(x)]
							for y in range(0, len(upLayer)):
								#print(upLayer[y].upWeights)
								upLayer[y].bias = upLayer[y].bias - (learnRate/numSamples)*upLayer[y].upBias
								upLayer[y].upBias = 0
								upLayer[y].inWeights = [w-(learnRate/numSamples)*nw for w, nw in zip(upLayer[y].inWeights, upLayer[y].upWeights)]
								upLayer[y].upWeights = np.zeros(len(upLayer[y].upWeights))
						#print(np.sum(epochError))
						break
				totalError[i] = np.sum(epochError)
			# layers["layer0"][0].output = -20
			# layers["layer0"][1].output = 0.1148
			# layers["layer0"][2].output = 0.014
			# layers["layer0"][3].output = 1100
			# (layers, result) = forwardPropagation(layers)
			#printWeights(layers)
			# print("FINAL: "+str(result))
			self.test(layers, rowlist, numSamples)
			#print(totalError)
			return (np.array([i for i in range(0, len(totalError))]), totalError)


	def main(self, numOutputs, numHiddenLayers, numInputs, numNeuronsHidden, learnRate, epochs, tolerance, numSamples):
		#command line arguments follow this pattern: numOutputs, numHiddenLayers, numInputs, numNeuronsHidden0, numNeuronsHidden1,...
		layers = dict()
		neuronList = []
		#numInputs = int(sys.argv[3])
		#numOutputs = int(sys.argv[1])
		#numHiddenLayers = int(sys.argv[2])
		#numNeuronsHidden = []	
		
		numNeuronsHidden = numNeuronsHidden[:numHiddenLayers]
		#use these numbers for example
		#inputs = [1, 1]
		# weights0 = [[[0.8, 0.2], [0.4, 0.9], [0.3, 0.5]],[[0.8, 0.2, 0.1], [0.4, 0.9, 0.1], [0.3, 0.5, 0.1]]]
		# upweights0 = [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]],[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]]
		# weights1 = [0.3, 0.5, 0.9]
		# upweights1 = [0.0, 0.0, 0.0]
		#decision = 0
		for x in range(0, numHiddenLayers):
			#numNeuronsHidden.append(int(sys.argv[4+x]))
			for y in range(0, numNeuronsHidden[x]):
				if x == 0:
					neuronList.append(HiddenNeuron(np.random.randn(numInputs), np.zeros(numInputs), np.random.randn(1)[0], 0, 0, 0, 0))
				else:
					neuronList.append(HiddenNeuron(np.random.randn(numNeuronsHidden[x-1]), np.zeros(numNeuronsHidden[x-1]), np.random.randn(1)[0], 0, 0, 0, 0))
			layers["layer" + str(x+1)] = neuronList
			neuronList = []
		for i in range(0, numOutputs):
			#neuronList.append(OutputNeuron(weights1, upweights1,0,0,0))
			neuronList.append(OutputNeuron(np.random.randn(numNeuronsHidden[-1]), np.zeros(numNeuronsHidden[-1]), np.random.randn(1)[0], 0, 0, 0, 0))
		layers["layer" + str(numHiddenLayers+1)] = neuronList
		neuronList = []
		
		# print(len(layers["layer1"][0].inWeights))
		# print(len(layers["layer2"][0].inWeights))
		#print(len(layers["layer3"][0].inWeights))
		return self.train(layers, "trainData.csv", learnRate, epochs, tolerance, numSamples)
		# print(layers["layer1"][1].inWeights[1])
		# for k in range(1, len(layers.keys())):
		# 	print("layer"+str(k)+"\n")
		# 	for thing in layers["layer" + str(k)]:
		# 		print(thing.inWeights)
		# 		print("\n")
		# print("WHAT THE FUCK:")
		# print(layers["layer"+str(2)][0].inWeights)



if __name__ == '__main__':
	N = Network()