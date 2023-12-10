import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Forget2Page } from './forget2.page';

describe('Forget2Page', () => {
  let component: Forget2Page;
  let fixture: ComponentFixture<Forget2Page>;

  beforeEach(async(() => {
    fixture = TestBed.createComponent(Forget2Page);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
