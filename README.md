# Assignment1

## Game Results Summary

### User Story
As a casual NHL fan, I want data about NHL games so I can know who won/lost/tied for each game on a specific date.

### Acceptance Criteria
- Ability to specify a date
-   Provide
    - Date of Game
    - Teams that played
    - Score of each team
    - Game outcome (Regular, OT, Penalties) 

### Description
For each game_id on the specified date we provided the two teams that are involved in the game, their scores and the outcome of the game. Moreover, there are even links redirect to the detailed game summary route as well as the player stats route. It is logical that a user who visits the webpage would desire detailed information about a game and not just the scores.

### Valid URLs
- /api/results?date=2012-04-29
- /api/results?date=2012-05-03

### Invalid URLs
- /api/result?date=2012-04-29
- /api/results/date=2012-05-03


## Game Results Details:

### User Story
As a sports analyst I want detailed information about NHL game so I can report specific strengths and weaknesses of each team for viewers and make predictions/meaningful commmentary based on performance

### Acceptance Criteria
- Ability to specify a particular game
   - Ability to specficy a particular team in that game
   	- For each game, provide the following stats: 
   		- Faceoff Win %
   		- Goals scored by each team
   		- Hits taken by each team
   		- PIM
   		- Powerplay goals
   		- Powerplay opportunities
   		- Shots taken by each team
   		- Takeaways

### Description
For each game, we provided the  team stats for each team. The team stats we decided on using were based on stats we observed to be present on the NHL, ESPN, and TSN websites when we looked for a summary of NHL games. The link that we provided for each team was a link to a resource for player stats. We decided to do this because logically speaking, fans want to delve in and get more information about a game, such as who scored goals. 

### Valid URLs
- /api/results/2014030215/teams
- /api/results/2011030221/teams

### Invalid URLs
- /api/results/123456/teams
- /api/result/2011030221/teams


## Game Player Stats:

###User Story
As a fanasy hockey user I want information about individual NHL players for a specified game so that I can format my team for maximal point

### Acceptance Criteria
- Ability to specify a particular game
   - Ability to specficy a particular team within that team
   	- For each player, provide the following stats: 
   		- Plus/Minus value
   		- Blocked Shots 
   		- Goals
   		- Giveaways
   		- Penalties in Minutes
   		- PowerPlay Points
   		- Hits by athlete
   		- Shots
   		- Takeaways

### Description
For each team in a game, we provided the stats for each player on that team. The player stats that we chose were based on stats that were present on the NHL, ESPN, and TSN websites as well as sample fantasy hockey leagues. The link we provided for each player on a team is a hypothetical link to a resource that gives player information such as birthdate, birthplace, height, etc. We thought that this would be a good resource to provide because fantasy hockey players would be, for example, interested in the years of experience in a player (so they can decide to draft them or not).

### Valid URLs
- /api/results/2014030215/players
- /api/results/2011030221/players

### Invalid URLs
- /api/results/123456/teams
- /api/result/2011030221/teams

## Game Scoring Summary (Enhancement):

### Description
For a specific game referred by the game id, we privided the goals that take place within the game in chronological order of period. For each goal, we provided information that could be useful for the user to understand the player/s involved, such as the scorer and any/all assisters that helped in the goal. The timeline is divided in periods, in chronological order. For each goal, the time that it takes place is also mentioned along with the score of each team at the time of this goal. Finally, the scorer and assisters have a number beside them that indicates the number of goals scored and assisted so far in this season, respectively. We decided to provide this information to make it more realistic and provide more detailed information (as well as because it's required for full marks)

### Valid URLs
- /api/results/2014030215/scoringsummary
- /api/results/2011030221/scoringsummary

### Invalid URLs
- /api/results/12345/scoringsummary
- /api/results/54321/scoringsummary