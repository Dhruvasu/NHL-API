from flask import Flask, jsonify, abort, request
import pandas as pd
import numpy as np

app = Flask(__name__)


# sample code for loading the team_info.csv file into a Pandas data frame.  Repeat as
# necessary for other files
def load_teams_data():
    td = pd.read_csv("./team_info.csv")
    return td
def load_game_data():
    td = pd.read_csv("./game.csv")
    return td
def load_player_info():
    td = pd.read_csv("./player_info.csv")
    return td
def load_game_skater_stats():
    td = pd.read_csv("./game_skater_stats.csv")
    return td
def load_game_teams_stats():
    td = pd.read_csv("./game_teams_stats.csv")
    return td


#global variables
team_data = load_teams_data()
print("successfully loaded teams data")
game_data = load_game_data()
print("successfully loaded games data")
player_info = load_player_info()
print("successfully loaded player info data")
game_skater_stats = load_game_skater_stats()
print("successfully loaded game skater stats data")
game_team_stats = load_game_teams_stats()
print("successfully loaded game skater stats data")



@app.route('/')
def index():
    return "NHL API"


# route mapping for HTTP GET on /api/schedule/TOR
@app.route('/api/teams/<string:team_id>', methods=['GET'])
def get_task(team_id):
    # fetch sub dataframe for all teams (hopefully 1) where abbreviation=team_id
    teams = team_data[team_data["abbreviation"] == team_id]

    # return 404 if there isn't one team
    if teams.shape[0] < 1:
        abort(404)

    # get first team
    team = teams.iloc[0]

    # return customized JSON structure in lieu of Pandas Dataframe to_json method
    teamJSON = {"abbreviation": team["abbreviation"],
                "city": team["shortName"],
                "name": team["teamName"]}

    # jsonify easly converts maps to JSON strings
    return jsonify(teamJSON)


#@app.route('/api/teams/<string:team_id>', methods=['GET'])
#def get_task(team_id):
#route mapping for HTTP GET on /api/results?date={YYYY-MM-DD}
@app.route('/api/results', methods=['GET'])
def get_result_details():
    date_str = request.args.get('date')
    dt = np.datetime64(date_str)
    gameJSON = {}

    games = game_data[game_data["home_team_id"] == 4]

    if games.shape[0] < 1:
        return dt

    #game = games.iloc[0]

    print(len(games.index))

    i = 0

    while i < len(games.index):
        game = games.iloc[i]
        gameJSON[int(game["game_id"])] = {
                        "home_team": int(game["home_team_id"]),
                        "away_team": int(game["away_team_id"]),
                        "home_goals": int(game["home_goals"]),
                        "away_goals": int(game["away_goals"]),
                        "outcome": game["outcome"]
                    }
        i += 1

    # gameJSON = {int(game["game_id"]):
    #                 {
    #                     "home_team": int(game["home_team_id"]),
    #                     "away_team": int(game["away_team_id"]),
    #                     "home_goals": int(game["home_goals"]),
    #                     "away_goals": int(game["away_goals"]),
    #                     "outcome": game["outcome"]
    #                 },
    # }

    #gameJSON = {"game_id": int(game["game_id"])}

    #dt = datetime.strptime(date_str, '%Y-%m-%d')

    return jsonify(gameJSON)

if __name__ == '__main__':
    app.run(debug=True)
