import sys
import subprocess


games = {
    "Runescape": "konsole -e gamescope --mangoapp -w 2560 -h 1080 -r 165 -F fsr --backend sdl -- flatpak run com.adamcake.Bolt",
    "Minecraft": "konsole -e gamescope --force-grab-cursor --mangoapp -w 2560 -h 1080 -r 165 -F fsr --backend sdl -- flatpak run org.polymc.PolyMC"
}
if (len(sys.argv) > 1):
    print(games.get(sys.argv[1]))
    subprocess.call(games.get(sys.argv[1]), shell=True)
else:
    print("What Game Do You Want To Play?")
    print(games.keys())
    subprocess.call(games.get(input("Enter A Game")), shell=True)
