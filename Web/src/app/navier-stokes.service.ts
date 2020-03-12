import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class NavierStokesService {

  constructor(
    private http: HttpClient
  ) { }

  public Cavity(
  ){
    return this.http.get("http://127.0.0.1:5002/navierstokes", {responseType: "blob"})
    
  }
}
