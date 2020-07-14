import glob, os, subprocess, shutil, sys

if len(sys.argv) == 2:
    print("Downloading and converting.")
    subprocess.call(['youtube-dl', '-f', '140', '-i', sys.argv[1]])
else:
    print("Just converting files in current directory.")

if not os.path.exists("./converted"):
    os.makedirs("./converted")

files = os.listdir("./")
for file in files:
    if file.endswith(".wav") or file.endswith(".m4a"):
        subprocess.call(['ffmpeg.exe', '-i', file, '-acodec', 'libmp3lame', '-ab', '192k', file+".mp3"])

files = os.listdir("./")
for file in files:
    if file.endswith(".mp3"):
        shutil.move(file, 'converted')

for file in files:
    if file.endswith(".wav") or file.endswith(".m4a"):
        os.remove(file)
