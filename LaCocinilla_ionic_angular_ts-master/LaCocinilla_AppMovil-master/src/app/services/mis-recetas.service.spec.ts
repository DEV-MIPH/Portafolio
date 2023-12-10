import { TestBed } from '@angular/core/testing';

import { MisRecetasService } from './mis-recetas.service';

describe('MisRecetasService', () => {
  let service: MisRecetasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MisRecetasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
