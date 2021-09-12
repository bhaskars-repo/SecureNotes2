//
// @Author: Bhaskar S
// @Blog:   https://www.polarsparc.com
// @Date:   01 Sep 2021
//

const config = {
    headers: {  
        'content-type': 'application/json'
    }
};

function clearSignup() {
    if (document.getElementById('email').value.length > 0)
        document.getElementById('email-err').innerText = "";
    if (document.getElementById('password1').value.length > 0)
        document.getElementById('pass1-err').innerText = "";
    if (document.getElementById('password2').value.length > 0)
        document.getElementById('pass2-err').innerText = "";
}

function mySignup() {
    const url = 'http://127.0.0.1:8080/signup';
    var data = {
        email: document.getElementById('email').value,
        password1: document.getElementById('password1').value,
        password2: document.getElementById('password2').value
    };
    axios.post(url, data, config)
        .then(
            (response) => {
                location.replace('http://127.0.0.1:8080/login');
        })
        .catch((error) => {
            if (error.response) {
                // Got an error response
                if (error.response.data.code == 1001) {
                    document.getElementById('email-err').innerText = error.response.data.error;
                } else if (error.response.data.code == 1002) {
                    document.getElementById('pass1-err').innerText = error.response.data.error;
                } else {
                    document.getElementById('pass2-err').innerText = error.response.data.error;
                }
            }
        });
}

function clearLogin() {
    if (document.getElementById('email').value.length > 0)
        document.getElementById('email-err').innerText = "";
    if (document.getElementById('password1').value.length > 0)
        document.getElementById('pass-err').innerText = "";
}

function myLogin() {
    const url = 'http://127.0.0.1:8080/login';
    var data = {
        email: document.getElementById('email').value,
        password: document.getElementById('password').value
    };
    axios.post(url, data, config)
        .then(
            (response) => {
                location.replace('http://127.0.0.1:8080/secure');
        })
        .catch((error) => {
            if (error.response) {
                // Got an error response
                if (error.response.data.code == 1004) {
                    document.getElementById('email-err').innerText = error.response.data.error;
                } else {
                    document.getElementById('pass-err').innerText = error.response.data.error;
                }
            }
        });
}
