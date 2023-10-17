class entityClient:
    def __init__(self, model, displacy):
        self.model = model
        self.displacy = displacy

    def getEntities(self, sentence):
        doc = self.model(sentence)
        html = self.displacy.render(doc, style="ent")
        entities = [{ 'ent': ent.text, 'label': self.map_label(ent.label_) } for ent in doc.ents]
        return { 'ents': entities, 'html': html }

    @staticmethod
    def mapping(label):
        labeling = {
            'PERSON'  : 'Person',
            'NORP'    : 'Group',
            'LOC'     : 'Location',
            'GPE'     : 'Location',
            'LANGUAGE': 'Language'
        }

        return labeling.get(label)
