import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProfileComponent } from './profile/profile.component';
import { StudSubjComponent } from './stud-subj/stud-subj.component';
import { LaptopsComponent } from './laptops/laptops.component';
import { ChartsComponent } from './charts/charts.component';
import { NgApexchartsModule } from 'ng-apexcharts';

@NgModule({
  declarations: [
    AppComponent,
    ProfileComponent,
    StudSubjComponent,
    LaptopsComponent,
    ChartsComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, NgApexchartsModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
