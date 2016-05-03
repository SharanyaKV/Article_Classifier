from filemngmnt import mngFile
from prediction import predictCategory
from test import testclassifier
from train import trainclassifier
import os

def classify():
    if not os.path.isfile('vocabulary.txt'):
        print('Training and testing the Classifier... ')
        train,test=mngFile()
        trainclassifier(train)
        testclassifier(test)

    else:
        answr = input('Want to train and test the classifier? (Y/N) : ')
        if answr == 'Y' or answr == 'y':
            print('Training and testing the Classifier... ')
            train, test = mngFile()
            trainclassifier(train)
            testclassifier(test)

    print('\nPredicting the category..')

    category = {'t': 'Science & Technology', 'h': 'Health', 'b': 'Business', 's': 'Sports', 'g': 'General',
                'e': 'Entertainment', 'p': 'Politics'}
    files=os.listdir('testdata')
    for file in files:
        print(file +' : ',predictCategory('testdata/'+file))

classify()