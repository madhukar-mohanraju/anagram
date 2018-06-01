'''
Created on 30-May-2018

@author: Madhukar
'''
import pytest
from anagram import getAnagram, app

@pytest.fixture(scope='module')
def client():
    flask_app = app
 
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
 
    yield client  # this is where the testing happens!
    ctx.pop()

def test_anagram(client):
    response = client.get('/anagram')
    assert response.status_code == 200
    assert b'Enter Anagram Input word' in response.data
    
def anagram_get(client, input_value):
    return client.get('/anagram?userinput='+input_value)

def test_anagram_with_input(client):
    response  = anagram_get(client, 'a')
    assert b'a' in response.data
    
    response  = anagram_get(client, 'ab')
    assert b'ab,ba' in response.data
    
def test_anagram_post(client):
    response = client.post('/anagram',data=dict(userinput='abc'))
    assert b'acb,abc,bca,cba,bac,cab' in response.data