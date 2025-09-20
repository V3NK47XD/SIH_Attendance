import { session } from "../session_token.js";

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
    const msg= document.getElementById("message");
    const result = await response.json();
    if (result.message == "OTP is valid!") {
        const class_valid = await fetch('/verify_class', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'name':ses_name})
        }); 
        const class_result = await class_valid.json();
        console.log(class_result);
        if (class_result.expected_class == null) {
            msg.innerText = "No class is scheduled at this time.";
            document.getElementById("photo").style.display = "none";
        }
        else if(class_result.expected_class == class_result.ip_class) {
            msg.innerText = "You are in the correct class. Go to :";
            document.getElementById("photo").style.display = "block";
        }
        else {
            msg.innerText = "You are not in the correct class. Please go to the correct class to mark attendance.";
        }
    }
    else{
        alert("Invalid OTP. Please try again.");
    }
});