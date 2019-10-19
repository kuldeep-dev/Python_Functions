#  Healthy Programmer task in python

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while True:
                a = input()
                if a == stopper:
                        mixer.music.stop()
                        break

def log_now(msg):
        with open("mylogs.txt","a") as f:
                f.write(f"{msg} {datetime.now()}\n")


if __name__=='__main__':
        # musiconloop("water.mp3","stop")
        init_water = time()
        init_eyes = time()
        init_exercise = time()
        watersecs = 40*60
        exsecs = 30*60
        eyesecs = 45*60

        while True:
                # Dring water
                if time()- init_water > watersecs:
                        print("water drinking time. Enter 'drank' to stop the alaram.")
                        musiconloop("water.mp3","drank")
                        init_water = time()
                        log_now("drank water at")

                # Eyes
                if time()- init_eyes > eyesecs:
                        print("Eyes exercise time. Enter 'doneeyes' to stop the alaram.")
                        musiconloop("eyes.mp3","doneeyes")
                        init_eyes = time()
                        log_now("Eye relaxed at")        


                 # Exercise
                if time()- init_exercise > exsecs:
                        print("Pysical activity time. Enter 'donephy' to stop the alaram.")
                        musiconloop("physical.mp3","donephy")
                        init_exercise = time()
                        log_now("Pysical activity done at")                