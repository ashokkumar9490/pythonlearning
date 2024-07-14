import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StudSubjComponent } from './stud-subj.component';

describe('StudSubjComponent', () => {
  let component: StudSubjComponent;
  let fixture: ComponentFixture<StudSubjComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [StudSubjComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(StudSubjComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
