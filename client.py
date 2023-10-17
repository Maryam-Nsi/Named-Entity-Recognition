import spacy

class entityClient:
    def __init__ (self , model):
        self.model = spacy.load(model)

    def getEntities(self , sentence):
        doc = self.model(sentence)
        entities = [{ 'ent': ent.text, 'label': self.map_label(ent.label_) } for ent in doc.ents]
        return { 'ents': entities, 'html': "" }