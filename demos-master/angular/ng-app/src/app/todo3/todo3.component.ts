import { Component } from '@angular/core';
import { TodoList } from './todoList';
import { TodoItem } from './todoItem';

@Component({
  selector: 'app-todo3',
  templateUrl: './todo3.component.html',
  styleUrl: './todo3.component.css',
})
export class Todo3Component {
  public list = new TodoList('Sharad', [
    new TodoItem('Go for run', true),
    new TodoItem('Get flowers'),
    new TodoItem('Collect tickets'),
  ]);

  get items(): readonly TodoItem[] {
    return this.list.todoItems.filter(
      (item) => this.showComplete || !item.complete
    );
  }

  showComplete: boolean = false;
}
