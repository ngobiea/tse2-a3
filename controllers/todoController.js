const Todo = require('../models/Todo');

exports.getTodos = async (req, res) => {
    try {
        const todos = await Todo.find();
        res.render('index', { todos });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};

exports.addTodo = async (req, res) => {
    const todo = new Todo({
        task: req.body.task
    });

    try {
        await todo.save();
        res.redirect('/');
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
};

exports.completeTodo = async (req, res) => {
    try {
        const todo = await Todo.findById(req.params.id);
        todo.completed = !todo.completed;
        await todo.save();
        res.redirect('/');
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
};
