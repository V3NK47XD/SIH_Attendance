import { session } from "./static/session_token.js";

    const ses_name = await session();
    console.log("Session Name :", ses_name);

    if (ses_name == "0") {
        window.location.href = "/login";
    }

document.getElementById("submit").addEventListener("click", async () => {
    const otp = document.getElementById("otp").value;
    const sessionKey = localStorage.getItem("session_key");
    const response = await fetch('http://localhost:7979/verify_otp', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'otp': otp})
    }); 
    const result = await response.json();
    document.getElementById("message").innerText = result.message;
});