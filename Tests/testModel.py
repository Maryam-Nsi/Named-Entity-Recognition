class testModel():
    def __init__(self , model):
        self.model = model
    
    def __call__(self, send):
        return testDoc(send , self.ents)
    
    def returnEntities (self , ents):
        self.ents = ents

class testDoc():
    def __init__(self , ents):
        self.ents = [testSpan(ent['text'], ent['label_']) for ent in ents]

    def patch_func(self, attr, value):
        def patched(): return value
        setattr(self, attr, patched)
        return self

class testSpan():
    def __init__(self , text , label):
        self.text = text
        self.label_ = label