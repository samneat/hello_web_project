# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
    
"""
When i send a request GET /wave?name=Dana
I expect the status code to be 200 ok
and response to be I am waving at Dana
"""
def test_get_wave_with_argument(web_client):
    response = web_client.get('/wave?name=Dana')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "I am waving at Dana"


"""
When i send a request POST
with arguments name = "Dana" and message "Hello"
expect status code to be 200 ok
reponse to be 'Thanks Dana, you sent this message: "Hello"'
"""
def test_post_submit_with_arguments(web_client):
    response = web_client.post('/submit', data={
        'name': 'Dana',
        'message': 'Hello'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'

#EXERCISE ONE
"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

#EXERCISE TWO
"""
When i send a request POST to /sort-names
with body parameters
i should get a 200 response and the names sorted
"""
def test_post_sort_names_wit_arguments(web_client):
    response = web_client.post('/sort-names', data={
        'names': 'Joe,Alice,Zoe,Julia,Kieran'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia,Kieran,Zoe"

#CHALLENGE
"""
When I send a request GET to /names
with name=Eddie,Leo as an argument 
status code should be 200
Eddie and Leo should be added to the list of names
names should be returned in alaphbetical order
"""
def test_get_names_with_argument(web_client):
    response = web_client.get('/names?name=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Eddie, Julia, Karim, Leo"
