# PollsAPI

## <Overview>
<!-- TODO: Write up description of the application -->
  
    

## <Prerequisites>
### How to set up Flask server?
1. Create virtual environment under /PollsAPI:  
`% python3 -m venv .venv`  
2. Activate virtual environment:  
    - mac: `% source .venv/bin/activate`
    - windows: 
3. Upgrade Pip:  
`(.venv) % pip install --upgrade pip`
4. Install Flask package:  
`(.venv) % pip install Flask`
5. (Option) Verify Flask package:  
`(.venv) % flask --version`
6. Run server:  
`(.venv) % python app.py`
access server from, http://127.0.0.1:5000/{endpoint_URL}

### How to send request to API?
1. (Option) Install postman application:
    - Link: https://www.postman.com/downloads/
2. Run server:
    - `% source .venv/bin/activate`
    - `(.venv) % python app.py`
3. Send POST request to `http://127.0.0.1/voting` with sample body
    ``` json
    {
        "sender": "Evi",
        "vote": "Option1"
    }
    ```