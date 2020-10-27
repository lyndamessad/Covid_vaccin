
import pandas as pd
import json
import os

#ouvrir les fichiers json test et train 
train = pd.read_json('Data/train.json', lines = True)  # 2400rows * 19columns
test = pd.read_json('Data/test.json', lines = True)

# filter le signal bruit, ne prendre que les valeurs > 1.
train= train[train.signal_to_noise >= 1] #filter le signal bruit ::: 1589 rows 

def fill(text, width=80):
    """Split text with a line return to respect fasta format"""
    return os.linesep.join(text[i:i+width] for i in range(0, len(text), width))

def write_sequences(sequences, file_fasta):

    with open(file_fasta, "w") as file:

        for i in range(0, len(sequences)):
            line = ">sequence"+ str(i+1) +"\n"
            file.write(line)
            file.write(fill(str(sequences[i])))
            file.write("\n")
            i = i+1

sequences_train = list(train.sequence)
sequences_test = list(test.sequence)
write_sequences(sequences_train, "train_sequences_file.fasta")
write_sequences(sequences_test, "test_sequences_file.fasta")

