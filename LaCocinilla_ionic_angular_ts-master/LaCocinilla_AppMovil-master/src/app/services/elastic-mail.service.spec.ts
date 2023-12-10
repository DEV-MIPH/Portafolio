import { TestBed } from '@angular/core/testing';

import { ElasticMailService } from './elastic-mail.service';

describe('ElasticMailService', () => {
  let service: ElasticMailService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ElasticMailService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
