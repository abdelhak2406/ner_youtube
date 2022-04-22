#   NAMED ENTITY RECOGNITION SERIES   #
#            Lesson 07                #
# Creating Word Vectors in Gensim     #
#               with                  #
#        Dr. W.J.B. Mattingly         #

# TODO: watch the video 'how to generate custom word vectors in gensim'
# and add the necessary code in here.
import json
from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import  KeyedVectors
import multiprocessing


def training(model_name):
    # TODO: how does the hp.json file look like???
    with open("data/hp.json","r", encoding="utf-8") as f:
        texts = json.load(f)
    sentences = texts
    # here it's used for multiprocessing things
    # we can comemnt it if we don't wanna use it
    cores = multiprocessing.cpu_count()
    # workers is where we use cores so if you don't want to
    # just dont add that parameter
    w2v_model = Word2Vec(
            min_count=5,
            windows =2,
            size = 500,
            sample = 6e-5,
            alpha = ,
            min_alpha = ,
            negative = 20,
            workers = cores -1)
