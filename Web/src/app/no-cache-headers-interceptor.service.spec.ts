import { TestBed } from '@angular/core/testing';

import { NoCacheHeadersInterceptorService } from './no-cache-headers-interceptor.service';

describe('NoCacheHeadersInterceptorService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: NoCacheHeadersInterceptorService = TestBed.get(NoCacheHeadersInterceptorService);
    expect(service).toBeTruthy();
  });
});
