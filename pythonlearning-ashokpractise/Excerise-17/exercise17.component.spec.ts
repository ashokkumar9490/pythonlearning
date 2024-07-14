import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Exercise17Component } from './exercise17.component';

describe('Exercise17Component', () => {
  let component: Exercise17Component;
  let fixture: ComponentFixture<Exercise17Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [Exercise17Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(Exercise17Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
