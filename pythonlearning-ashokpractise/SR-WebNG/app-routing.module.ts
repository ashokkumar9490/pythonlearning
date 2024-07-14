import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
//import { TestComponent } from './test/test.component';
//import { NewsComponent } from './news/news.component';
import { LaptopComponent } from './laptop/laptop.component';
//import { HomeComponent } from './home/home.component';

const routes: Routes = [
  // { path: 'news', component: NewsComponent },
  { path: 'laptop', component: LaptopComponent },
  //{ path: 'Home', component: HomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
