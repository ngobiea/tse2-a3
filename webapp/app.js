const express = require('express');
const mongoose = require('mongoose');


const bodyParser = require('body-parser');
const todoController = require('./controllers/todoController');

const app = express();

app.set('view engine', 'ejs');
app.set('views', 'views');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('./public'));


app.get('/', todoController.getTodos);
app.post('/add', todoController.addTodo);
app.get('/complete/:id', todoController.completeTodo);

// Connect to MongoDB
mongoose.connect(
  `mongodb://${process.env.MONGODB_USERNAME}:${process.env.MONGODB_PASSWORD}@mongodb:27017/`,
  {
    dbName: 'todo-app'
  }).then(() => {
    app.listen(80, () => {
      console.log('Server started on port 80');
    });
  }).catch((err) => {
    console.log(err);
  });


