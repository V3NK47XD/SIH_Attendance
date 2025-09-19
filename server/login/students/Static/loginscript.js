const msg = document.getElementById("message");

const submit=document.getElementById("submit");

async function getStatus(){
    st = await fetch('/status');
    const status = await st.text();
    res.innerHTML = status;
}

async function send() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const lol = await fetch('/loginbackend', {
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
        window.location.href = "/otp";
    }

}

submit.addEventListener("click", () => {
    send();
});