import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { NavierStokesCavityComponent } from './navier-stokes-cavity/navier-stokes-cavity.component';

import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { NoCacheHeadersInterceptorService } from 'src/app/no-cache-headers-interceptor.service';
import { FormsModule, ReactiveFormsModule} from '@angular/forms'

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    NavierStokesCavityComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [
            {
              provide: HTTP_INTERCEPTORS,
              useClass: NoCacheHeadersInterceptorService,
              multi: true
            }],
  bootstrap: [AppComponent]
})
export class AppModule { }
