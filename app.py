import copy
import random
import constants

#v2
def clean_data(players_data):
    for player in players_data:
        player["height"] = int(player["height"].split()[0])
        player["experience"] = player["experience"] == 'YES'
    return players_data

if __name__ == "__main__":
    players_data = copy.deepcopy(constants.PLAYERS)
    players_data = clean_data(players_data)
    random.shuffle(players_data)
    all_teams = copy.deepcopy(constants.TEAMS)

    experienced_players = [player for player in players_data if player["experience"]]
    inexperienced_players = [player for player in players_data if not player["experience"]]

    num_teams = len(all_teams)
    num_players_per_team = len(players_data) // num_teams // 2

    random.shuffle(experienced_players)
    random.shuffle(inexperienced_players)

    height_all_team = [player["height"] for player in players_data]
    total_height_all_team = sum(height_all_team)
    ave_team_height = total_height_all_team // len(players_data)

    for player in players_data:
        player["ave_height"] = ave_team_height

    teams = []
    for i in range(num_teams):
        team = []
        team.extend(experienced_players[i * num_players_per_team:(i + 1) * num_players_per_team])
        team.extend(inexperienced_players[i * num_players_per_team:(i + 1) * num_players_per_team])

        random.shuffle(team)
        teams.append(team)

    all_players = []
    all_guardians = []
    for team_players in teams:
        for player in team_players:
            if player["name"] not in all_players:
                all_players.append(player["name"])
            if player["guardians"] not in all_guardians:
                all_guardians.extend(player["guardians"])

    quit_flag = False
    while not quit_flag:
        print("\n-- Menu --")
        print("1 - Display Teams")
        print("2 - Quit")
        try:
            option1 = int(input("Please enter an option: "))
            if option1 == 1:
                print("=> Teams:")
                for i, team in enumerate(all_teams, 1):
                    print("{} - {}".format(i, team))
                print("=> More: ")
                print("4 - Overall stats\n5 - Back\n6 - Quit")

            elif option1 == 2:
                print("Quitting the Tool...")
                quit_flag = True

            else:
                print("Invalid option. Please enter 1 or 2.")
                continue

        except ValueError:
            print("Invalid input. Please enter a valid option.")
            continue

        while not quit_flag:
            option2 = input("\nPlease enter a valid option: ")

            if option2 == '5':
                break
            elif option2 == '4':
                print("\nTotal teams: {}".format(len(all_teams)))
                print("Total players: {}".format(len(players_data)))
                print("Experienced players: {}".format(len(experienced_players)))
                print("Inexperienced players: {}".format(len(inexperienced_players)))
                print("Average height: {} inches".format(ave_team_height))
                print()
                all_players_on_teams = sorted([player["name"] for player in players_data])
                print("Players on teams: {}".format(", ".join(all_players_on_teams)))
                print()
                all_guardians_on_teams = sorted([player["guardians"] for player in players_data])
                print("Guardians on teams: {}".format(", ".join(all_guardians_on_teams)))
                continue

            elif option2 == '6':
                print("Quitting the tool...")
                quit_flag = True
                break

            try:
                team_index = int(option2) - 1
                if 0 <= team_index < num_teams:
                    team_name = all_teams[team_index]
                    team_players = teams[team_index]
                    total_players = len(team_players)
                    player_names = sorted(
                        [player["name"] + " (EXP)" if player["experience"] else player["name"] + " (NO EXP)"
                        for player in team_players if player["name"] in all_players])
                    guardians = sorted([player["guardians"] for player in team_players])
                    height_team = [player['height'] for player in team_players]
                    total_height = sum(height_team)
                    ave_height = total_height // len(team_players)

                    print("\nTeam: {}".format(team_name))
                    print("==============")
                    print("Total players: {}".format(total_players))
                    print("Experienced players: {}".format(len([player for player in team_players if player["experience"]])))
                    print("Inexperienced players: {}".format(len([player for player in team_players if not player["experience"]])))
                    print("Average height: {} inches".format(ave_height))
                    print()
                    print("Players on team: {}".format(", ".join(player_names)))
                    print()
                    print("Guardians on team: {}".format(", ".join(guardians)))
                else:
                    print("Invalid input. Please enter a valid option.")

            except ValueError:
                print("Invalid input. Please enter a valid option.")
