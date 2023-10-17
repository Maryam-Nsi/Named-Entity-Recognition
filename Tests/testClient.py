import unittest
from client import entityClient
from testModel import testModel

class TestNerClient(unittest.TestCase):

    def testEmpty(self):
        model = testModel('eng')
        model.returnEntities([])
        ner = entityClient(model)
        ents = ner.getEntities("")
        self.assertIsInstance(ents, dict)

    def testNonEmpty(self):
        model = testModel('eng')
        model.returnEntities([])
        ner = entityClient(model)
        ents = ner.getEntities("Mary live in Iran")
        self.assertIsInstance(ents, dict)

    def testPerson(self):
        model = testModel('eng')
        doc_ents = [{'text': 'Mary', 'label_':'PERSON'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents': [{'ent': 'Mary', 'label': 'Person'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def testNORP(self):
        model = testModel('eng')
        doc_ents = [{'text': 'Chinese', 'label_':'NORP'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents': [{'ent': 'Chinese', 'label': 'Group'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def testLocation(self):
        model = testModel('eng')
        doc_ents = [{'text': 'the ocean', 'label_':'LOC'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents': [{'ent': 'the ocean', 'label': 'Location'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def testLangauge(self):
        model = testModel('eng')
        doc_ents = [{'text': 'English', 'label_':'LANGUAGE'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents': [{'ent': 'English', 'label': 'Language'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def testGPE(self):
        model = testModel('eng')
        doc_ents = [{'text': 'Iran', 'label_':'GPE'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents': [{'ent': 'Iran', 'label': 'Location'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])


    def testMultiple(self):
        model = testModel('eng')
        doc_ents = [{'text': 'Iran', 'label_':'GPE'},
                    {'text': 'Mary', 'label_':'PERSON'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents':
                [{'ent': 'Iran', 'label': 'Location'},
                 {'ent': 'Mary', 'label': 'Person'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])
