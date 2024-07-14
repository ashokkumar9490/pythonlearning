import { Component } from '@angular/core';

@Component({
  selector: 'app-friends',
  templateUrl: './friends.component.html',
  styleUrl: './friends.component.css'
})
export class FriendsComponent {
  friendnames = ["Santosh", "Ashok", "Naresh", "Koti", "Raghava", "Bhanu"];
  getColor(name: string): string {
    return name.startsWith('R') ? 'red' : name.startsWith('B') ? 'blue' : 'green';
  }

}

