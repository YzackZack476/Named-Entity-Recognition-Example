import spacy
import string
import unicodedata
from spacy.lang.es import STOP_WORDS as ES_STOP_WORDS
# from spacy.lang.es.examples import sentences #Solo para testear con más ejemplos
# from nltk.corpus import stopwords


def get_entities(data_input):
    NER = spacy.load("es_core_news_sm")
    doc_array = tuple([NER(phrase) for phrase in data_input['oraciones']])

    def clean_token(token_phrase):
        token_phrase_noaccent = unicodedata.normalize("NFKD", token_phrase.text).encode("ASCII", "ignore").decode("utf-8")
        token_phrase_nopunctuation =  token_phrase_noaccent.translate(str.maketrans("", "", string.punctuation))
        return NER(token_phrase_nopunctuation)

    doc_array_cleaner = tuple([clean_token(token_prhase) for token_prhase in doc_array])

    doc_simple_array = tuple([" ".join([token.text for token in doc if token.text not in ES_STOP_WORDS]) for doc in doc_array_cleaner])
    doc_simple_array = tuple([NER(phrase) for phrase in doc_simple_array])

    result_dict = {
        "resultado":[
            
        ]
    }

    for phrase_org, token_phrase in zip(doc_array, doc_simple_array):
        entities = {}
        for word in token_phrase.ents:
            entities[word.text] = word.label_
        
        result_dict["resultado"].append({
            "oracion":phrase_org.text,
            "entidades":entities
        })
        
    return result_dict


