from scipy.io import wavfile
from tqdm import tqdm

with open("/media/nas_mount/Ritwik/subtask1_blindset/hindi/files/segments", 'r') as file1:
    lines = file1.readlines()

new_file = []
old_file = []
starting = []
ending = []

for line in lines:
    feats = line.strip().split()
    new_file.append(feats[0])
    old_file.append(feats[1])
    starting.append(float(feats[2]))
    ending.append(float(feats[3]))
    

    

for o,n,s,e in tqdm(zip(old_file, new_file, starting, ending)):
    sampleRate, waveData = wavfile.read("/media/nas_mount/Ritwik/subtask1_blindset/hindi/" + o + ".wav")
    startSample = int( s * sampleRate )
    endSample = int( e * sampleRate )
    wavfile.write( "/media/nas_mount/Ritwik/hindi_segmented/" + n + ".wav", sampleRate, waveData[startSample:endSample])
