import { Component, OnInit } from '@angular/core';
import { NewsService } from '../news.service';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrl: './news.component.css',
})
export class NewsComponent implements OnInit {
  newsdata: any[] = [];
  constructor(private newsService: NewsService) {}
  ngOnInit(): void {
    this.getNews();
  }

  getNews() {
    this.newsService.getNews().then((data) => {
      // console.log(data['articles']);
      this.newsdata = data['articles'];
    });
  }
}
