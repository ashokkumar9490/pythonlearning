import { Injectable } from '@angular/core';
import { ReplaySubject } from 'rxjs';
import { Lap } from './Models/laptop';

@Injectable({
  providedIn: 'root',
})
export class LaptopService {
  _url: string = 'http://localhost:3000/laps'; //server url where data exists(db.json file under server)

  private favCount = new ReplaySubject<number>(0); //create to store fav count
  favCount$ = this.favCount.asObservable(); //use in fav

  laps: Lap[] = []; //for delete, storing data in array

  constructor() {}

  // write all fetch methods here
  // get all laptops
  //to get data from server
  getLaps() {
    return fetch(this._url).then((res) => res.json());
  }

  //to add/post new laptop data to server
  addLaps(lap: any) {
    return fetch(this._url, {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
      },
      body: JSON.stringify(lap),
    });
  }

  //to delete LAPTOP from server
  delLap(lap: Lap) {
    return fetch(this._url + lap.id, {
      method: 'DELETE',
    }).then((res) => res.json());
  }
}
