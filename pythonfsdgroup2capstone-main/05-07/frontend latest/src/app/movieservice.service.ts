import { Injectable } from '@angular/core';
import { Moviemod } from './Models/moviemodel';
import jsPDF from 'jspdf';

@Injectable({
  providedIn: 'root'
})

export class MovieserviceService {

  constructor() { }  

  _url : string = 'http://localhost:3000/movies/' ;
  url1 :string = 'http://127.0.0.1:8000/api/movies/'
 

   
 

  // get all employees
  getMovies() {
    return fetch(this.url1).then((res) => res.json());
  }


  addMovie(mov:any){
    return fetch(this._url,{
      method : 'POST',
      headers : {
        'Content-Type' :'application/jason',
      },

      body :JSON.stringify(mov),
    });

  };


  clickedArticle : any = {}; 
  fav : any = [];

  setCLickedArticleObj(obj :any){
     this.clickedArticle  = obj;
  }
  
  getClickedArticle(){
     return this.clickedArticle;  
  }

  setFav(obj:any){
    this.fav.push(obj);
    
  }

  getFav(){
    return this.fav;
  }
  generateTicketPdf(movieName: string, dateTime: string, seatNumber: string): void {
    const doc = new jsPDF();
 
     
    doc.setFontSize(18);
    doc.text(`Ticket Details`, 20, 20);
 
    doc.setFontSize(12);
    doc.text(`Movie: ${movieName}`, 20, 30);
    doc.text(`Date & Time: ${dateTime}`, 20, 40);
    doc.text(`Seat Number: ${seatNumber}`, 20, 50);
 
     
    doc.save('ticket.pdf');
  }
  
 
  
}
