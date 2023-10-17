import unittest
import json
from flask import request
from app import app

class TestApi(unittest.TestCase):

    def testJsonBody(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Mary live in Iran."})
            assert response._status_code == 200

    def testKnownEntities(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Mary"})
            data = json.loads(response.get_data())
            print(data)
            assert data['entities'][0]['ent'] == 'Mary'
            assert data['entities'][0]['label'] == 'Person'
