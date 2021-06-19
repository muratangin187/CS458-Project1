module.exports = class Result{
    constructor(data){
        this.result = data.result??null;
        this.error = data.error??null;
    }
    
    isError(){return this.error != null;}

    getResult(){return this.result;}

}