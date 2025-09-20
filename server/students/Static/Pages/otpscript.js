import { session } from "../session_token.js";
import ipaddr from "../ip.js"
    const ses_name = await session();
    console.log("Session Name :", ses_name);

    if (ses_name == "0") {
        window.location.href = "/login";
    }
verify_class();

document.getElementById("submit").addEventListener("click", async () => {
    const otp = document.getElementById("otp").value;
    const sessionKey = localStorage.getItem("session_key");

    const response = await fetch(`https://${ipaddr}:7979/verify_otp`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'otp': otp})
    }); 
    const result = await response.json();
    if (result.message == "OTP is valid!") {
        window.location.href="/photos"
    }
    else{
        alert("Invalid OTP. Please try again.");
    }
});

async function verify_class(){
    const msg= document.getElementById("message");
    const subject = document.getElementById("subject");
    const classroom = document.getElementById("classroom");
    const you = document.getElementById("you");
    const class_valid = await fetch(`https://${ipaddr}:6969/verify_class`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'name':ses_name})
        }); 
        const class_result = await class_valid.json();
        console.log(class_result);
        const otp = document.getElementById("otp");
        const submit = document.getElementById("submit");
        if (class_result.expected_class == null) {
            otp.style.display = "none";
            submit.style.display = "none";
            msg.innerText = "No class is scheduled at this time.";

        }
        else if(class_result.expected_class == class_result.ip_class) {
            otp.style.display = "block";
            submit.style.display = "block";
            subject.innerHTML = `Subject now : ${class_result.current_subject}`
            classroom.innerHTML = `Classses Room : ${class_result.expected_class}`
            you.innerHTML = `You are in the Class : ${class_result.ip_class}`
            msg.innerText = "You are in the correct class. Go to Photo";
        }
        else {
            otp.style.display = "none";
            submit.style.display = "none";
            subject.innerHTML = `Subject now : ${class_result.current_subject}`
            classroom.innerHTML = `Classses Room : ${class_result.expected_class}`
            you.innerHTML = `You are in the Class : ${class_result.ip_class}`
            msg.innerText = "You are not in the correct class. Please go to the correct class to mark attendance.";
        }
}