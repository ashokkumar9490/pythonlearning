import { Component } from '@angular/core';
import { Player, Batsman, Bowler, WicketKeeper, AllRounder } from './Player';

@Component({
  selector: 'app-cricket-player',
  templateUrl: './cricket-player.component.html',
  styleUrl: './cricket-player.component.css',
})
export class CricketPlayerComponent {
  //create array of cricket players having 10 batsman, 10 bowlers, 5 wicketkeepers and 5 allrounders
  cricketPlayers: Player[] = [
    // add 10 batsman
    new Batsman('Virat Kohli', 18, 10000),
    new Batsman('Rohit Sharma', 45, 9000),
    new Batsman('Kane Williamson', 22, 8000),
    new Batsman('Steve Smith', 49, 7000),
    new Batsman('Joe Root', 66, 6000),
    new Batsman('David Warner', 31, 5000),

    // add 10 bowlers
    new Bowler('Jasprit Bumrah', 33, 200),
    new Bowler('Kagiso Rabada', 25, 180),
    new Bowler('Pat Cummins', 30, 160),
    new Bowler('Trent Boult', 18, 140),
    new Bowler('Rashid Khan', 10, 120),

    // add 5 wicketkeepers
    new WicketKeeper('MS Dhoni', 7, 100),
    new WicketKeeper('Quinton de Kock', 10, 40),
    new WicketKeeper('Rishabh Pant', 17, 20),

    // add allrounders
    new AllRounder('Ben Stokes', 55, 4000, 100, 50),
    new AllRounder('Hardik Pandya', 33, 3000, 80, 40),
    new AllRounder('Andre Russell', 12, 2000, 60, 30),
  ];

  selectedPlayers: Player[] = [];
  skills = ['Batsman', 'Bowler', 'WicketKeeper', 'AllRounder'];

  countOfBatsman = this.selectedPlayers.filter(
    (player) => player instanceof Batsman
  ).length;

  countOfBowler = this.selectedPlayers.filter(
    (player) => player instanceof Bowler
  ).length;

  countOfWicketKeeper = this.selectedPlayers.filter(
    (player) => player instanceof WicketKeeper
  ).length;

  selectPlayer(player: Player) {
    console.log('Selected player:', player);
    // add or remove player from selected players list
    player.isSelected = !player.isSelected;
    if (player.isSelected) {
      this.selectedPlayers.push(player);
      // add to the count of batsman, bowler, wicketkeeper and allrounder
      if (player instanceof Batsman) {
        this.countOfBatsman++;
      } else if (player instanceof Bowler) {
        this.countOfBowler++;
      } else if (player instanceof WicketKeeper) {
        this.countOfWicketKeeper++;
      }
    } else {
      this.selectedPlayers = this.selectedPlayers.filter(
        (selectedPlayer) => selectedPlayer !== player
      );
    }
  }

  showSelectedPlayers() {
    console.log(
      'Selected players:',
      this.cricketPlayers.filter((player) => player.isSelected)
    );
  }

  removePlayer(player: Player) {
    this.selectedPlayers = this.selectedPlayers.filter(
      (selectedPlayer) => selectedPlayer !== player
      // make the player unselected
    );
    player.isSelected = false;
    if (player instanceof Batsman) {
      this.countOfBatsman--;
    } else if (player instanceof Bowler) {
      this.countOfBowler--;
    } else if (player instanceof WicketKeeper) {
      this.countOfWicketKeeper--;
    }
  }
}
