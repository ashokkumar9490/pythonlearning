import { Component, Input } from '@angular/core';
import { MovieserviceService } from '../movieservice.service';
import jsPDF from 'jspdf';
import { TicketService } from '../ticket.service';

@Component({
  selector: 'app-ticket',
  templateUrl: './ticket.component.html',
  styleUrl: './ticket.component.css'
})
export class TicketComponent {
  numberOfTickets: any;
  totalprice: any;
  selectedDate:any;
  theater:any
 
  @Input() movieName: string = '1';
  @Input() dateTime: string ='1'
  @Input() seatNumber: string ='1'
 
   constructor(private mov: MovieserviceService,
              private ticketService: TicketService
   ) { }
  downloadTicketPdf(): void {
    this.mov.generateTicketPdf(this.movieName, this.dateTime, this.seatNumber);
  }
  ngOnInit(){
    this.ticketService.data$.subscribe(({NumberofTickets, totalprice, selectedDate, theater}) => {
      
      this.numberOfTickets = NumberofTickets;
      console.log(this.numberOfTickets);
      
      this.totalprice = totalprice;
      console.log(this.totalprice);
      this.selectedDate=selectedDate;
      this.theater=theater;
      
    });
}
}
