// create cricket player base class
export class Player {
  constructor(
    public name: string,
    public jerseyNumber: number,
    public skill: string,
    public isSelected: boolean = false
  ) {}
}

// bowler class
export class Bowler extends Player {
  constructor(name: string, jerseyNumber: number, public wickets: number) {
    super(name, jerseyNumber, 'Bowler');
  }
}

// batsman class
export class Batsman extends Player {
  constructor(name: string, jerseyNumber: number, public runs: number) {
    super(name, jerseyNumber, 'Batsman');
  }
}

// wicketkeeper class
export class WicketKeeper extends Player {
  constructor(name: string, jerseyNumber: number, public catches: number) {
    super(name, jerseyNumber, 'WicketKeeper');
  }
}

// allrounder class
export class AllRounder extends Player {
  constructor(
    name: string,
    jerseyNumber: number,
    public runs: number,
    public wickets: number,
    public catches: number
  ) {
    super(name, jerseyNumber, 'AllRounder');
  }
}
