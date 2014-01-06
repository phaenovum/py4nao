# This Python file uses the following encoding: utf-8
'''
Created on 03.01.2014

@author: lars
'''

from naoqi import ALProxy

phaenao = {"name": "phänao", "ip": "192.168.1.123", "port": 9559}
    
tts = ALProxy("ALTextToSpeech", phaenao["ip"], phaenao["port"])
tts.setLanguage('german')

motion = ALProxy("ALMotion", phaenao["ip"], phaenao["port"])
motion.setStiffnesses("Body", 1.0)
motion.moveInit()
id = motion.post.moveTo(0.5, 0, 0)

tts.say("Ich laufe!")

motion.wait(id, 0)

tts.say("Hallo, ich bin %s!" % phaenao["name"])
