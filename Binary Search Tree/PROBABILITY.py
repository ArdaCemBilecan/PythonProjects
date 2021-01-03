import random
import pylab

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollDieN(n):
    result = ""
    for i in range(n):
        result = result+" "+str(rollDie())
    print(result)
    
    
def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.choice(['H','T']) == 'H':
            heads = heads+1
    return heads/numFlips



def flipSim(numFlipsPerTrial,numTrials):
    fracHeads=[]
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean


def regressToMean(numFlips,numTrials):
    fracHeads=[]
    for i in range(numTrials):
        fracHeads.append(flip(numFlips))
    extremes,nextTrials=[],[]
    for i in range(len(fracHeads)-1):
        if fracHeads[i]<0.33 or fracHeads[i]>0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
    
    pylab.plot(range(len(extremes)),extremes,'ko',label='Extreme')
    pylab.plot(range(len(nextTrials)),nextTrials,'k^',label = 'Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0,1)
    pylab.xlim(-1,len(extremes)+1)
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fractions Heads')
    pylab.title('Regression to Mean')
    pylab.legend(loc='best')
    pylab.show()



rollDieN(5)  # 5 defa zar atılsın ve sonuıçları yazdır
# Yazı tura deneyinde Tura yüzdesi
print(flip(10))
# Tüm para atma oalyında turanın gelme olaslığıonı tutuyor
print(flipSim(100,100))

regressToMean(15,40)


