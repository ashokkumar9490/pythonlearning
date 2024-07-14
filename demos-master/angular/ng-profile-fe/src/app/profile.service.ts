import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ProfileService {
  loginUrl = 'http://127.0.0.1:8000/api/login/';

  // create fetch method for passing name and password to the backend
  // and get the token back
  fetchToken(name: string, password: string) {
    return fetch(this.loginUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: name,
        password: password,
      }),
    }).then((response) => response.json());
  }

  // create method to pass token to the backend and get profile data back
  fetchProfile(token: string) {
    return fetch('http://127.0.0.1:8000/api/profile/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
    }).then((response) => response.json());
  }

  constructor() {}
}
