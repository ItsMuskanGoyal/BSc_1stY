const express = require('express');
const app = express();

app.get('/', (req,res)=>{
    res.setEncoding({"messgae":"hello world"})
})


app.get('/user/:num', (req, res))



app.get('/user', (req, res)=>{
    console.log(req.params)
    res.send(`${req.params.id} is a good girl`)

})


app.get("/add/:num1/:num2", (req, res)=> {
    var num1 = parseInt(req.parse.num1);
    var num2 = parseInt(req.parse.num2);

    res.send(`${num1+ num2}`)
})








app.listen(3000, ()=>{
    console.log('server is running at 3000')
})






