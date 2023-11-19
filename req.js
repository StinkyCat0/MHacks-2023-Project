//creates a request to get user data
//returns a promise
//takes in a url and a method
//method is defaulted to GET
//if method is POST, it will take in a body
//body is defaulted to null

const req = (url, method = 'GET', body = null) => {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(method, url);
        xhr.onload = () => {
        if (xhr.status >= 200 && xhr.status < 300) {
            resolve(xhr.response);
        } else {
            reject(xhr.statusText);
        }
        };
        xhr.onerror = () => reject(xhr.statusText);
        xhr.send(body);
    });
    }