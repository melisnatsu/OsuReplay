import osrparse
import os;
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import math

os.system("cls");
Tk().withdraw()
t = 2
while(t > 0):
    filename = askopenfilename(defaultextension="C:\\Users\\mique\\AppData\\Local\\osu!\\Replays")

    osuReplaysPath = "C:\\Users\\mique\\AppData\\Local\\osu!\\Replays\\"


    replay = osrparse.Replay.from_path(filename)

    playerName = replay.username
    noteCount300 = replay.count_300
    noteCount100 = replay.count_100
    noteCount50 = replay.count_50
    score = replay.score
    missCount = replay.count_miss
    maxCombo = replay.max_combo
    
    accuracy = round(((300*noteCount300 + 100*noteCount100 + 50*noteCount50))/
                     (300*(noteCount300 + noteCount100 + noteCount50 + missCount))*100, 2)

    print(f"Player name: {playerName}")
    print(noteCount300)
    print(noteCount100)
    print(noteCount50)
    print(score)
    print(missCount)
    print(maxCombo)
    print()
    t -= 1


