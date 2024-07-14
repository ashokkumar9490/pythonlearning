import { Component } from '@angular/core';

@Component({
  selector: 'app-lightswitch',
  standalone: true,
  imports: [],
  templateUrl: './lightswitch.component.html',
  styleUrl: './lightswitch.component.css',
})
export class LightswitchComponent {
  isOn = false;
  clicked() {
    this.isOn = !this.isOn;
  }
  get message() {
    return `The light is ${this.isOn ? 'On' : 'Off'}`;
  }
}
