import csv
import datetime
if __name__ == "__main__":
    player_data = {}
    header_categories = []
    list_of_player_id = []
    player_data_with_categories = {}
    player_number_id = 0
    Sharks = ["Sharks"]
    Dragons = ["Dragons"]
    Raptors = ["Raptors"]
    players_with_experience = []
    players_with_no_experience = []
    exportable_list = []

    def category_data_assigner(player_data_individual, header_categories): #THIS RETURNS A DICT OF ALL THE DATA RELEVENT TO THE INDIVIDUAL PLAYER
        #player_data_individual example: player_data["player0"]. This will bring up a list of player0's data in an order.
        specific_player_data = {}
        player = player_data_individual
        categories = header_categories
        number_of_loops = len(header_categories) - 1
        while number_of_loops >= 0:
            specific_player_data[categories[number_of_loops]] = player[number_of_loops]
            number_of_loops -= 1
        else:
            return specific_player_data

    def data_request(player, category, header_categories):
        # "player" parameter will be using: "player_data_with_categories[list_of_player_id[0]]"
        # "category" parameter will be the specific category to return
        # "header_categories" parameter will be unpacked to variables in the function
        unpack_the_tuple = tuple(header_categories)

        name, height, soccer_experience, guardian_names = unpack_the_tuple
        if category == name:
            return player[name]
        elif category == height:
            return player[height]
        elif category == soccer_experience:
            return player[soccer_experience]
        elif category == guardian_names:
            return player[guardian_names]
        else:
            return "error"

    def sorting_function(players_with_experience, players_with_no_experience, team1, team2, team3):
        # Sorts player_id's into the 3 teams according to the rules of the project
        sharks = []
        dragons = []
        raptors = []
        for i in players_with_experience:
            if len(sharks) < len(players_with_experience) / 3:
                sharks.append(i)
            elif len(dragons) < len(players_with_experience) / 3:
                dragons.append(i)
            else:
                raptors.append(i)
        for i in players_with_no_experience:
            if len(sharks) - 3 < len(players_with_no_experience) / 3:
                sharks.append(i)
            elif len(dragons) - 3 < len(players_with_no_experience) / 3:
                dragons.append(i)
            else:
                raptors.append(i)
        for i in sharks:
            team1.append(i)
        for i in dragons:
            team2.append(i)
        for i in raptors:
            team3.append(i)

    def text_formatter(team_list, player_data_with_categories, header_categories):
        #formats the list item in to a readable form specified by the the projects rules
        formatted_list = []
        formatted_list.append(team_list[0])
        for i in team_list[1:]:
            formatted_list.append(
            "{}, {}, {}".format(
            data_request(player_data_with_categories[i], header_categories[0], header_categories),
            data_request(player_data_with_categories[i], header_categories[2], header_categories),
            data_request(player_data_with_categories[i], header_categories[3], header_categories)
            )
            )
        return formatted_list

    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        the_date = ("{}/{}/{}".format(now.month, now.day, now.year))
        the_time = ("{}:{}".format(now.hour, now.minute))
        date_and_time.append(the_date)
        date_and_time.append(the_time)
        return date_and_time

    with open('soccer_players.csv') as csvfile:
        spread_sheet_reader = csv.reader(csvfile)
        rows = list(spread_sheet_reader)
        header_categories.extend(rows[0])
        for row in rows[1:]:
            player_data["player{}".format(player_number_id)] = row
            list_of_player_id.append("player{}".format(player_number_id))
            player_number_id += 1

    #These variables are assigned this way to make it easy to call values from the keys of a dict
    name = header_categories[0]
    height = header_categories[1]
    soccer_experience = header_categories[2]
    guardian_names = header_categories[3]

    for i in list_of_player_id:
        # to create an associative unordered dict to pull invididual data from, specified by player ID
        player_data_with_categories[i] = category_data_assigner(player_data[i], header_categories)



    for i, f in enumerate(list_of_player_id):
        # sorts player id's into 2 lists, players with experience and players with no experience
        if data_request(player_data_with_categories[list_of_player_id[i]], soccer_experience, header_categories) == 'YES':
            players_with_experience.append(f)
        else:
            players_with_no_experience.append(f)


    sorting_function(players_with_experience, players_with_no_experience, Sharks, Dragons, Raptors)
    #team lists filled out with player ID's

    exportable_list.extend(text_formatter(Sharks, player_data_with_categories, header_categories))
    exportable_list.extend(text_formatter(Dragons, player_data_with_categories, header_categories))
    exportable_list.extend(text_formatter(Raptors, player_data_with_categories, header_categories))
    # formatting and adding all sorted items into exportable_list

    with open("teams.txt", "w") as file:
        # writes to file teams.txt
        for i in exportable_list:
            file.write(i + "\n" + "\n")


    for i, f in enumerate(list_of_player_id):
        # extra Credit section
        with open(data_request(player_data_with_categories[list_of_player_id[i]], name, header_categories).replace(" ", "_").lower() + ".txt", "w") as file:
            if list_of_player_id[i] in Sharks:
                file.write("Date: {} ".format(get_date_and_time()[0]) + "\n")
                file.write("Time: {} ".format(get_date_and_time()[1]) + "\n")
                file.write("Dear {}, your child {}, has just finished their first round of soccer practice! He is not part of the team {}! ".format(
                data_request(player_data_with_categories[list_of_player_id[i]], guardian_names, header_categories),
                data_request(player_data_with_categories[list_of_player_id[i]], name, header_categories),
                "Sharks"
                )
                )
            elif list_of_player_id[i] in Dragons:
                file.write("Date: {} ".format(get_date_and_time()[0]) + "\n")
                file.write("Time: {} ".format(get_date_and_time()[1]) + "\n")
                file.write("Dear {}, your child {}, has just finished their first round of soccer practice! He is not part of the team {}! ".format(
                data_request(player_data_with_categories[list_of_player_id[i]], guardian_names, header_categories),
                data_request(player_data_with_categories[list_of_player_id[i]], name, header_categories),
                "Dragons"
                )
                )
            else:
                file.write("Date: {} ".format(get_date_and_time()[0]) + "\n")
                file.write("Time: {} ".format(get_date_and_time()[1]) + "\n")
                file.write("Dear {}, your child {}, has just finished their first round of soccer practice! He is not part of the team {}! ".format(
                data_request(player_data_with_categories[list_of_player_id[i]], guardian_names, header_categories),
                data_request(player_data_with_categories[list_of_player_id[i]], name, header_categories),
                "Raptors"
                )
                )
