def count_points_scored(score, first, second):
    if int(score[first]) > int(score[second]):
        return 3
    elif int(score[first]) == int(score[second]):
        return 1
    else:
        return 0


def points_scored(score, first_or_second):
    if first_or_second == 0:
        return count_points_scored(score, 0, -1)
    else:
        return count_points_scored(score, -1, 0)


def number_victories(points):
    if points == 3:
        return 1
    return 0


def create_dict(strings, point, number_element, dict_points, dict_place):
    if dict_points.get(strings[number_element]):
        number = number_victories(point)
        set_place = set()
        set_place.add(strings[number_element])
        sum_points = dict_points[strings[number_element]][2]
        dict_points[strings[number_element]][0] += point
        dict_points[strings[number_element]][1] += number
        count_points = dict_points[strings[number_element]][0]
        number_of_victories = dict_points[strings[number_element]][1]
        new_sum_points = count_points + number_of_victories
        if dict_place.get(sum_points + number + point):
            dict_place[sum_points + number + point] = dict_place[sum_points + number + point] | set_place
            if sum_points != new_sum_points:
                dict_place[sum_points] = dict_place[sum_points] - set_place
                if len(dict_place[sum_points]) < 1:
                    del dict_place[sum_points]
        else:
            dict_place[sum_points] = dict_place[sum_points] - set_place
            if len(dict_place[sum_points]) < 1:
                del dict_place[sum_points]
            dict_place[sum_points + number + point] = set_place
        dict_points[strings[number_element]][2] += number + point
    else:
        number = number_victories(point)
        set_place = set()
        set_place.add(strings[number_element])
        dict_points[strings[number_element]] = [point, number, point + number]
        if dict_place.get(dict_points[strings[number_element]][2]):
            dict_place[dict_points[strings[number_element]][2]] |= set_place
        else:
            dict_place[dict_points[strings[number_element]][2]] = set_place
    return dict_points, dict_place


def result_win_or_not(fist, second):
    if fist > second:
        return 'W'
    elif fist == second:
        return 'D'
    else:
        return 'L'


def result_games(dict_result, first_point, second_point, first_string, second_string):
    if dict_result.get(first_string):
        dict_result[first_string] += (second_string, result_win_or_not(first_point, second_point))
    else:
        dict_result[first_string] = (second_string, result_win_or_not(first_point, second_point))
    return dict_result


def check_len_string(first_string, second_string, max_element):
    if first_string > second_string:
        if first_string > max_element:
            max_element = first_string
    else:
        if second_string > max_element:
            max_element = second_string
    return max_element


def place_from_first_to_third(dict_place):
    team_place = max(list(dict_place))
    team_from_first_to_third = dict_place[team_place]
    del dict_place[team_place]
    return team_from_first_to_third


def place_second_or_third(dict_team, teams_are_equal):
    if len(list(dict_team)) > 0:
        teams = place_from_first_to_third(dict_team)
    else:
        teams = teams_are_equal
    return teams


max_len_string = 0
number_of_points_scored_and_wins = dict()
result_game = dict()
place = dict()
with open("Test 2.txt", "r") as plane:
    for team in plane.readlines():
        string = team.split()
        max_len_string = check_len_string(len(string[0]), len(string[2]), max_len_string)
        first_points = points_scored(" ".join(string[-1]).split(), 0)
        second_points = points_scored(" ".join(string[-1]).split(), 2)
        create_dict(string, first_points, 0, number_of_points_scored_and_wins, place)
        create_dict(string, second_points, 2, number_of_points_scored_and_wins, place)
        result_games(result_game, first_points, second_points, string[0], string[2])
        result_games(result_game, second_points, first_points, string[2], string[0])
count_team = len(number_of_points_scored_and_wins)
max_len_string += 1

# sort_dict = sorted(list(result_game), key=str.lower)
sort_dict = list(result_game)
sort_dict.sort(key=str.lower)

first_place = place_from_first_to_third(place)
second_place = place_second_or_third(place, first_place)
third_place = place_second_or_third(place, second_place)
table_game = [
    f"+-+{'-' * max_len_string}{'+-' * count_team}+-+-+"
]
string_ = []
for index_team in range(len(sort_dict)):
    team = sort_dict[index_team]
    string_.append(f"|{index_team + 1}|")
    string_.append(sort_dict[index_team])
    string_.append(" " * (max_len_string - len(team)))
    string_.append("|")
    len_before_games = len(string_)
    for _ in range(count_team):
        string_.append(" |")
    len_became_games = len(string_)
    string_[len_before_games + index_team] = f"{'X'}|"
    sort_sorted_dict = set(range(len(sort_dict))) - {index_team}
    for index_rival_or_result in range((len(result_game[team]) // 2)):
        rival_2 = result_game[team][index_rival_or_result * 2]
        result_rival = result_game[team][index_rival_or_result * 2 + 1]
        for rival in sort_sorted_dict:
            rivals = sort_dict[rival]
            if rival_2 == rivals:
                string_[len_before_games + sort_dict.index(rival_2)] = f"{result_rival}|"
                break
    string_.append(str(number_of_points_scored_and_wins[team][0]))
    set_team = set()
    set_team.add(team)
    if len(first_place & set_team) > 0:
        string_.append(f"|{1}|")
    elif len(second_place & set_team) > 0:
        string_.append(f"|{2}|")
    elif len(third_place & set_team) > 0:
        string_.append(f"|{3}|")
    else:
        string_.append(f"|{' '}|")
    table_game.append("".join(string_)), table_game.append(f"+-+{'-' * max_len_string}{'+-' * count_team}+-+-+")
    string_ = []
print(*table_game, sep="\n")
