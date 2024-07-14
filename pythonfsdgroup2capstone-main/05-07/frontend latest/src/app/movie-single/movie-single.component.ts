import { Component, OnInit } from '@angular/core';
import { MovieserviceService } from '../movieservice.service';
import { FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { TicketService } from '../ticket.service';

@Component({
  selector: 'app-movie-single',
  templateUrl: './movie-single.component.html',
  styleUrl: './movie-single.component.css'
})

export class MovieSingleComponent implements OnInit{

  constructor(private router:Router,private mov :MovieserviceService,
              private ticketService:TicketService
  ){
    
  }

  numberOfTickets: Number = 0 ;
  selectedDate: Date = new Date();
    
  incomingArticleObject : any ;
  totalprice:number =0;
  fav :any =[];
  x1:any;

  theaters = ['Theater A', 'Theater B', 'Theater C'];  
  timeval = ['3 PM', '6 PM', '9 PM'];  

  theaterControl = new FormControl();  
  timeControl = new FormControl();  
  Price: number = 200;
  calculateTotal(): number {
    // return this.numberOfTickets * this.Price;
    this.totalprice=Number(this.numberOfTickets) * Number(this.Price);
    return this.totalprice;

}

  ngOnInit(): void {
    this.incomingArticleObject  = this.mov.getClickedArticle()
  console.log('name',this.incomingArticleObject.name);
  
  }

  onSubmit(){
    console.log('no ',this.numberOfTickets,' and date ', this.selectedDate,'theatre ',this.theaterControl.value);
   
      this.router.navigate(['/ticket'])
      this.sendMessage()
    }
  

  
  addFav(obj1:Object): any{
     
    this.mov.setFav(obj1)
    
  }  
  sendMessage() {
    this.ticketService.changeTicket(this.numberOfTickets,this.totalprice,this.selectedDate, this.theaterControl.value);
     // Clear input after sending
  }

}
 



