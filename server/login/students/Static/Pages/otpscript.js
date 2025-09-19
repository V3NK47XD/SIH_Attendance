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