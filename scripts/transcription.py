import sys
sys.argv = ['']

import os

#soundfiles = os.listdir("/media/nas_mount/Ritwik/subtask1_blindset/bengali_segmented")

#files = []

#for file in soundfiles:
#    if file[-3:] == "wav":
#        files.append("/media/nas_mount/Ritwik/subtask1_blindset/bengali_segmented/" + file)


with open("/home/sreyan/interspeech_hindi/test_finetune_manifests/telegu_test_manifest_nas_path.txt", 'r') as file1:
    lines = file1.readlines()

files = []

for line in lines:
    feats = line.strip().split("\t")
    files.append(feats[0])

from stt_2 import Transcriber
transcriber = Transcriber(pretrain_model = '/media/nas_mount/Ritwik/checkpoints_interspeech/full_pretrain_hindi/checkpoint_best.pt', finetune_model = '/media/nas_mount/Ritwik/checkpoints_interspeech/full_finetune_hindi_hindi/checkpoint_best.pt',
                          dictionary = '/media/nas_mount/Ritwik/multilingual_manifest/dict.ltr.txt',
                          lm_type = 'kenlm',
                          lm_lexicon = '/home/sreyan/interspeech_hindi/self-supervised-speech-recognition/ritwik_outputs/subtask2/lexicon.txt', lm_model = '/home/sreyan/interspeech_hindi/self-supervised-speech-recognition/ritwik_outputs/subtask2/lm.bin',
                          lm_weight = 1.5, word_score = -1, beam_size = 50)
hypos = transcriber.transcribe(files)
#print(hypos)

with open('transcriptions_telegu_no_english.txt', 'w') as f:
    for item in hypos:
        f.write("%s\n" % item)

#with open('transcriptions_order.txt', 'w') as f:
#    for item in files:
#        f.write("%s\n" % item)
