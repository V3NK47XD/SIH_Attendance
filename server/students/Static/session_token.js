import ipaddr from "./ip.js"

async function session(){
    const st = await fetch(`https://${ipaddr}:6969/sessioncheck`, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body : localStorage.getItem("session_key")
    });
    const ses = await st.text();
    return ses;
}

export { session }; 