import { Injectable } from '@angular/core';

import { Todo } from '../app/todo-json/todo';

@Injectable({
  providedIn: 'root',
})
export class TodoService {
  private todoList: Todo[] = [];
  private storageKey = 'todos';

  constructor() {
    this.loadTodos();
  }

  // Get all todos
  getTodos(): Todo[] {
    return this.todoList;
  }

  // Add a new todo
  addTodo(todo: Todo): void {
    this.todoList.push(todo);
    this.saveTodos();
  }

  // Update a todo
  updateTodo(todo: Todo): void {
    const index = this.todoList.findIndex((item) => item.title === todo.title);
    if (index !== -1) {
      this.todoList[index] = todo;
      this.saveTodos();
    }
  }

  // Delete a todo
  deleteTodo(title: string): void {
    const index = this.todoList.findIndex((item) => item.title === title);
    if (index !== -1) {
      this.todoList.splice(index, 1);
      this.saveTodos();
    }
  }

  // Load todos from local storage
  private loadTodos(): void {
    const storedTodos = localStorage.getItem(this.storageKey);
    if (storedTodos) {
      this.todoList = JSON.parse(storedTodos);
    }
  }

  // Save todos to local storage
  private saveTodos(): void {
    localStorage.setItem(this.storageKey, JSON.stringify(this.todoList));
  }
}
