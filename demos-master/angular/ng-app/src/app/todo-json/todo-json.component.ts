import { Component, OnInit } from '@angular/core';
import { TodoService } from '../todo.service';
import { Todo } from './todo';

@Component({
  selector: 'app-todo-json',
  templateUrl: './todo-json.component.html',
  styleUrl: './todo-json.component.css',
})
export class TodoJsonComponent implements OnInit {
  newTodoTitle: string = '';
  todos: Todo[] = [];

  constructor(private todoListService: TodoService) {}

  ngOnInit(): void {
    this.todos = this.todoListService.getTodos();
  }

  addTodo(): void {
    if (this.newTodoTitle.trim()) {
      const newTodo: Todo = { title: this.newTodoTitle, completed: false };
      this.todoListService.addTodo(newTodo);
      this.todos = this.todoListService.getTodos();
      this.newTodoTitle = '';
    }
  }

  updateTodo(todo: Todo): void {
    this.todoListService.updateTodo(todo);
  }

  deleteTodo(title: string): void {
    this.todoListService.deleteTodo(title);
    this.todos = this.todoListService.getTodos();
  }
}
