let toDoList = []
function addTask(task, dueDate) {
    toDoList.push({ task: task, dueDate: new Date(dueDate) });
}
function displayList() {
    console.log("To-Do List:\n");
    toDoList.forEach((item, index) => {
        let formattedDate = item.dueDate.toISOString().slice(0, 10);
        let status = "";
        if (item.dueDate < new Date()) {
            status = "**(Overdue: " + formattedDate + ")**";
        } else {
            status = "(Due: " + formattedDate + ")";
        }
        console.log((index + 1) + ". " + item.task + " " + status);
    });
    console.log("\n");
}
function markComplete(taskIndex) {
    if (taskIndex >= 0 && taskIndex < toDoList.length) {
        toDoList.splice(taskIndex, 1);
    } else {
        console.log("Invalid task index.");
    }
}

addTask("Buy Groceries", "2024-05-25");
addTask("Finish Project Report", "2024-05-20"); 
addTask("Clean the House", "2024-05-23");

displayList();
markComplete(1);
displayList();
