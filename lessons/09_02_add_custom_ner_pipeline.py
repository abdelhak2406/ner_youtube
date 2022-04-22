#   NAMED ENTITY RECOGNITION SERIES   #
#            Lesson 09.02             #
#      Custom Labels (Holocaust)      #
#        Adding Labels to spaCy       #
#               with                  #
#        Dr. W.J.B. Mattingly         #

import spcay

# blank spacy Model
nlp = spacy.blank("en")

# create ner pipe (it knows that it's ner so
# it does some things in the background)
# if we want a custom class we will use someting else

ner = nlp.create_pipe("ner")

# this is going to create a new "pipe" named conc_camp_ner
# we can check the folder hollocost_ner and we will see a
# subfolder called conc_camp_neryou need to precise ner
nlp.add_pipe(ner,name="conc_camp_ner")
"""
if we go into the `meta.json` file we will see
in
```
    "pipeline":[
        "conc_camp_ner"
    ],
    "factories":{
        "conc_camp_ner":"ner"
    },
    "labels":{
        "conc_camp_ner":[

        ]
    }
```
- in factories the key of conc_camp_ner is ner , so
it can load all Named Entity Recongnition related classes and methods in
the background
- `labels`: each of our pipes that are Ner, are going to have a custom label
    if we add a new label the content will change.

"""
# if wa want to add a lew label we do:
ner.add_label("CONC_CAMP")




# the folder in which it will be saved
nlp.to_disk("hollocost_ner")
