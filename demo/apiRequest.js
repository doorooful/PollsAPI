const axios = require('axios');

const apiUrl = "http://127.0.0.1:5000/"
const optionListUrl = "setOptionList"
const votingUrl = "voting"
const resultUrl = "result"

function setOptionList(optionBody){
    return new Promise((resolve, reject) => {
      console.log("body is " + optionBody);
      axios
        .post(apiUrl + optionListUrl, optionBody)
        .then(response => {
          console.log('POST requested to set optionList', response.data);
          resolve(response.data);
        })
        .catch(error => {
          console.error('POST request failed:', error);
          reject(error);
        });
    });
}

function addVote(voteBody) {
    return new Promise((resolve, reject) => {
      axios
        .post(apiUrl + votingUrl, voteBody)
        .then(response => {
          console.log('POST requested to add vote:', response.data);
          resolve(response.data);
        })
        .catch(error => {
          console.error('POST request failed:', error);
          reject(error);
        });
    });
}

function getResult() {
    return new Promise((resolve, reject) => {
      axios
        .get(apiUrl + resultUrl)
        .then(response => {
          console.log('GET request to get result:', response.data);
          resolve(response.data);
        })
        .catch(error => {
          console.error('GET request failed:', error);
          reject(error);
        });
    });
}

module.exports = {setOptionList, addVote, getResult};
