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
    const lol = await fetch('/registerbackend', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body : JSON.stringify({'username': username, 'password': password})
    });

    const status = await lol.text();
    msg.innerHTML = status;

}

submit.addEventListener("click", () => {
    send();
});