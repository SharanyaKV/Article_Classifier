import Rake


def trainclassifier(trainset):
    with open('vocabulary.txt','w') as voc_ref:
        for folder in trainset:
            for file in trainset[folder]:


                #tokens=Tokenize('articles/'+folder+'/'+file)

                with open('articles/'+folder+'/'+file, 'r') as text_ref:
                    text = text_ref.read()

                rake_obj = Rake.Rake('stopwords.txt')
                tokens = rake_obj.run(text)

                for token in tokens:
                    voc_ref .write(token[0]+':'+folder+'\n')

