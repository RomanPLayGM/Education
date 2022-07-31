max_version_a, max_version_b, max_version_c = map(int, input().split())
number_off_rule = int(input())
if number_off_rule == 0:
    print(max_version_a * max_version_b * max_version_c)
else:
    max_number_off_combinations = max_version_a * max_version_b * max_version_c
    rules = []
    number_off_correct_versions = 0
    module_versions = (1, 2, 3)
    for i in range(number_off_rule):
        rules.append(tuple(input().split()))
    rules1 = (max_version_a,) + (max_version_b,) + (max_version_c,)
    count = 0
    step = 0 if len(rules) == 1 else 1
    for i in range(0, len(rules) - step):
        rules_i = rules[i][0]
        rules_i_1 = rules[i][2]
        if step == 1:
            difference_off_the_first = int(rules[i][1]) - int(rules[i + 1][3])
            difference_off_the_third = int(rules[i][3]) - int(rules[i + 1][1])
            if rules_i == rules[i + 1][2] and rules_i_1 == rules[i + 1][0] and (difference_off_the_first <= 0 or difference_off_the_third <= 0):
                count += 2
                if difference_off_the_first <= 0:
                    if (rules_i == (1 or 2)) and (rules_i_1 == (1 or 2)):
                        version_remaining = rules1[int(rules_i_1) - 1] * rules1[2]
                        # ((rules1[int(rules_i) - 1] - int(rules[i][1]) + 1 + difference_off_the_first) * (int(rules[i][3]) - 1) * rules1[2])
                        number_off_correct_versions = (version_remaining * abs(difference_off_the_first)) + ((rules1[int(rules_i_1) - 1] - int(rules[i + 1][1]) + 1) * (int(rules[i + 1][3]) - 1 + difference_off_the_first) * rules1[2])
                    else:
                        # number_correct_0 = (rules1[int(rules_i) - 1] - int(rules[i][1]) + 1 + difference_off_the_first) * (int(rules[i][3]) - 1) * rules1[const]
                        # number_correct_1 = (rules1[int(rules_i_1) - 1] - int(rules[i + 1][1]) + 1) * (int(rules[i + 1][3]) - 1 + difference_off_the_first) * rules1[const]
                        # number_off_correct_versions = number_correct_0 + number_correct_1
                        const = abs(int(rules_i) - int(rules_i_1)) - 1
                        version_remaining = rules1[int(rules_i_1) - 1] * rules1[const]
                        number_off_correct_versions = (version_remaining * abs(difference_off_the_first)) + ((rules1[int(rules_i_1) - 1] - int(rules[i + 1][1]) + 1) * (int(rules[i + 1][3]) - 1 + difference_off_the_first) * rules1[const])
                elif difference_off_the_third <= 0:
                    if (rules_i == (1 or 2)) and (rules_i_1 == (1 or 2)):
                        number_off_correct_versions = ((int(rules[i][1])) * (int(rules[i][3]) - 1) * rules1[2]) + ((int(rules[i + 1][1]) + difference_off_the_third) * (int(rules[i + 1][3]) - 1) * rules1[2])
                    else:
                        const = abs(int(rules_i) - int(rules_i_1)) - 1
                        number_off_correct_versions = (int(rules[i][1]) * (int(rules[i][3]) - 1) * rules1[const]) + ((int(rules[i + 1][1]) + difference_off_the_third) * (int(rules[i + 1][3]) - 1) * rules1[const])
            else:
                if count == 0:
                    if (rules_i == (1 or 2)) and (rules_i_1 == (1 or 2)):
                        max_number_off_combinations -= (rules1[int(rules_i) - 1] - int(rules[i][1]) + 1) * (int(rules[i][3]) - 1) * rules1[2]
                    else:
                        max_number_off_combinations -= (rules1[int(rules_i) - 1] - int(rules[i][1]) + 1) * (int(rules[i][3]) - 1) * rules1[abs(int(rules_i) - int(rules_i_1)) - 1]
                else:
                    if (rules_i == (1 or 2)) and (rules_i_1 == (1 or 2)):
                        max_number_off_combinations -= (rules1[int(rules_i) - 1] - int(rules[i + 1][1]) + 1) * (int(rules[i + 1][3]) - 1) * rules1[2]
                    else:
                        max_number_off_combinations -= (rules1[int(rules_i) - 1] - int(rules[i + 1][1])) * (int(rules[i + 1][3]) - 1) * rules1[abs(int(rules_i) - int(rules_i_1))]
            max_number_off_combinations -= number_off_correct_versions
            number_off_correct_versions = 0
        else:
            if (rules_i == (1 or 2)) and (rules_i_1 == (1 or 2)):
                max_number_off_combinations -= (rules1[int(rules_i) - 1] - int(rules[i][1]) + 1) * (int(rules[i][3]) - 1) * rules1[2]
            else:
                max_number_off_combinations -= (rules1[int(rules_i) - 1] - int(rules[i][1]) + 1) * (int(rules[i][3]) - 1) * rules1[abs(int(rules_i) - int(rules_i_1)) - 1]
    print(max_number_off_combinations)
