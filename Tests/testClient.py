import unittest
from client import entityClient
from testModel import testModel

class testClient(unittest.TestCase):
    def emptyInputString(self):
        model = testModel("eng")
        model.returnEntities([])
        ner = entityClient(model)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = testModel('eng')
        doc_ents = [{'text': 'Laurent Fressinet', 'label_':'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = testClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Laurent Fressinet', 'label': 'Person'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])