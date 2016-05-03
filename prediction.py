import re
import Rake



def predictCategory(fname):
    with open('vocabulary.txt','r') as voc_ref:
        vocabulary=voc_ref.read()
        vocabulary = re.split('\n', vocabulary)
        if '' in vocabulary:
            vocabulary.remove('')
        vocabulary = [token.split(':') for token in vocabulary]

    voc_dict={}
    for token in vocabulary :
        if len(token)==2:
            voc_dict [token [0]]=token[1]

    #tokens=Tokenize(fname)

    with open (fname,'r') as text_ref:
        text=text_ref.read()


    rake_obj = Rake.Rake('stopwords.txt')
    tokens=rake_obj.run(text)



    category = {}
    for token in tokens :
        if token[0] in voc_dict :
            cls= voc_dict[token[0]]
            if cls in category:
                category[cls]+=1
            else:
                category[cls] = 1
    print (category)
    clslist = []
    if category!={}:
        clslist=[]
        x = max(category.values())
        for cls in category:
            if category[cls] == x or category [cls]==x-1:
                clslist .append(cls)
    return clslist