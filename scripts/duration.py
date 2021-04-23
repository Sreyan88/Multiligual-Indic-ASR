
# coding: utf-8

# In[5]:


import numpy as np
import librosa

all_lines_hindi_train = []
with open("/home/sreyan/interspeech_hindi/test_finetune_manifests/hindi_test_manifest.txt", 'r',encoding = "utf-8") as file:
    lines = file.readlines()
    for line in lines:
        all_lines_hindi_train.append(line.strip().split()[0])
        file.close()
        
all_lines_odia_train = []
with open("/home/sreyan/interspeech_hindi/test_finetune_manifests/odia_test_manifest.txt", 'r',encoding = "utf-8") as file:
    lines = file.readlines()
    for line in lines:
        all_lines_odia_train.append(line.strip().split()[0])
        file.close()
        
all_lines_marathi_train = []
with open("/home/sreyan/interspeech_hindi/test_finetune_manifests/marathi_test_manifest.txt", 'r',encoding = "utf-8") as file:
    lines = file.readlines()
    for line in lines:
        all_lines_marathi_train.append(line.strip().split()[0])
        file.close()
        
all_lines_guj_train = []
with open("/home/sreyan/interspeech_hindi/test_finetune_manifests/guj_test_manifest.txt", 'r',encoding = "utf-8") as file:
    lines = file.readlines()
    for line in lines:
        all_lines_guj_train.append(line.strip().split()[0])
        file.close()
        
all_lines_tamil_train = []
with open("/home/sreyan/interspeech_hindi/test_finetune_manifests/tamil_test_manifest.txt", 'r',encoding = "utf-8") as file:
    lines = file.readlines()
    for line in lines:
        all_lines_tamil_train.append(line.strip().split()[0])
        file.close()
        
all_lines_telegu_train = []
with open("/home/sreyan/interspeech_hindi/test_finetune_manifests/telegu_test_manifest.txt", 'r',encoding = "utf-8") as file:
    lines = file.readlines()
    for line in lines:
        all_lines_telegu_train.append(line.strip().split()[0])
        file.close()
        
list_of_list = [all_lines_hindi_train,all_lines_odia_train,all_lines_marathi_train,all_lines_guj_train,all_lines_tamil_train,all_lines_telegu_train]

for item in list_of_list:
    #print(str(item))
    duration = []
    for soundfile in item:
        duration.append(librosa.get_duration(filename=soundfile))
        
    print(str(item).split("_")[2])
        
    print(np.mean(duration))
    print(max(duration))
    print(min(duration))
    print(len(duration))
        
    print("_________________________________________________________")
        

