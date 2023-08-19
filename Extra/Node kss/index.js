// BoilerPlate Code

//Import express
const express = require ('express');



// creating const function for express, any name  
// express is used for backend framework
// Cors is middleman 
const app = express();

//port opening
const port = 3000;



//Import cors
const cors = require('cors');
//Use it cors for origin which is localhost now 
app.use(cors({
    // This means allowing only local host
    //origin: 'https://localhost:5500'

    // This means allowing everyone
    origin:'*'
}))




// Anonyms Fat arrow function creation 
// listen is a method in app function
// This line will print when someone will listen this port
app.listen(3000, ()=>
{
    console.log("server run" )
})

//request by user, response by server
// '/' for home page

app.get('/', (req, res) =>{
    console.log(req)
    // res.send('Hello world');
    res.send({"message":"Hello World", "msg2":"Muskan"})
});

// app.get('/', (req, res)=> {
//     console.log(req)
//     res.send('user page')

// })




// Calculator 
// req is sum a and b
// converting string to int
// sending response

app.get('/sum/:a/:b', (req, res)=>{
    console.log(req.params)
    var num1 = parseInt(req.params.a);
    var num2 = parseInt(req.params.b);
    var sum= num1+ num2;
    res.send('Sum is :  '+ sum);
    console.log(sum);
})


app.get('/sub/:a/:b', (req, res)=>{
    console.log(req.params)
    var num1 = parseInt(req.params.a);
    var num2 = parseInt(req.params.b);
    var sub= num1- num2;
    res.send('Sub is :  '+ sum);
    console.log(sub);
})


app.get('/multi/:a/:b', (req, res)=>{
    console.log(req.params)
    var num1 = parseInt(req.params.a);
    var num2 = parseInt(req.params.b);
    var multi= num1+ num2;
    res.send('Multi is :  '+ multi);
    console.log(multi);
})


app.get('/div/:a/:b', (req, res)=>{
    console.log(req.params)
    var num1 = parseInt(req.params.a);
    var num2 = parseInt(req.params.b);
    var div= num1/ num2;
    res.send('Div is :  '+ div);
    console.log(div);
})

//params means parameters keyword
// a  b are var created by us
app.get('/calculate/:op/:a/:b', (req, res)=> {
    var op = req.params.op;
    
    var a = parseInt(req.params.a)
    var b = parseInt(req.params.b)

    if (op === 'sub'){
        // a and b are used a parameter not working
        //res.send("sub is :", a-b)
        res.send(`Sub is ${a-b}`)
    } else if (op=== 'mul'){
        res.send(`Sum is ${a*b}`)
    } else if (op=== 'div'){
        res.send(`Sub is ${a/b}`)
    } else if (op==='sum'){
        res.send(`Sub is ${a+b}`)
    } else{
        res.send("Wrong input")
    }

})









app.get('/cal/:op/:a/:b', (req, res)=> {
    var op = req.params.op;
    var a = parseInt(req.params.a)
    var b = parseInt(req.params.b)
    if (op === 'sub'){
        //This will not work due to parameter taking
        //res.send("sub is :", a-b)

        //Shorten the code
        //res.send(`Sub is ${a-b}`)

        // This is used to enter in json format
        res.send({'result':a-b})
    } else if (op=== 'multi'){
        res.send({'result':a*b})
    } else if (op=== 'div'){
        res.send({'result':a/b})
    } else if (op==='sum'){
        res.send({'result':a+b})
    } else{
        res.send("Wrong input")
    }

})















