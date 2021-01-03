import random
import pylab    
def variance(X):
        mean = sum(X)/len(X)
        tot = 0.0
        for x in X:
            tot += (x - mean)**2
        return tot/len(X)
    
def stdDev(X):
    return variance(X)**0.5


def makePlot(xVals, yVals, title, xLabel, yLabel, style,logX = False, logY = False):
     pylab.figure()
     pylab.title(title)
     pylab.xlabel(xLabel)
     pylab.ylabel(yLabel)
     pylab.plot(xVals, yVals, style)
     if logX:
         pylab.semilogx()
     if logY:
         pylab.semilogy()
         
         
def runTrial(numFlips):
     numHeads = 0
     for n in range(numFlips):
         if random.choice(('H', 'T')) == 'H':
             numHeads += 1
     numTails = numFlips - numHeads
     return (numHeads, numTails) 



def flipPlot1(minExp, maxExp, numTrials):
     ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], [] 
     xAxis = []
     for exp in range(minExp, maxExp + 1):
         xAxis.append(2**exp)
     for numFlips in xAxis:
         ratios, diffs = [], []
         for t in range(numTrials):
             numHeads, numTails = runTrial(numFlips)   
             ratios.append(numHeads/numTails)         
             diffs.append(abs(numHeads - numTails))    
         
         ratiosMeans.append(sum(ratios)/numTrials)
         diffsMeans.append(sum(diffs)/numTrials)
         ratiosSDs.append(stdDev(ratios))
         diffsSDs.append(stdDev(diffs))
     
     numTrialsString = ' (' + str(numTrials) + ' Trials)' 
     title = 'Mean Heads/Tails Ratios' + numTrialsString
     makePlot(xAxis, ratiosMeans, title, 'Number of flips','Mean Heads/Tails', 'ko', logX = True) 
     title = 'SD Heads/Tails Ratios' + numTrialsString 
     makePlot(xAxis, ratiosSDs, title, 'Number of Flips','Standard Deviation', 'ko', logX = True, logY = True) 
        
    
flipPlot1(4,20,20)
            
            
            

