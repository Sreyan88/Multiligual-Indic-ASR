import sys
sys.argv = ['']

import os

soundfiles = os.listdir("/media/nas_mount/Ritwik/subtask2_blindset/audios")

files = []

for file in soundfiles:
    if file[-3:] == "wav":
        files.append("/media/nas_mount/Ritwik/subtask2_blindset/audios/" + file)


with open('transcriptions_order.txt', 'w') as f:
    for item in files:
        f.write("%s\n" % item)

