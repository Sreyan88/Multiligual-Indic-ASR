import os
from tqdm import tqdm
import soundfile
from sklearn.utils import shuffle

lol = "/home/sreyan/interspeech_hindi/merged_merged_finetune_manifests/ritwik_outputs/only_bengali/train"

train_words = os.path.join(lol,'train.wrd')
train_letters = os.path.join(lol,'train.ltr')
train_map = os.path.join(lol,'train.tsv')



with open("/media/nas_mount/Ritwik/subtask1_finetuning/wav2vec_transcripts/subtask1_Bengali_train_manifest.txt") as f:
    data = f.read().splitlines()




words = [d.split('\t')[1] for d in data]
letters = [d.replace(' ','|') for d in words]
letters = [' '.join(list(d)) + ' |' for d in letters]



paths = [d.split('\t')[0] for d in data]
total_duration = 0



for i in tqdm(range(0,len(paths))):
    audio_info = soundfile.info(paths[i])
    frames = audio_info.frames
    total_duration += audio_info.duration
    paths[i] = paths[i] + '\t' + str(frames)


words,letters,paths = shuffle(words,letters,paths)


train_w = words[:]
train_l = letters[:]
train_p = paths[:]


with open(train_words,'w') as f:
    f.write('\n'.join(train_w))

with open(train_letters,'w') as f:
    f.write('\n'.join(train_l))

with open(train_map,'w') as f:
    f.write('\n')
    f.write('\n'.join(train_p))
