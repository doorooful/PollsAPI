# PollsAPI

Poll API to calculate data using pyheaan(which supports homomorphic encryption).
This API mainly provides **voting**, **setting options**, **getting results**.

## <Overview>

### API Documentation

| URL            | Method | Request Body              | Response                        |
| -------------- | ------ | ------------------------- | ------------------------------- |
| /voting        | POST   | { "vote": "Option1" }     | "voted!"                        |
| /setOptionList | POST   | { "1": "yes", "2": "no" } | Given options are ["yes", "no"] |
| /result        | GET    |                           | { "yes": 2, "no": 0}            |

### Description

**Relevance of Online Voting**  
Voting is an essential part of democracy.  
Currently voting is done with paper, either in a voting booth or by post.  
That is rather cost intensive and harmful for the environment.  
Furthermore, the involvment of people bears risks.  
In countries like the US people have come to distrust the traditional voting system in recent years.  
Therefore, online voting seems like an attracktive option to consider.

**Homomorphic Encryption in Online Voting**  
The votes from local districts need to be transferred to a central databse, so that the overall result can be calculated.  
This transferred data is very sensitive.  
First of all, we need to protect the information of who voted for whom (data collected to ensure people can‘t vote more than once).  
Second of all, we need to protect the final voting results, so that they are not leaked prematurely (since that could influence the election).  
With homomorphic encryption we can encrypt this data before transferring votes to a central database of the country.  
Therefore even if data leakage occurs, confidentility can be assured.

## <Prerequisites>

### How to set up Flask server?

1. Create virtual environment under /PollsAPI:
   - mac: `% python3 -m venv .venv`
   - windows: `> python -m venv .venv`
2. Activate virtual environment:
   - mac: `% source .venv/bin/activate`
   - windows: `> .\.venv\Scripts\activate`
3. Upgrade Pip:
   - mac: `(.venv) % pip install --upgrade pip`
   - windows: `> python -m pip install --upgrade pip`
4. Install pi-heaan library:
   - mac: `(.venv) % pip install pi-heaan`
   - windows: `(.venv) > pip install pi-heaan`
5. Install Flask package:
   - mac: `(.venv) % pip install Flask`
   - windows: `(.venv) > pip install -U Flask`
6. (Option) Verify Flask package:
   - `(.venv) % flask --version`
   - `(.venv) > pip show Flask`
7. Run server:  
   `(.venv) % python app.py`
   access server from, http://127.0.0.1:5000/{endpoint_URL}

## <API Usages>

### How to send request to API?

1. (Option) Install postman application:
   - Link: https://www.postman.com/downloads/
2. Run server:
   - `% source .venv/bin/activate`
   - `(.venv) % python app.py`
3. Send POST request to `http://127.0.0.1/voting` with sample body
   (Available options are Option1, Option2, Option3 initially)
   ```json
   {
     "vote": "Option1"
   }
   ```

### How to change Option name?

1. Change setOption = ["Option1", "Option2", "Option3"] to setOption = ["apple", "banana", "cookie","drinks"]
   - any number of options, and any characters can be used.
2. User must send option name in POST request to a character that include in setOption.
   ```json
   {
     "1": "apple",
     "2": "banana",
     "3": "cookie",
     "4": "drinks"
   }
   ```
   <img width="1256" alt="KakaoTalk_20230423_161859583" src="https://user-images.githubusercontent.com/117963984/233825820-7c691cdb-da63-4b84-b0e2-e8fe198559f0.png">

### How to get results?

- Send GET request to `http://127.0.0.1/result`
