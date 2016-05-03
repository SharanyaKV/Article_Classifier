import os
import random


def mngFile():
    trainset={}
    testset={}

    for folder in os.listdir('articles'):
        if len(folder)==1:
            files=os.listdir('articles/'+folder)
            random.shuffle(files)
            n = int(len(files) / 2)
            trainset[folder]=files[:n]
            testset[folder]=files[n:]
    return trainset ,testset