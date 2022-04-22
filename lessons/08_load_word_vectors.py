#   NAMED ENTITY RECOGNITION SERIES   #
#            Lesson 08                #
#   Loading Word Vectors into spaCy   #
#               with                  #
#        Dr. W.J.B. Mattingly         #

# TODO: write this part when watching the video
# "How to Load Custom Word Vectors into spaCy Models (Named Entity Recognition for DH 08)"
import spacy
import subprocess
import sys

model_name = "hp_model_test"
word_vectors = "word_vectors/word2vec_hp_ner_model_03.txt"
def load_word_vectors(model_name, word_vectors):
        subprocess.run([sys.executable,
        "-m",
        "spacy",
        "init-model",
        "en",
        model_name,
        "--vectors-loc",
        word_vectors
        ])
