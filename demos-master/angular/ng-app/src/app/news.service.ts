import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class NewsService {
  _url: string =
    'https://newsapi.org/v2/top-headlines?country=in&apiKey=08eb952963d749fe8946821d7fbce565';

  constructor() {}

  getNews() {
    return fetch(this._url).then((res) => res.json());
  }
}
