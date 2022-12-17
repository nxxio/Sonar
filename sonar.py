import numpy as np
import matplotlib.pyplot as pypl




class Sonar():

    def CreateSignal(self,fb,T, tau, fs, ampl):

        num_impls = int(np.round(tau*fs))

        self.timeArr = np.arange(0,T,1/fs)
        self.signal = np.zeros(self.timeArr.size)

        t_imls = self.timeArr[0:num_impls]
        self.signal[0:num_impls] = ampl*np.sin(2*np.pi*fb*t_imls)
        Impls = self.signal[0:num_impls]
        
        self.signal_attr = {'BaseFreq': fb,'TimeArr': self.timeArr,'Ampl': ampl,'Signal': self.signal,'NumImpls': num_impls,'LenSignalArr': len(self.timeArr), 'fs': fs, 'Impuls': Impls}

        return self.signal_attr

    def show_signal(self, signal):

        return [self.timeArr, signal]

class Echo():

    def reflect(self, signalAttr, r):

        fs = signalAttr.get('fs')
        signal = signalAttr.get('Signal')
        numImpls = signalAttr.get('NumImpls')
        Impuls = signalAttr.get('Impuls')

        #blic = np.random.randint(4,6)
        
        #for i in range(blic):
        d = np.random.randint(50)
        r1 = np.sqrt(r*r +d*d)
        tau = 2*r1/1500
        num_tau = round(tau*fs)
        signal[num_tau:num_tau+numImpls] += 0.5*Impuls

        signalAttr.update(Signal = signal)

        return signal


class Water():

    def ChangeSignal(self, signalAttr):

        len = signalAttr.get('LenSignalArr')
        numImpls = signalAttr.get('NumImpls')
        ampl = signalAttr.get('Ampl')
        fb = signalAttr.get('BaseFreq')
        timeArr = signalAttr.get('TimeArr')
        signal = signalAttr.get('Signal')

        for i in range(len):

            if i > numImpls:
                #signal[i] = ampl*np.sin(2*np.pi*fs*self.timeArr[i])/((self.timeArr[i]*1500)*(self.timeArr[i]*1500))
                signal[i] = ampl*np.sin(2*np.pi*fb*timeArr[i])*np.exp(-1*timeArr[i])

        signalAttr.update(Signal = signal)  
        return signalAttr



def Simulation(fb,T, tau, fs, ampl, r):

    if r >3000:
        return 1
    sonar1 = Sonar()
    SA = sonar1.CreateSignal(fb,T, tau, fs, ampl)
    water = Water()
    sa = water.ChangeSignal(SA)
    echo = Echo()
    signal = echo.reflect(sa,r)

    return sonar1.show_signal(signal)
