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
    parameters
  ){
    let xlength = parameters.controls['xlength'].value
    let ylength = parameters.controls['ylength'].value
    let nx = parameters.controls['nx'].value
    let nu = parameters.controls['nu'].value
    let rho = parameters.controls['rho'].value
    let dt = parameters.controls['dt'].value
    let iteration = parameters.controls['iteration'].value
    console.log(xlength)
    return this.http.get("http://127.0.0.1:5002/navierstokes?xlength="+xlength+"&ylength="+ylength+"&nx="+nx+"&nu="+nu+"&rho="+rho+"&dt="+dt+"&iteration="+iteration, {responseType: "blob"})
    
  }
}
