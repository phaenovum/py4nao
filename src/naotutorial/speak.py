# This Python file uses the following encoding: utf-8
'''
Created on 03.01.2014

@author: lars
'''

from naoqi import ALProxy

phaenao = "192.168.1.123"
    
if __name__ == '__main__':
    tts = ALProxy("ALTextToSpeech", phaenao, 9559 )
    tts.say("Hallo, ich bin phänao!")
