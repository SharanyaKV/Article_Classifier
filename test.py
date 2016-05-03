from prediction import predictCategory


def testclassifier(testset):
    correct=0
    incorrect=0
    for folder in testset :
        for file in testset [folder]:
            print('Testing the file '+file)
            category=predictCategory('articles/'+folder+'/'+file)
            flag=False
            for cls in category :
                if cls==folder:
                    flag=True
            if flag:
                correct+=1
            else:
                print('Incorrect... Identified the category : ' , category,' instead of '+folder )
                incorrect+=1
    print('\nAccuracy : ',end='')
    print((correct / (correct + incorrect ))*100)