const express=require('express');
const path=require('path');
const indexRouter=require('./routes/index');
const usersRouter=require('./routes/users');
const app=express();

app.use(express.urlencoded({extended:false}));

// Routes
app.use('/', indexRouter);
app.use("/users", usersRouter);

app.listen(3000);

(error="") =>
{
    console.log(`Oops! Something went wrong: ${error}`);
    return 0;
};

module.exports = app;
