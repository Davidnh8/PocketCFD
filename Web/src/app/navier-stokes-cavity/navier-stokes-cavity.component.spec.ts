import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NavierStokesCavityComponent } from './navier-stokes-cavity.component';

describe('NavierStokesCavityComponent', () => {
  let component: NavierStokesCavityComponent;
  let fixture: ComponentFixture<NavierStokesCavityComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NavierStokesCavityComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NavierStokesCavityComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
