import { session } from "../session_token.js";

    const ses_name = await session();
    console.log("Session Name :", ses_name);

    if (ses_name == "0") {
        window.location.href = "/login";
    }

const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const snap = document.getElementById('snap');
    const context = canvas.getContext('2d');

    const saveBtn = document.getElementById('save');

    // Access webcam
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
      video.srcObject = stream;
    })
    .catch(err => {
      console.error("Error accessing webcam: ", err);
    });
    
    // Take picture
    snap.addEventListener('click', () => {
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
    });
    saveBtn.addEventListener('click', () => {
      // Convert canvas content to PNG base64
      const dataURL = canvas.toDataURL('image/png');
    
      send_url(ses_name,dataURL);
      
    });
    
    async function send_url(ses_name,dataURL) {
        console.log("url",dataURL);
        const response = await fetch('http://localhost:6969/photo_upload', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({'name': ses_name, 'image': dataURL})
        }); 
        const result = await response.json();
        const head = document.getElementById("result");
        head.innerText = "Result : " + result.message;
        console.log("Result :", result);
    }