import { Component, OnInit } from '@angular/core';
import { NavierStokesService } from 'src/app/navier-stokes.service'
import { DomSanitizer } from '@angular/platform-browser';
import { FormBuilder, FormGroup } from '@angular/forms'

@Component({
  selector: 'app-navier-stokes-cavity',
  templateUrl: './navier-stokes-cavity.component.html',
  styleUrls: ['./navier-stokes-cavity.component.css']
})
export class NavierStokesCavityComponent implements OnInit {

  cavity: any;
  parameterForm;

  constructor(
    private navierstokes: NavierStokesService,
    private sanitizer: DomSanitizer,
    private formBuilder: FormBuilder,
  ) {
    this.parameterForm = this.formBuilder.group({
      xlength: '',
      ylength: '',
      nx: '',
      nu: '',
      rho: '',
      dt: '',
      iteration: '',
    })
  }

  ngOnInit() {

  }
/*
  public getCavity(){
    this.navierstokes.Cavity()
    .subscribe(data => { 
      let urlObject = URL.createObjectURL(data);
      this.cavity = this.sanitizer.bypassSecurityTrustUrl(urlObject);
    })
  }
*/
  public onSubmit(parameters: FormGroup){
    //console.log(parameters)

    this.navierstokes.Cavity(parameters)
    .subscribe(data => {
      let urlObject = URL.createObjectURL(data);
      this.cavity = this.sanitizer.bypassSecurityTrustUrl(urlObject);
    })


  }



}

