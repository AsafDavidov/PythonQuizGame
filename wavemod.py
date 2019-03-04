# Sound Processing using .wav files
# Adapted from http://www.eg.bucknell.edu/~csci203/2012-fall/hw/hw03/hw3pr4.html

import math
#import imp
from csaudio import *

class WavMod:
    """WavMod constructor takes:
        fileName, a string indicating the sound you wish to use.
        outputFile, an OPTIONAL string indicating the name to which
                     you wish to save the modified sound.
                     If you don't specify a second input,
                     the new sound will be saved as "out.wav"
    """
    def __init__(self,fileName, outputFile = "out.wav"):
        self.wavFile = fileName
        self.newFile = outputFile

    def changeSpeed(self,newSampleRate):
        """ changeSpeed takes in             

              newSampleRate, an integer representing the new sample rate you want,
                     in units of samples per second.
    
            changeSpeed creates a new file (using the name in newFile)
              that uses the same sound data as self.wavFile, but runs it at the
              samplerate of newSampleRate samples per second.
              It plays the new sound and then does not return anything...
        """
        # This next function call returns TWO values:
        #   samples is a LIST of the raw sound data
        #   oldSampleRate is the old sample rate, in samples per second
        #
        # This will be the standard way to get sound data from a file.
        samples, oldSampleRate = readWav(self.wavFile)

        # This next function call does not return any value, but
        #   it does write the sound data in the list "samples" into
        #   a file whose name is the string in the newFile variable
        #   It uses the new sample rate instead of the old.
        writeWav(samples, newSampleRate, self.newFile)

        # This next call to play also does not return a value,
        #   but it plays the sound in the file named newFile.
        play(self.newFile)

        # Now, we return the list of the sound data - it won't always
        #   be needed, we return it just in case it is.
        # actually, let's comment this out for now...
        #return samples

    def flipflop(self):
        """ flipflop creates a new file (using the name in self.newFile)
              that uses the same sound data as self.wavFile, but with the first and second
              halves of the sound interchanged.

            flipflop plays the new sound that it creates (no return value)
        """
        samples, sampleRate = readWav(self.wavFile)

        length = len(samples)
        newSamples = samples[length // 2:] + samples[:length // 2] # flip flop

        writeWav(newSamples, sampleRate, self.newFile)

        play(self.newFile)      # play the new sound for good measure

        #return newSamples  # return the new sound data list - commented for now

    
    # a function to make sure everything is working
    def test(self):
        """ a test function that plays the wav file.
        """
        play(self.wavFile)


    def reverse(self):
        samples, sampleRate = readWav(self.wavFile)

        #number of sample data point
        n = len(samples)

        #new wave form data storage
        newSamples=[]

        #for each sample point in data, copy data from samples in reverse order
        for i in range(n):
            ###your code here (comment pass and add your code)
            newSamples.append(samples[n-i-1])
            #newSamples.append(samples.pop())

        #write new sample to wave file
        writeWav(newSamples, sampleRate, self.newFile)

        #play new file
        play(self.newFile)
    
    def volume(self,fraction):
        samples, sampleRate = readWav(self.wavFile)
        n = len(samples)
        newSamples = []
        for i in range(n):
            newSamples.append(samples[i]*fraction)
        writeWav(newSamples, sampleRate, self.newFile)
        play(self.newFile)

    def oneFreq(self,freq, secs):
        amplitude = 32767.0
        twoPi = 2*math.pi
        sampleRate = 22050
        #sample data storage
        samples = []

        #iterate all sample point and generate waveform data
        for i in range(int(sampleRate*secs)):
            ###your code here (comment pass and add your code)
            #pass
            samples.append( math.sin(twoPi*freq*i/sampleRate)*amplitude)                     

        #write wave sample data to wave file
        writeWav(samples, sampleRate, self.newFile)

        #play saved wave file
        play(self.newFile)

        
        return samples

    def multiFreq(self,freqList):
        secs = 2
        sampleRate = 22050
        samples=[] #will hold a sample list for each frequency in freqList

        #generate multiple sample data corresponding each given frequency
        #assume we have three frequencies for chord
        for i in range(3):
            samples.append(self.oneFreq(freqList[i],secs))

        #new sample data storage
        newSamples = []

        #for each data point, append averaged sample data from multiple frequencies 
        for i in range(int(sampleRate*secs)):
            ###your code here (comment pass and add your code)
            #pass
            newSamples.append( (samples[0][i] + samples[1][i] + samples[2][i]) / 3)

        #write wave sample data to file
        writeWav(newSamples, sampleRate, self.newFile)

        #play saved wav file
        play(self.newFile)
    
    


def main():
    wm = WavMod('swfaith.wav')
    wm.test()

    wm.changeSpeed(14000)
    wm.flipflop()
    wm.volume(1/2)

    wm.reverse()
    wm.oneFreq(220,1)

    wm.multiFreq([440, 440*1.26, 440*1.5])
    wm.multiFreq([440, 442, 443])
    wm.multiFreq([440, 440, 440])
    wm.multiFreq([439, 440, 441])

if __name__ == "__main__":
    main()
