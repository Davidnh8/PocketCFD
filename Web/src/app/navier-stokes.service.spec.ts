import { TestBed } from '@angular/core/testing';

import { NavierStokesService } from './navier-stokes.service';

describe('NavierStokesService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: NavierStokesService = TestBed.get(NavierStokesService);
    expect(service).toBeTruthy();
  });
});
