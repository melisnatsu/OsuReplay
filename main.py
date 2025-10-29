import osrparse
import os;
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import requests
from dotenv import load_dotenv
load_dotenv()

name = input()

api_url = f"https://osu.ppy.sh/api/v2/users/{name}"

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": "client_credentials",
    "scope": "public"
}
token_url = "https://osu.ppy.sh/oauth/token"

response = requests.post(token_url, data=data)
access_token = response.json()["access_token"]
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {access_token}"
}
user_data = requests.get(api_url, headers=headers).json()

print(user_data["is_online"])
print(user_data["statistics"]["global_rank"])
print(user_data["statistics"]["pp"])
print(user_data["statistics"]["level"]["current"])
print(user_data["statistics"]["hit_accuracy"])
input()
os.system("clear");
Tk().withdraw()
t = 2
while(t > 0):
    filename = askopenfilename(defaultextension="C:\\Users\\mique\\AppData\\Local\\osu!\\Replays")
    
    osuReplaysPath = "C:\\Users\\mique\\AppData\\Local\\osu!\\Replays\\"

    if(filename):
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