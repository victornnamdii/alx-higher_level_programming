#!/usr/local/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const taskCount = {};
    const allTasks = JSON.parse(body);
    for (const taskId in allTasks) {
      const task = allTasks[taskId];
      if (task.completed && taskCount[task.userId] === undefined) taskCount[task.userId] = 1;
      else if (task.completed) taskCount[task.userId] += 1;
    }
    console.log(taskCount);
  }
});
