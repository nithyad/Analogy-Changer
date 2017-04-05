# coding: utf-8

import textblob
from textblob import Word

#   This function will substitute each word with it's top match
#   in word2vec, and will take into account POS tagging, lemmatizing, 
#   spell correction, not using e, and using different starting letters
#
def paraphrase_sentence( sentence, model ):
    """
    This will take in a sentence, and create a new sentence with similar words that don't start with the same letter, or contain e
    """
    # 3 implementations:
    # if the first letter is equal to the first letter of w, move to the next one.
    # don't use the letter e at all
    # spelling corrections

    blob = textblob.TextBlob( sentence )
    print("The sentence's words are")
    LoW = blob.words
    print(LoW)

    NewLoW = ""
    for w in LoW:
        
        if w not in model:
            NewLoW += w + " "
        else:
            
            w_alternatives = model.most_similar(positive=[w], topn=100)

            counter = 0

            for i in range(len(w_alternatives)):
                
                first_alternative, first_alternative_score = w_alternatives[i]  # initial one!

                if (first_alternative[0] != w[0]):
                    if 'e' not in first_alternative:
                        break
                else:
                    counter += 1
                    
            if counter == len(w_alternatives):
                first_alternative, first_alternative_score = w_alternatives[0]
            else:   
                NewLoW += first_alternative + " "
    
    # you should change this so that it returns a new string (a new sentence),
    # NOT just print a list of words (that's what's provided in this starter code)
   
    NewLoW = NewLoW[:-1]
    
    NewLoW = textblob.TextBlob(NewLoW)
    NewLoW = NewLoW.correct()
    NewLoW = NewLoW.words
    
    NewSentence = ""
    
    for x in NewLoW:
        NewSentence += x + " "
    
    NewSentence = NewSentence[:-1]   
    
    return NewSentence


# 
# Once the above function is more sophisticated (it certainly does _not_ need to be
#   perfect -- that would be impossible...), then write a file-paraphrasing function:
#
def paraphrase_file(filename, model):
    """
    This will take in a file, and return a new file with the equivalent sentences in paraphrased sentences
    """
    n = open(filename)
    data= n.readlines()
    
    for x in data:
        f = open("test_paraphrased.txt", "w")
        f.write(paraphrase_sentence(x, model))
    
    f.close()
    n.close()