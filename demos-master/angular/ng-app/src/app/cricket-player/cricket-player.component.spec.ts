import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CricketPlayerComponent } from './cricket-player.component';

describe('CricketPlayerComponent', () => {
  let component: CricketPlayerComponent;
  let fixture: ComponentFixture<CricketPlayerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CricketPlayerComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CricketPlayerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
