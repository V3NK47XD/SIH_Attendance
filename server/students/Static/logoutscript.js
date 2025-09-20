import ipaddr from "./ip.js"

const sessionKey = localStorage.getItem("session_key"); // get it first
fetch(`https://${ipaddr}:6969/logoutbackend`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({'session_key': sessionKey})
});
localStorage.removeItem("session_key"); // then remove it
