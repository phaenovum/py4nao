# This Python file uses the following encoding: utf-8
'''
Created on 03.01.2014

@author: lars
'''

from naoqi import ALProxy

phaenao = {"name": "phänao", "ip": "192.168.1.123", "port": 9559}
    
if __name__ == '__main__':
    tts = ALProxy("ALTextToSpeech", phaenao["ip"], phaenao["port"])
    tts.say("Hallo, ich bin %s!" % phaenao["name"])
