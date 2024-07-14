import { Component, OnInit } from '@angular/core';
import { MovieserviceService } from '../movieservice.service';
import { FormBuilder,Validators } from '@angular/forms';
import {Moviemod} from '../Models/moviemodel'
import { SharingService } from '../sharing.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-movie',
  templateUrl: './movie.component.html',
  styleUrl: './movie.component.css'
})


export class MovieComponent  implements OnInit{

  constructor(private mov:MovieserviceService,private formBuilder: FormBuilder,private service: SharingService,private router:Router){}

  movie:any;
  err:string = "";
   

  isLogged = false;
  loggedin$:any;

  ngOnInit(): void {
    this.getMovies(); 
    this.isLogged = this.service.isLoggedIn;
    this.loggedin$ = this.service.loggedin$ //subscribing here
  }
  
  getMovies(){

    this.mov.getMovies().then((data) => {
        this.movie = data;
        console.log(this.movie);
        
    })
    .catch((err) => {
      this.err = "Error fetching movie...check server";

    });   

  }

  profileForm = this.formBuilder.group({
    id: ['', Validators.required],
    rating: [''],
    name: ['', Validators.required],   
    desc: [''],
    image: ['']
  
  });

  onSubmit(){
    console.log('clicked');
    console.warn(this.profileForm.value);

      let id1 = (this.profileForm.value.id) || '';
      let name1 = (this.profileForm.value.name) || '';
      let rating1 = (this.profileForm.value.rating) || '';
      let desc1 = (this.profileForm.value.desc) || '';
      let image1 = this.profileForm.value.image || '';

      this.addMovie(new Moviemod(id1,rating1,name1,desc1,image1));
    
  }


  addMovie(mov1:Moviemod){

    this.mov.addMovie(mov1).then(() => {
      this.mov.getMovies()
    });

  }
  

}


