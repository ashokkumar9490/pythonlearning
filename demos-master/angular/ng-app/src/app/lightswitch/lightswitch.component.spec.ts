import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LightswitchComponent } from './lightswitch.component';
import { By } from '@angular/platform-browser';

describe('LightswitchComponent', () => {
  let component: LightswitchComponent;
  let fixture: ComponentFixture<LightswitchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LightswitchComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(LightswitchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('#clicked() should toggle #isOn', () => {
    component = fixture.componentInstance;
    expect(component.isOn).withContext('off at first').toBe(false);
    component.clicked();
    expect(component.isOn).withContext('on after click').toBe(true);
    component.clicked();
    expect(component.isOn).withContext('off after second click').toBe(false);
  });
  it('#clicked() should set #message to "is on"', () => {
    const comp = fixture.componentInstance;
    expect(comp.message)
      .withContext('off at first')
      .toMatch(/is off/i);
    comp.clicked();
    expect(comp.message).withContext('on after clicked').toMatch(/is on/i);
  });

  it('native - should have <b1> with text "Click me!"', () => {
    const bannerElement: HTMLElement = fixture.nativeElement;
    const b = bannerElement.querySelector('#b1')!;
    expect(b.innerHTML).toEqual('Click me!');
  });

  it('debug - should have <b1> with text "Click me!"', () => {
    const element: any = fixture.debugElement.query(By.css('#b1'));
    const b = element.nativeElement;
    expect(b.innerHTML).toEqual('Click me!');
  });
});
