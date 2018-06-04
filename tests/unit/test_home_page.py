'''
Created on 30-May-2018

@author: Madhukar
'''
import pytest
from anagram import app

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

def test_home_page(client):
    response = client.get('/')
    #print(response)
    assert response.status_code == 200
    assert b'Hello Everyone!!!' in response.data
    
def test_invalid_page(client):
    response = client.get('/random')
    assert response.status_code == 404

def home_page_with_user(client, name):
    return client.get('/?name='+name)

    
def test_home_page_with_user(client):
    
    response  = home_page_with_user(client, 'Madhukar')
    assert b'Hello Mr. Madhukar' in response.data    
    
    response  = home_page_with_user(client, 'Jeff Bezoz')
    assert b'Hello Mr. Jeff Bezoz' in response.data
    
    response  = home_page_with_user(client, 'Mark Elliot Zuckerberg')
    assert b'Hello Mr. Mark Elliot Zuckerberg' in response.data
