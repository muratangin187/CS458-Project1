module.exports = class User{
    constructor(id, name, password, secretQuestion, secretAnswer){
        this.id = id;
        this.name = name;
        this.password = password;
        this.secretQuestion = secretQuestion;
        this.secretAnswer = secretAnswer;
    }

    getQuestion(){return this.secretQuestion};

    checkAnswer(answer){return answer == this.secretAnswer};
}