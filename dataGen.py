c
from scipy import signal as sig
from scipy import stats as stat

#freq0 = 4000

Fc = 1000       #simulate a carrier frequency of 1kHz
Fbit = 50       #simulated bitrate of data
Fdev = 500      #frequency deviation, make higher than bitrate
N = 64          #how many bits to send
A = 1           #transmitted signal amplitude
Fs = 10000      #sampling frequency for the simulator, must be higher than twice the carrier frequency
A_n = 0.10      #noise peak amplitude
N_prntbits = 10 #number of bits to print in plots

def power(x):
	power = 0.0
	for i in range(0, len(x)):
		power += pow(x[i], 2.0)
	return power/len(x)

def main():
	#make data
	data_in = np.random.random_integers(0,1,N)
	t = np.arange(0,float(N)/float(Fbit),1/float(Fs), dtype=np.float)
	#extend the data_in to account for the bitrate and convert 0/1 to frequency
	m = np.zeros(0).astype(float)
	for bit in data_in:
	    if bit == 0:
	        m=np.hstack((m,np.multiply(np.ones(Fs/Fbit),Fc+Fdev)))
	    else:
	        m=np.hstack((m,np.multiply(np.ones(Fs/Fbit),Fc-Fdev)))
	#calculate the output of the VCO
	B = 2*Fdev
	y=np.zeros(0)
	y=A * np.cos(2*np.pi*np.multiply(m,t))
	noise = (np.random.randn(len(y))+1)*A_n
	snr = stat.signaltonoise(y)
	yn = np.add(y,noise)
	snrn = stat.signaltonoise(yn)
	print(power(y))
	print(power(noise))
	print(power(yn))





	
	
	#signal = (2 + np.sqrt(2)*np.cos(2*np.pi*freq*t + theta))*np.cos(2*np.pi*freq0+theta0)

if __name__ == '__main__':
	main()