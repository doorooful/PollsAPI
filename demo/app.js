const http = require('http');
const express = require('express');
const ejs = require('ejs');

const hostname = '127.0.0.1';
const port = 3000;

const app = express();
const server = http.createServer(app);

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

app.listen(port, hostname, () => {
	console.log(`Server running at http://${hostname}:${port}`);
});
