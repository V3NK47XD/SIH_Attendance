import { session } from "./session_token.js";
import ipaddr from "./ip.js"

const ses_name = await session();
if (ses_name != "0") {
    window.location.href = "/middle";
}

const msg = document.getElementById("message");
const submit=document.getElementById("submit");

async function getStatus(){
    st = await fetch(`https://${ipaddr}:6969/status`);
    const status = await st.text();
    res.innerHTML = status;
}

async function send() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const lol = await fetch(`https://${ipaddr}:6969/loginbackend`, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body : JSON.stringify({'username': username, 'password': password})
    });
    const status = await lol.json();
    message.innerHTML = status.message;
    if (status.session_key != null) {
        localStorage.setItem("session_key", status.session_key);
        window.location.href = "/middle";
    }

}


submit.addEventListener("click", () => {
    send();
});