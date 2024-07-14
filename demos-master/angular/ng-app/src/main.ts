/// <reference types="@angular/localize" />

import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';

platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch((err) => console.error(err));

//---------------------------------------------------
//import { Observable, Observer, Subject, of, throwError } from 'rxjs';

//---------------------------------------------------
// const observable = new Observable((subscriber) => {
//   subscriber.next(1);
//   subscriber.next(2);
//   subscriber.next(3);
//   subscriber.complete();
// });
// const observer1 = {
//   next: (x: any) => console.log('Observer1 got a next value: ' + x),
//   error: (err: any) => console.error('Observer got an error: ' + err),
//   complete: () => console.log('Observer1 got a complete notification'),
// };
// const observer2 = {
//   next: (x: any) => console.log('Observer2 got a next value: ' + x),
//   error: (err: any) => console.error('Observer got an error: ' + err),
//   complete: () => console.log('Observer2 got a complete notification'),
// };
// observable.subscribe(observer1);
// observable.subscribe(observer2);
//---------------------------------------------------
// const subject = new Subject<number>();

// subject.subscribe({
//   next: (v) => console.log(`observerA: ${v}`),
// });
// subject.subscribe({
//   next: (v) => console.log(`observerB: ${v}`),
// });

// subject.next(1);
// subject.next(2);

// Logs:
// observerA: 1
// observerB: 1
// observerA: 2
// observerB: 2

//---------------------------------------------------
// const numbers$ = of(
//   1,
//   2,

//   throwError(() => new Error('Invalid')),
//   3
// );
// numbers$.subscribe({
//   next: (value) => console.log('Observable emitted the next value: ' + value),
//   error: (err) => console.error('Observable emitted an error: ' + err),
//   complete: () => console.log('Observable emitted the complete notification'),
// });
//---------------------------------------------------
// function recieveEvents(observable: Observable<string>) {
//   observable.subscribe({
//     next: (str) => {
//       console.log(`Event received: ${str}`);
//     },
//     complete: () => console.log('Sequence ended'),
//   });
// }
// function sendEvents(observer: Observer<string>) {
//   let count = 5;
//   for (let i = 0; i < count; i++) {
//     observer.next(`${i + 1} of ${count}`);
//   }
//   observer.complete();
// }

// let subject = new Subject<string>();
// let subject2 = new Subject<string>();
// recieveEvents(subject);
// recieveEvents(subject2);
// sendEvents(subject);
// sendEvents(subject2);
