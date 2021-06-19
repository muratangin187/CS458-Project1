var Datastore = require('nedb');
const Result = require('./Result');
const User = require('./UserModel');

class DatabaseController{
    constructor(){
        this.db = new Datastore({ filename: 'users.db', autoload: true});
    }
    
    async insertUser(id, password, question, answer){
        return new Promise((resolve, reject)=>{
            this.db.insert({id, password, question, answer}, (err, doc)=>{
                if(err){
                    console.log(err);
                    resolve(new Result({error: err}));
                }else{
                    resolve(new Result({result: "Successfully inserted user."}));
                }
            });
        });
    }

    async getUser(id, password){
        return new Promise((resolve, reject)=>{
            this.db.findOne({id: parseInt(id), password}, (err, doc)=>{
                if(err){
                    console.log(err);
                    resolve(new Result({error: err}));
                }else{
                    if(doc){
                        let user = new User(doc.id, doc.name, doc.password, doc.question, doc.answer);
                        resolve(new Result({result: user}));
                    }else{
                        resolve(new Result({error: "Invalid password or ID"}));
                    }
                }
            });
        });
    }

    async getQuestion(id){
        return new Promise((resolve, reject)=>{
            this.db.findOne({id: parseInt(id)}, (err, doc)=>{
                if(err){
                    console.log(err);
                    resolve(new Result({error: err}));
                }else{
                    if(doc){
                        let user = new User(doc.id, doc.name, doc.password, doc.question, doc.answer);
                        resolve(new Result({result: user}));
                    }else{
                        resolve(new Result({error: "No student found with ID Number"}));
                    }
                }
            });
        });
    }

    async changePassword(id, newPassword){
        return new Promise((resolve, reject)=>{
            this.db.update({id},{$set: {password: newPassword}}, (err, n, _)=>{
                if(err){
                    console.log(err);
                    resolve(new Result({error: err}));
                }else{
                    resolve(new Result({result: n}));
                }
            });
        });
    }
}

module.exports = new DatabaseController();