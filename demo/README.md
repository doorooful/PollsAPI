# Setup

## 1. Install Node.js

### Mac

`% brew install node`

### Windows

[Download from the official website](https://nodejs.org/en)

## 2. Verify

### Mac

- `% node`

### Windows

- `> node --version`

## 3. Initialize Node.js

### Mac

- `%cd demo/`
- `%npm init`
- `%npm install express`
- `%npm install ejs`
- `%npm install axios`

### Windows

- `> cd .\demo\`
- `> npm init`
- `> npm install express`
- `> npm install ejs`
- `> npm install axios`

## 4. Run server

### Mac

- `%cd demo/`
- `%node app.js`

### Windows

- `> cd .\demo\`
- `> node .\app.js`

## Sample usage to use apiRequest.js

```JavaScript

var optionBody = {
    "1":"yes",
    "2":"no"
};
var votingBody = {
    "vote":"Option1"
};

// Sample1.
// Setting Option List
setOptionList(optionBody);

// Sample2.
// Adding Vote and Get Result
async function performRequests() {
    try {
        await addVote(votingBody); // wait to finish addVote
        await getResult(); // wait to finish getResult
    } catch (error) {
      console.error('Error occured:', error);
    }
}
performRequests();

```
