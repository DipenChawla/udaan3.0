import json
from bert import Ner
import snoop
model = Ner('out_base/')


def convert_entities(entities):
    ents = set()
    w= ''
    for entity, next_entity in zip(entities, entities[1:] + [(".", "O")]):
        word, tag = entity
        if tag != "O":
            ent_position, ent_type = tag.split("-")
            if ent_position == "U":
                ents.add((word, ent_type))
            else:
                if ent_position == "B":
                    w = word
                elif ent_position == "I":
                    w += " " + word
                if next_entity[1].split("-")[0] != "I":
                    ents.add((w, ent_type))
    return ents

def get_store_results(text): 
    output = model.predict(text)
    for entity in convert_entities([(sin_put["word"], sin_put["tag"]) for sin_put in output]):
        if entity[1]=="ORG":
            yield entity[0]

def get_address_results(text):
    output = model.predict(text)
    for entity in convert_entities([(sin_put["word"], sin_put["tag"]) for sin_put in output]):
        if entity[1]=="LOC":
            yield entity[0]

