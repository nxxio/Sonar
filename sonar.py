import numpy as np
import matplotlib.pyplot as pypl




class Sonar():

    def CreateSignal(self,fb,T, tau, fs, ampl):

        num_impls = int(np.round(tau*fs))

        self.timeArr = np.arange(0,T,1/fs)
        self.signal = np.zeros(self.timeArr.size)

        t_imls = self.timeArr[0:num_impls]
        self.signal[0:num_impls] = ampl*np.sin(2*np.pi*fb*t_imls)
        self.signal_attr = {'BaseFreq': fb,'TimeArr': self.timeArr,'Ampl': ampl,'Signal1': self.signal,'NumImpls': num_impls,'LenSignalArr': len(self.timeArr), 'fs': fs, 'Signal2': self.signal}

        return self.signal_attr

    def show_signal(self, signal):

        return [self.timeArr, signal[0],signal[1],signal[2],signal[3]]

class Echo():

    def reflectSubmarine(self, signalAttr, r,d=0.2):

        fs = signalAttr.get('fs')
        signal1 = signalAttr.get('Signal1')
        signal2 = signalAttr.get('Signal2')
        numImpls = signalAttr.get('NumImpls')
        ampl = signalAttr.get('Ampl')
        timeArr = signalAttr.get('TimeArr')
        fb = signalAttr.get('BaseFreq')

        blic = np.random.randint(3,6)
        testx = []
        testy = []
        testx.append(0)
        testy.append(0)
        alpha = np.random.randint(45,135)
        
        phi = np.random.randint(180)
       
        alpha = np.deg2rad(alpha)
        phi =np.deg2rad(phi)

        for i in range(blic):

            x = r*np.cos(alpha) + 20*i*np.cos(phi) 
            y = r*np.sin(alpha) + 20*i*np.sin(phi)
            testx.append(x)
            testy.append(y)
            R = np.sqrt(np.power(x,2) + np.power(y,2))
            delay = 2*R/1500
            num_delay = round(delay*fs)
            ampl1 = self.ChAmpl(ampl,R)
          
            phi_blic = np.arctan(y/x)
            
            dphi = 2*np.pi*fb*d*np.sin(phi_blic)/1500
            t_echo = timeArr[num_delay:num_delay+numImpls]
            signal1[num_delay:num_delay+numImpls] = ampl1*np.sin(2*np.pi*fb*t_echo)
            signal2[num_delay:num_delay+numImpls] = ampl1*np.sin(2*np.pi*fb*t_echo + dphi)


        signalAttr.update(Signal1 = signal1)
        signalAttr.update(Signal2 = signal2)
        
        return [signal1,signal2,testx,testy]
    
    def ChAmpl(self, ampl, r):

        dbAmpl = 20*np.log10(ampl)
        dbAmpl -= (3.2*r/1000 + 20*np.log10(r/1000))
        ampl = np.power(10,dbAmpl/20)

        return ampl
    
    def reflectFake(self, signalAttr, r,d=0.2):
        
        fs = signalAttr.get('fs')
        signal1 = signalAttr.get('Signal1')
        signal2 = signalAttr.get('Signal2')
        numImpls = signalAttr.get('NumImpls')
        ampl = signalAttr.get('Ampl')
        timeArr = signalAttr.get('TimeArr')
        fb = signalAttr.get('BaseFreq')

        testx = []
        testy = []
        testx.append(0)
        testy.append(0)
        alpha = np.random.randint(45,135)
        alpha = np.deg2rad(alpha)
        phi = alpha

        for i in range(3):

            x = r*np.cos(alpha) + 20*i*np.cos(phi) 
            y = r*np.sin(alpha) + 20*i*np.sin(phi)
            testx.append(x)
            testy.append(y)
            R = np.sqrt(np.power(x,2) + np.power(y,2))
            delay = 2*R/1500
            num_delay = round(delay*fs)
            ampl1 = self.ChAmpl(ampl,R)

            phi_blic = np.arctan(y/x)
            
            dphi = 2*np.pi*fb*d*np.sin(phi_blic)/1500
            t_echo = timeArr[num_delay:num_delay+numImpls]
            signal1[num_delay:num_delay+numImpls] = ampl1*np.sin(2*np.pi*fb*t_echo)
            signal2[num_delay:num_delay+numImpls] = ampl1*np.sin(2*np.pi*fb*t_echo + dphi)


        signalAttr.update(Signal1 = signal1)
        signalAttr.update(Signal2 = signal2)

        return [signal1,signal2,testx,testy]
    
    def reflectCloud(self, signalAttr, r,d=0.2):

        fs = signalAttr.get('fs')
        signal1 = signalAttr.get('Signal1')
        signal2 = signalAttr.get('Signal2')
        numImpls = signalAttr.get('NumImpls')
        ampl = signalAttr.get('Ampl')
        timeArr = signalAttr.get('TimeArr')
        fb = signalAttr.get('BaseFreq')

        testx = []
        testy = []
        testx.append(0)
        testy.append(0)
        alpha = np.random.randint(45,135)
        alpha = np.deg2rad(alpha)

        for i in range(20):

            x = r*np.cos(alpha) + 120*np.random.rand(1) 
            y = r*np.sin(alpha) + 120*np.random.rand(1)
            testx.append(x)
            testy.append(y)
            R = np.sqrt(np.power(x,2) + np.power(y,2))[0]
            delay = 2*R/1500
            num_delay = round(delay*fs)
            ampl1 = self.ChAmpl(ampl,R)
            phi_blic = np.arctan(y/x)
            dphi = 2*np.pi*fb*d*np.sin(phi_blic)/1500
            t_echo = timeArr[num_delay:num_delay+numImpls]
            signal1[num_delay:num_delay+numImpls] = ampl1*np.sin(2*np.pi*fb*t_echo)
            signal2[num_delay:num_delay+numImpls] = ampl1*np.sin(2*np.pi*fb*t_echo + dphi)


        signalAttr.update(Signal1 = signal1)
        signalAttr.update(Signal2 = signal2)
        
        return [signal1,signal2,testx,testy]

class Water():

    def ChangeSignal(self, signalAttr):

        len = signalAttr.get('LenSignalArr')
        numImpls = signalAttr.get('NumImpls')
        ampl = signalAttr.get('Ampl')
        signal1 = signalAttr.get('Signal1')
        signal2 = signalAttr.get('Signal2')

        for i in range(len):

            if i > numImpls:
                
                noise = 0.1*ampl*np.random.rand()
                if i % 2 == 0:
                    noise = -1*noise
                signal1[i] = noise
                signal2[i] = noise

        signalAttr.update(Signal1 = signal1)
        signalAttr.update(Signal2 = signal2) 

        return signalAttr

    def Filter(self, signalAttr):

        signal1 = signalAttr.get('Signal1')
        signal2 = signalAttr.get('Signal2')
        len = signalAttr.get('LenSignalArr')
        fs = signalAttr.get('fs')
        numImpls = signalAttr.get('NumImpls')

        num_delay = round(2*fs)


        SIGNAL1 = np.fft.fft(signal1)
        SIGNAL1 = abs(SIGNAL1)
        print(SIGNAL1.size)
        freq = np.linspace(0,fs,SIGNAL1.size)
        print(freq.size)

        pypl.plot(SIGNAL1)
        pypl.show()
        

def Simulation(fb,T, tau, fs, ampl, r,d, type):

    if r >3000:
        return 1

    sonar1 = Sonar()
    SA = sonar1.CreateSignal(fb,T, tau, fs, ampl)
    water = Water()
    SA = water.ChangeSignal(SA)
    echo = Echo()

    if type == 0:
        signal = echo.reflectSubmarine(SA,r,d)
    elif type == 1:
        signal = echo.reflectFake(SA,r)
    elif type == 2:
        signal = echo.reflectCloud(SA,r,d)

    #water.Filter(SA)
        
    return sonar1.show_signal(signal)


if __name__ == '__main__':

    Simulation(20000,5,0.01,80000,10,1500,0.2,0)