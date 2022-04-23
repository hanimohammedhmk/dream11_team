import random
print("\nMerciful Army of Allah\n")


def generate_team(list):
    return random.sample(list, k=11)


def letter_to_num(x):
    num_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
                'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
                'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8}
    letter = x
    if letter.isupper:
        letter = letter.upper()
    return num_dict[letter]


def name_to_luck(names):
    name = names
    lucky_numer = 0
    for item in name:
        if(item == ' '):
            continue
        lucky_numer = lucky_numer + letter_to_num(item)
        if(lucky_numer > 9):
            lucky_numer = lucky_numer % 9
    # print(name, 'Lucky number is '+str(lucky_numer))
    return lucky_numer

tdys_lucky_number = (name_to_luck('Mumbai Dr DY Patil Sports Academy') +
                     name_to_luck('Gujarat Titans')+name_to_luck('Kolkata Knight Riders')+5+4+6) % 9

print('Tdys lucky number = {}'.format(tdys_lucky_number))

players_list1 = ['Venkatesh Iyer', 'Aaron Finch', 'Shreyas Iyer', 'Sunil Narine', 'Nitish Rana',
                 'Sheldon Jackson', 'Andre Russell', 'Pat Cummins', 'Shivam Mavi', 'Umesh Yadav', 'Varun Chakravarthy']

players_list2 = ['Shubman Gill', 'Wriddhiman Saha', 'Hardik Pandya', 'David Miller', 'Abhinav Manohar',
                 'Rahul Tewatia', 'Rashid Khan', 'Mohammad Shami', 'Lockie Ferguson', 'Alzarri Joseph', 'Yash Dayal']

wk = ['Sheldon Jackson', 'Wriddhiman Saha']
bat = ['Aaron Finch', 'Shreyas Iyer', 'Nitish Rana', 'Shubman Gill',
       'David Miller', 'Abhinav Manohar', 'Venkatesh Iyer']
all = ['Andre Russell', 'Sunil Narine', 'Hardik Pandya',
       'Rahul Tewatia']
bowl = ['Pat Cummins', 'Shivam Mavi', 'Umesh Yadav', 'Varun Chakravarthy',
        'Rashid Khan', 'Mohammad Shami', 'Lockie Ferguson', 'Alzarri Joseph', 'Yash Dayal']
# recommended = ['Hardik Pandya','Alzarri Joseph','Wriddhiman Saha','Shreyas Iyer']
point_table = {
    'Venkatesh Iyer': 8.5,
    'Aaron Finch': 8.5,
    'Shreyas Iyer': 9.5,
    'Sunil Narine': 8.5,
    'Nitish Rana': 8.5,
    'Sheldon Jackson': 7.5,
    'Andre Russell': 10.0,
    'Pat Cummins': 8.5,
    'Shivam Mavi': 8.0,
    'Umesh Yadav': 9.0,
    'Varun Chakravarthy': 8.5,
    'Shubman Gill': 9.0,
    'Wriddhiman Saha': 8.0,
    'Hardik Pandya': 10.5,
    'David Miller': 9.0,
    'Abhinav Manohar': 8.5,
    'Rahul Tewatia': 8.0,
    'Rashid Khan': 9.0,
    'Mohammad Shami': 9.0,
    'Lockie Ferguson': 8.5,
    'Alzarri Joseph': 8.5,
    'Yash Dayal': 8.0,
}


while True:
    dream_team = generate_team(wk+bat+all+bowl)
    no_of_ind_players = 0
    no_of_sl_players = 0
    no_of_wk = 0
    no_of_bat = 0
    no_of_all = 0
    no_of_bowl = 0
    no_of_recommended = 0

    for item in dream_team:
        if item in players_list1:
            no_of_ind_players += 1
        if item in players_list2:
            no_of_sl_players += 1
        if item in wk:
            no_of_wk += 1
        if item in bat:
            no_of_bat += 1
        if item in all:
            no_of_all += 1
        if item in bowl:
            no_of_bowl += 1
        # if item in recommended:
        #     no_of_recommended +=1

    total_point = 0
    for item in dream_team:
        player_point = point_table[item]
        total_point += player_point

    team_lucky_number = 0
    for item in dream_team:
        team_lucky_number = team_lucky_number + name_to_luck(item)
    team_lucky_number = team_lucky_number % 9
    # cap_vice = name_to_luck(dream_team[0])+name_to_luck(dream_team[1])

    # if no_of_ind_players < 4 or no_of_sl_players < 4 or no_of_wk == 0 or no_of_wk > 2 \
    #     or no_of_bat == 0 or no_of_bat < 3 or no_of_bowl == 0 or no_of_bowl < 3 \
    #         or no_of_all == 0 or total_point != 100 or no_of_recommended != 4 or team_lucky_number != tdys_lucky_number or cap_vice != tdys_lucky_number :
    #     continue
    if no_of_ind_players < 4 or no_of_sl_players < 4 or no_of_wk == 0 or no_of_wk > 2 \
      or no_of_bat == 0 or no_of_bat < 3 or no_of_bowl == 0 or no_of_bowl < 3 \
          or no_of_all == 0 or total_point < 95 or team_lucky_number != tdys_lucky_number  :
        continue

    else:
        break


dream_team[0] = str(dream_team[0])+' (captain)'
dream_team[1] = str(dream_team[1])+' (vice captain)'

for item in dream_team:
    print(item)


print('\n\nno _of Bangladesh players = {}'.format(no_of_ind_players))
print('no _of Australia players = {} \n\n'.format(no_of_sl_players))

print('no _of Wicket Keepers = {}'.format(no_of_wk))
print('no _of Batsmen = {}'.format(no_of_bat))
print('no _of All rounders = {}'.format(no_of_all))
print('no _of Bowlers = {}'.format(no_of_bowl))

print('\nTotal Point : {}'.format(total_point))

