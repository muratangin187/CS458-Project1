// GLOBALS
let id = "";
let password = "";
let passwordAgain = "";
let captcha = "";
let answer = "";


let forgetState = 0;

let currentCaptcha = captchaGenerate();

function captchaGenerate() {
    let chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz'.split('');
    let length = 7;
    let str = '';
    for (var i = 0; i < length; i++) {
    str += chars[Math.floor(Math.random() * chars.length)];
    }
    return str;
}

function handleID(value){
    id = value;
}

function handlePassword(value){
    password = value;
}

function handleAgainPassword(value){
    passwordAgain = value;
}

function handleAnswer(value){
    answer = value;
}

function handleCaptcha(value){
    captcha = value;
}

function showMessage(string, isAlert){
    if(isAlert)
        document.getElementById("alertBox").setAttribute("class","alert alert-danger");
    else
        document.getElementById("alertBox").setAttribute("class","alert alert-success");
    document.getElementById("alertBox").style.display = "block";
    document.getElementById("alertBox").innerText = string;
}

function hideMessage(){
    document.getElementById("alertBox").style.display = "none";
}

async function login(){
    captchaCount = parseInt(window.localStorage.getItem("captchaCount")??0);
    console.log("Captcha count: " + captchaCount);
    captchaTime = parseInt(window.localStorage.getItem("captchaTime")??Date.now());
    console.log("Captcha time: " + new Date(parseInt(captchaTime)).toLocaleTimeString());
    if(captchaCount > 5){
        if(captchaTime + 60*1000 < Date.now()){
            window.localStorage.setItem("captchaCount", 0);
            window.localStorage.setItem("captchaTime", Date.now());
        }else{
            showMessage("Please try again later (Too many attempt)", true);
            return;
        }
    }
    if(currentCaptcha != captcha){
        showMessage("Please enter correct captcha!", true);
        if(captchaTime + 60*1000 < Date.now()){
            window.localStorage.setItem("captchaCount", 1);
            window.localStorage.setItem("captchaTime", Date.now());
        }else{
            captchaCount++;
            window.localStorage.setItem("captchaCount", captchaCount);
            window.localStorage.setItem("captchaTime", Date.now());
        }
    }else{
        try{
            let response = await axios.post("http://localhost:3000/api/login", {
                id: id,
                password: password
            });
            showMessage("Welcome to STARS " + response.data.result.name, false);
            window.localStorage.setItem('username', response.data.result.name)
            window.localStorage.setItem('idNumber', response.data.result.id)
            setTimeout(()=> document.location.href="/auth.html", 1500);
        }catch(error){
            showMessage(error.response.data.error, true);
        }
    }
}

function logout(){
    window.localStorage.removeItem('username');
    window.localStorage.removeItem('idNumber');
    document.location.href="/";
}

let canvas = document.getElementById("myCanvas");
if(canvas){
    let ctx = canvas.getContext("2d");
    ctx.font = "30px Arial";
    ctx.strokeText(currentCaptcha,10,30);
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(300, 150);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(200, 150);
    ctx.stroke();
}

let forgetButton = document.getElementById("forgetButton");
let hiddenInputs = document.getElementById("hide");
let questionInput = document.getElementById("questionText");
let idInput = document.getElementById("idNumber");
if(forgetButton) 
forgetButton.addEventListener("click", async (_)=>{
    if(forgetState == 0){
        hideMessage();
        if(id == "" || id == null){
            showMessage("Please enter your id", true);
            return;
        } 
        try{
        let response = await axios.post("http://localhost:3000/api/question", {
            id: id
        });
        hiddenInputs.style.display = "block";
        questionInput.placeholder = response.data.result;
        forgetButton.setAttribute("class", "btn btn-danger");
        forgetButton.innerText = "Reset password";
        idNumber.setAttribute("disabled", "true");
        forgetState = 1;
        }catch(err){
            showMessage(err.response.data.error, true);
            return;
        }
    }else{
        hideMessage();
        if(id == "" || id == null || answer == "" || answer == null || password == "" || password == null || passwordAgain == "" || passwordAgain == null){
            showMessage("Please fill all the fields", true);
            return;
        } 
        if(passwordAgain != password){
            showMessage("You need to write same password twice", true);
            return;
        }
        try{
        let response = await axios.post("http://localhost:3000/api/resetPassword", {
            id: id,
            password: password,
            answer: answer,
        });
        showMessage(response.data.result, false);
        window.localStorage.removeItem('username');
        window.localStorage.removeItem('idNumber');
        setTimeout(()=> document.location.href="/", 1500);
        }catch(err){
            showMessage(err.response.data.error, true);
            return;
        }
    }
});