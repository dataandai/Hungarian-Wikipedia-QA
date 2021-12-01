
import spacy

nlp = spacy.load("hu_core_ud_lg")


def recognize_entities(text):


    doc = nlp(text)   
        
    return doc

    #print(list(doc.sents))
