import { TestBed } from '@angular/core/testing';

import { DbrecetaService } from './dbreceta.service';

describe('DbrecetaService', () => {
  let service: DbrecetaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DbrecetaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
