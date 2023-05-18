const http = require('http');
const express = require('express');
const ejs = require('ejs');
const bodyParser = require('body-parser');

// TODO: change hostname by checking actual IP
const hostname = '127.0.0.1';
const port = 3000;

const app = express();
app.use(bodyParser.json());
const server = http.createServer(app);

const {setOptionList, addVote, getResult} = require("./apiRequest.js");

var optionBody = {
    "1":"Option1",
    "2":"Option2",
    "3":"Option3",
    "4":"Option4",
    "5":"Option5"
};
async function setInitialState() {
    try {
        await setOptionList(optionBody); // wait to finish getResult
    } catch (error) {
      console.error('Error occured:', error);
    }
}
setInitialState();

app.set('view engine', 'ejs');
app.set('views', './views');
app.get('/', function(req, res) {
    res.render('index', function(err, html) {
        if(err) {
            console.log(err);
        }
        res.end(html);
    });
});

app.post('/userVote', (req, res) => {
    const userVote = req.body.vote;
    console.log(userVote);
    var votingBody = {
        "vote": userVote
    };
    addVote(votingBody)
    res.json({ message: 'Vote added successfully' });
  });

app.listen(port, hostname, () => {
	console.log(`Server running at http://${hostname}:${port}`);
});
