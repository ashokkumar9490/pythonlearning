import { Component } from '@angular/core';

@Component({
  selector: 'app-stud-subj',
  templateUrl: './stud-subj.component.html',
  styleUrl: './stud-subj.component.css',
})
export class StudSubjComponent {
  users: any[] = [
    {
      name: 'Anil Yadav',
    },
    {
      name: 'Anil Singh',
      qualification: [
        {
          title: 'BSc',
          year: 2015,
        },
      ],
    },
    {
      name: 'Dhiru Singh',
      qualification: [
        {
          title: 'MCA',
          year: 2014,
          subjects: [
            {
              title: 'Database',
              duration: 60,
            },
          ],
        },
        {
          title: 'BA',
          year: '2009',
          subjects: [
            {
              title: 'History',
              duration: 60,
            },
            {
              title: 'Economics',
              duration: 90,
            },
          ],
        },
      ],
    },
  ];
}
