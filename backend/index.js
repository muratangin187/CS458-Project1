const express = require('express')
const app = express()
app.use(express.json());

const port = 3000
const DatabaseController = require("./DatabaseController");

//DatabaseController.insertUser(21702962, "123", "Secret Question?", "Secret Answer.");

app.use(express.static('../frontend'))

app.get('/', (req, res) => {
  res.sendFile("index.html")
})

app.get('/login', (req, res) => {
  res.sendFile("index.html")
})

app.get('/reset', (req, res) => {
  res.sendFile("reset.html")
})

app.get('/auth', (req, res) => {
  res.sendFile("auth.html");
})

app.post('/api/resetPassword', async (req, res) => {
    let response = await DatabaseController.getQuestion(req.body.id);
    if(response.isError()){
        res.status(400);
        console.log(response.error);
        res.json({
            error: response.error
        });
    }else{
        if(response.result.checkAnswer(req.body.answer)){
            let response2 = await DatabaseController.changePassword(parseInt(req.body.id), req.body.password);
            if(response2.isError()){
                res.status(400);
                console.log(response2.error);
                res.json({
                    error: response2.error
                });
            }else{
                res.status(200);
                res.json({
                    result: "You changed your password successfully, please login now"
                });
            }
        }else{
            res.status(400);
            console.log(response.error);
            res.json({
                error: "The answer of the secret question is false"
            });
        }
    }
})

app.post('/api/question', async (req, res) => {
    let response = await DatabaseController.getQuestion(req.body.id);
    if(response.isError()){
        res.status(400);
        console.log(response.error);
        res.json({
            error: response.error
        });
    }else{
        res.status(200);
        res.json({
            result: response.result.getQuestion()
        });
    }
})

app.post('/api/login', async (req, res) => {
    console.log("ID: " + req.body.id);
    if(req.body.id == "" || req.body.password == ""){
        res.status(400);
        res.json({
            error: "Please fill ID and password fields"
        });
        return;
    }
    let response = await DatabaseController.getUser(req.body.id, req.body.password);
    if(response.isError()){
        res.status(400);
        console.log(response.error);
        res.json({
            error: response.error
        });
    }else{
        res.status(200);
        res.json({
            result: response.result
        });
    }
})

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`)
})