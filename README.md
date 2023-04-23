# PollsAPI

## <Overview>
<!-- TODO: Write up description of the application -->
  

## <Prerequisites>
### How to set up Flask server?
1. Create virtual environment under /PollsAPI:  
    - mac: `% python3 -m venv .venv`
    - windows: `python -m venv .venv`
2. Activate virtual environment:  
    - mac: `% source .venv/bin/activate`
    - windows: `.\.venv\Scripts\activate`
3. Upgrade Pip:  
    - mac: `(.venv) % pip install --upgrade pip`
    - windows: `python -m pip install --upgrade pip`
4. Install pi-heaan library: 
     - mac: `(.venv) % pip install pi-heaan`
     - windows: `(.venv) pip install pi-heaan` 
5. Install Flask package:  
    - mac: `(.venv) % pip install Flask`
    - windows: `(.venv) pip install -U Flask`
6. (Option) Verify Flask package:  
    - `(.venv) % flask --version`
    - `(.venv) pip show Flask`
7. Run server:  
`(.venv) % python app.py`
access server from, http://127.0.0.1:5000/{endpoint_URL}

### How to set up pyheaan environment?
<!-- TODO: Write up docs -->

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