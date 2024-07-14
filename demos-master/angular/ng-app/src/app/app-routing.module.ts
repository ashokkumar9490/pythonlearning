import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HelloComponent } from './hello/hello.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { TodoComponent } from './todo/todo.component';
import { Todo2Component } from './todo2/todo2.component';
import { ReactiveFormsComponent } from './reactive-forms/reactive-forms.component';
import { ParentComponent } from './parent/parent.component';
import { React1Component } from './react1/react1.component';
import { React2Component } from './react2/react2.component';
import { TsclassComponent } from './tsclass/tsclass.component';
import { P2Component } from './p2/p2.component';
import { ProductsComponent } from './products/products.component';
import { Todo3Component } from './todo3/todo3.component';
import { EmpsComponent } from './emps/emps.component';
import { LoginComponent } from './login/login.component';
import { authGuard } from './auth.guard';
import { LogoutComponent } from './logout/logout.component';
import { EmpsDetailsComponent } from './emps-details/emps-details.component';
import { AppComponent } from './app.component';
import { adminGuard } from './admin.guard';
import { EmpDetailComponent } from './emp-detail/emp-detail.component';
import { ShowFavComponent } from './show-fav/show-fav.component';
import { NewsComponent } from './news/news.component';
import { CricketPlayerComponent } from './cricket-player/cricket-player.component';
import { TodoJsonComponent } from './todo-json/todo-json.component';

const routes: Routes = [
  // { path: '', component: HelloComponent },
  { path: 'hello', component: HelloComponent, canActivate: [authGuard] },
  { path: 'welcome', component: WelcomeComponent, canActivate: [adminGuard] },
  { path: 'todo', component: TodoComponent },
  { path: 'todo2', component: Todo2Component },
  { path: 'todo3', component: Todo3Component },
  { path: 'react', component: ReactiveFormsComponent },
  { path: 'react1', component: React1Component },
  { path: 'react2', component: React2Component },
  { path: 'prt', component: ParentComponent },
  { path: 'prt2', component: P2Component },
  { path: 'tsclass', component: TsclassComponent },
  { path: 'prod', component: ProductsComponent },
  { path: 'news', component: NewsComponent },
  { path: 'emps', component: EmpsComponent },
  { path: 'empsd', component: EmpsDetailsComponent },
  { path: 'emp/:Id', component: EmpDetailComponent },
  { path: 'login', component: LoginComponent },
  { path: 'logout', component: LogoutComponent },
  { path: 'fav', component: ShowFavComponent },
  { path: 'cric', component: CricketPlayerComponent },
  { path: 'todojs', component: TodoJsonComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
