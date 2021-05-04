#!/usr/bin/node

const r = require('request');

r.get(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    const computed = {};
    const todos = JSON.parse(body);
    todos.forEach(task => {
      if (!computed[task.userId]) computed[task.userId] = 0;
      computed[task.userId] += task.completed;
    });
    console.log(computed);
  }
});
