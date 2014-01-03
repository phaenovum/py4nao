# This Python file uses the following encoding: utf-8
'''
Created on 03.01.2014

@author: lars
'''

from naoqi import ALProxy

phaenao = ["phänao", "192.168.1.123", 9559]
    
if __name__ == '__main__':
    tts = ALProxy("ALTextToSpeech", phaenao[2], phaenao[3] )
    tts.say("Hallo, ich bin" + phaenao[1] + "!")
