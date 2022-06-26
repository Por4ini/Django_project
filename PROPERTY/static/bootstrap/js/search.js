const input = document.getElementById("search");
const result = document.getElementById("results");

const fetchResult = value => {
    if(value) {
        const url = '/index/${value}/';
        fetch(url, {
            method: "GET"
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            console.log(data);
        })
        .catch(err => {
            console.log(err);
        })
    }
    else{
        console.log("no value");
    }
}

input.onkeyup = () => fetchResult(input.value);



