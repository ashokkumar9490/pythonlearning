import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HelloComponent } from './hello.component';
import { NO_ERRORS_SCHEMA } from '@angular/core';

describe('HelloComponent', () => {
  let component: HelloComponent;
  let fixture: ComponentFixture<HelloComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [HelloComponent],
      schemas: [NO_ERRORS_SCHEMA],
    }).compileComponents();

    fixture = TestBed.createComponent(HelloComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  // test getIncrement
  it('should return 29567', () => {
    expect(component.getIncrement()).toEqual(29567);
  });

  // test SayHello
  it('should return "Button Clicked..."', () => {
    component.SayHello();
    expect(component.message).toEqual('Button Clicked...');
  });

  // test properties
  it('should check all properties of hello component', () => {
    expect(component.classname).toEqual('text-danger');
    expect(component.company).toEqual('Google');
    expect(component.weekDay).toEqual('Mon');
    expect(component.myName).toEqual('Sharad');
    expect(component.isDisabled).toEqual(false);
    expect(component.message).toEqual('message will appear here...');
    expect(component.salary).toEqual(24567);
    expect(component.friendNames).toEqual(['Aman', 'Suresh', 'Neha', 'Jyothi']);
    expect(component.myli).toEqual('myli');
  });

  // write tests to test hello.component.html
  // test h3 with id h31

  it('should have h3 with id h31', () => {
    const h3 = fixture.nativeElement.querySelector('#h31');
    expect(h3).toBeTruthy();
    expect(h3.textContent).toEqual('Hello SHARAD');
  });
});
