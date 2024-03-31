import copy
import constants

def sort_players_by_name(players):
    return sorted(players, key=lambda x: x['name'])

def sort_guardians_by_name(players):
    return sorted(players, key=lambda x: x['guardians'])

def assign_players_to_teams(players):
    num_players = len(players)
    num_teams = len(constants.TEAMS)
    players_per_team = num_players // num_teams
    remaining_players = num_players % num_teams

    teams = [[] for _ in range(num_teams)]
    player_idx = 0
    for team_idx in range(num_teams):
        for _ in range(players_per_team + (1 if team_idx < remaining_players else 0)):
            teams[team_idx].append(players[player_idx])
            player_idx += 1

    return teams

def team_info_output(team, players_sorted):
    total_players = len(players_sorted)
    experienced_players = sum(1 for p in players_sorted if p['experience'] == 'YES')
    inexperienced_players = sum(1 for p in players_sorted if p['experience'] == 'NO')
    total_height = sum(int(p['height'].split()[0]) for p in players_sorted)

    if total_players > 0:
        average_height = total_height / total_players
    else:
        average_height = 0

    print(
        "Team: {}\nTotal Players: {}\nExperienced Players: {}\nInexperienced Players: {}\nAverage height: {:.2f} inches\n"
        .format(team, total_players, experienced_players, inexperienced_players, average_height))

def display_team_stats():
    num_players = len(constants.PLAYERS)
    num_teams = len(constants.TEAMS)
    experienced_players = sum(1 for p in constants.PLAYERS if p['experience'] == 'YES')
    inexperienced_players = sum(1 for p in constants.PLAYERS if p['experience'] == 'NO')
    total_height = sum(int(p['height'].split()[0]) for p in constants.PLAYERS if 'height' in p)
    average_height = total_height / num_players if num_players > 0 else 0
    team_names = "\n".join([f" {i} - {name}" for i, name in enumerate(constants.TEAMS, 1)])

    print(
        f"\n* Total Teams: {num_teams}\n =>Teams are:\n{team_names}\n* Total Players: {num_players}\n* Experienced Players: {experienced_players}\n* Inexperienced Players: {inexperienced_players}\n* Average height: {average_height:.2f} inches"
    )

def review_players_on_team():
    players = sorted(constants.PLAYERS, key=lambda x: x['name'])
    all_player = [player['name'] for player in players]
    print(f"Players on Teams: {', '.join(all_player)}")

def review_guardians_on_team():
    players = sorted(constants.PLAYERS, key=lambda x: x['guardians'])
    all_guardians = [player['guardians'] for player in players]
    print(f"Guardians on Teams: {', '.join(all_guardians)}")

def review_team_stats():
    while True:
        try:
            team_num = int(input(
                "Please enter a team number (1 for team Panthers, 2 for Bandits, 3 for Warriors, or 4 to Back to Sub-Menu): "))
            if team_num == 4:
                print("Returning to main menu...")
                break
            elif 1 <= team_num <= len(constants.TEAMS):
                teams = assign_players_to_teams(constants.PLAYERS)
                team_name = list(constants.TEAMS)[team_num - 1]
                team_players = teams[team_num - 1]
                team_info_output(team_name, team_players)
            else:
                print(
                    "Invalid team number. Please enter a valid team number or 4 to return to the Sub-Menu.")
        except ValueError:
            print(
                "Invalid input. Please enter a valid team number or 4 to return to the Sub-Menu.")

if __name__ == '__main__':
    players = copy.deepcopy(constants.PLAYERS)
    sorted_players = sort_players_by_name(players)
    teams = assign_players_to_teams(sorted_players)

    while True:
        print("1 - Display Team Stats\n2 - Quit")
        option1 = input("Please enter an option: ")
        try:
            option1 = int(option1)
            if option1 == 1:
                display_team_stats()
            elif option1 == 2:
                print("Quitting the Tool...")
                break
            else:
                print("Invalid input. Please enter a valid team number 1 or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid team number 1 or 2.")
            continue

        while True:
            print("\nA - Review Players on team\nB - Review Guardians on team\n"
                  "C - Review the Team's full Stats\nD - Quit the Tool...")
            option2 = input("Please enter a Sub-Menu option: ")
            if option2.lower() == "a":
                review_players_on_team()
            elif option2.lower() == "b":
                review_guardians_on_team()
            elif option2.lower() == "c":
                review_team_stats()
            elif option2.lower() == "d":
                print("Quitting to tool...")
                exit()
            else:
                print("Invalid option. Please enter a valid option (A, B, C, or D).")
