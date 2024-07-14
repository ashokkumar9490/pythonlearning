import {
  CUSTOM_ELEMENTS_SCHEMA,
  NgModule,
  NO_ERRORS_SCHEMA,
} from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HelloComponent } from './hello/hello.component';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { WelcomeComponent } from './welcome/welcome.component';

import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

import { TodoComponent } from './todo/todo.component';

import { MatButtonModule } from '@angular/material/button';
import { MatToolbar, MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatBadgeModule } from '@angular/material/badge';
import { MatTableModule } from '@angular/material/table';
import { MatCheckboxModule } from '@angular/material/checkbox';
import {
  MAT_FORM_FIELD_DEFAULT_OPTIONS,
  matFormFieldAnimations,
  MatFormFieldModule,
} from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { HighlightDirective } from './highlight.directive';
import { Todo2Component } from './todo2/todo2.component';
import { ReactiveFormsComponent } from './reactive-forms/reactive-forms.component';
import { ChildComponent } from './child/child.component';
import { ParentComponent } from './parent/parent.component';
import { React2Component } from './react2/react2.component';
import { TsclassComponent } from './tsclass/tsclass.component';
import { P2Component } from './p2/p2.component';
import { C2Component } from './c2/c2.component';
import { ProductsComponent } from './products/products.component';
import { Todo3Component } from './todo3/todo3.component';

import { ToastrModule } from 'ngx-toastr';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { EmpsComponent } from './emps/emps.component';
import { EmpsDetailsComponent } from './emps-details/emps-details.component';
import { React1Component } from './react1/react1.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { TopbarComponent } from './topbar/topbar.component';
import { EmpDetailComponent } from './emp-detail/emp-detail.component';
import { ShowFavComponent } from './show-fav/show-fav.component';
import { LightswitchComponent } from './lightswitch/lightswitch.component';
import { NewsComponent } from './news/news.component';
import { CricketPlayerComponent } from './cricket-player/cricket-player.component';
import { TodoJsonComponent } from './todo-json/todo-json.component';

@NgModule({
  declarations: [
    AppComponent,
    HelloComponent,
    WelcomeComponent,
    TodoComponent,
    HighlightDirective,
    Todo2Component,
    ReactiveFormsComponent,
    ChildComponent,
    ParentComponent,
    React2Component,
    TsclassComponent,
    P2Component,
    C2Component,
    ProductsComponent,
    Todo3Component,
    EmpsComponent,
    EmpsDetailsComponent,
    React1Component,
    LoginComponent,
    LogoutComponent,
    TopbarComponent,
    EmpDetailComponent,
    ShowFavComponent,
    NewsComponent,
    CricketPlayerComponent,
    TodoJsonComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    MatBadgeModule,
    MatSlideToggleModule,
    MatIconModule,
    MatCheckboxModule,
    MatFormFieldModule,
    MatInputModule,
    MatToolbar,
    MatTableModule,
    MatButtonModule,
    ToastrModule.forRoot({
      timeOut: 3000,
      positionClass: 'toast-bottom-right',
    }),
    BrowserAnimationsModule,
  ],
  exports: [],
  providers: [
    provideAnimationsAsync(),
    {
      provide: MAT_FORM_FIELD_DEFAULT_OPTIONS,
      useValue: { appearance: 'outline' },
    },
  ],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA, NO_ERRORS_SCHEMA],
})
export class AppModule {}
