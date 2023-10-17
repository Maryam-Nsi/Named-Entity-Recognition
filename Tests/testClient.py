import unittest
from client import entityClient
from testModel import testModel


class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = testModel('eng')
        model.returnEntities([])
        ner = entityClient(model)
        ents = ner.getEntities("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = testModel('eng')
        model.returnEntities([])
        ner = entityClient(model)
        ents = ner.getEntities("Madison is a city in Wisconsin")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = testModel('eng')
        doc_ents = [{'text': 'Laurent Fressinet', 'label_':'PERSON'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents': [{'ent': 'Laurent Fressinet', 'label': 'Person'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = testModel('eng')
        doc_ents = [{'text': 'Lithuanian', 'label_':'NORP'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents': [{'ent': 'Lithuanian', 'label': 'Group'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = testModel('eng')
        doc_ents = [{'text': 'the ocean', 'label_':'LOC'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents': [{'ent': 'the ocean', 'label': 'Location'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Langauge(self):
        model = testModel('eng')
        doc_ents = [{'text': 'ASL', 'label_':'LANGUAGE'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents': [{'ent': 'ASL', 'label': 'Language'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        model = testModel('eng')
        doc_ents = [{'text': 'Australia', 'label_':'GPE'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents': [{'ent': 'Australia', 'label': 'Location'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])


    def test_get_ents_given_multiple_ents_serializes_all(self):
        model = testModel('eng')
        doc_ents = [{'text': 'Australia', 'label_':'GPE'},
                    {'text': 'Judith Polgar', 'label_':'PERSON'}]
        model.returnEntities(doc_ents)
        ner = entityClient(model)
        result = ner.getEntities('...')
        expected_result = { 'ents':
                [{'ent': 'Australia', 'label': 'Location'},
                 {'ent': 'Judith Polgar', 'label': 'Person'}], 'html': "" }
        self.assertListEqual(result['ents'], expected_result['ents'])
