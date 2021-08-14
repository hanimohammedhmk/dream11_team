import random
print("\nMerciful Army of Allah\n")

def generate_team(list):
    return random.sample(list,k=11)

ind = ['Mohammad Naim',
'Soumya Sarkar',
'Shakib Al Hasan',
'Mahedi Hasan',
'Mahmudullah',
'Afif Hossain',
'Nurul Hasan',
'Shamim Patwari',
'Mustafizur Rahman',
'Shoriful Islam',
'Nasum Ahmed']

sl = ['Matthew Wade',
'Ben McDermott',
'Mitchell Marsh',
'Moises Henriques',
'Alex Carey',
'Ashton Turner',
'Daniel Christian',
'Ashton Agar',
'Nathan Ellis',
'Adam Zampa',
'Josh Hazlewood']

wk = ['Matthew Wade','Nurul Hasan','Alex Carey']
bat = ['Mohammad Naim','Mahmudullah','Shamim Patwari','Ashton Turner',
'Moises Henriques','Ben McDermott']
all = ['Shakib Al Hasan','Mitchell Marsh','Soumya Sarkar',
'Ashton Agar','Afif Hossain','Mahedi Hasan','Daniel Christian']
bowl = ['Josh Hazlewood','Mustafizur Rahman','Shoriful Islam',
'Nasum Ahmed','Nathan Ellis','Adam Zampa']

point_table = {'Mohammad Naim':9.0,
'Soumya Sarkar':9.0,
'Shakib Al Hasan':10,
'Mahedi Hasan':8.5,
'Mahmudullah':9.0,
'Afif Hossain':8.5,
'Nurul Hasan':8.5,
'Shamim Patwari':8.5,
'Mustafizur Rahman':9,
'Shoriful Islam':8.5,
'Nasum Ahmed':8.5,

'Matthew Wade':9.0,
'Ben McDermott':8.0,
'Mitchell Marsh':10.0,
'Moises Henriques':8.5,
'Alex Carey':8.5,
'Ashton Turner':8.5,
'Daniel Christian':8.5,
'Ashton Agar':9.0,
'Nathan Ellis':8.0,
'Adam Zampa':8.5,
'Josh Hazlewood':9.5}


while True:
    dream_team = generate_team(wk+bat+all+bowl)
    no_of_ind_players = 0
    no_of_sl_players = 0
    no_of_wk = 0
    no_of_bat = 0
    no_of_all = 0
    no_of_bowl = 0
    
    for item in dream_team:
        if item in ind:
            no_of_ind_players +=1
        if item in sl:
            no_of_sl_players +=1
        if item in wk:
            no_of_wk +=1
        if item in bat:
            no_of_bat +=1
        if item in all:
            no_of_all +=1
        if item in bowl:
            no_of_bowl +=1

    total_point = 0
    for item in dream_team:
        player_point = point_table[item]
        total_point += player_point

    if no_of_ind_players < 4 or no_of_sl_players < 4 or no_of_wk == 0 or no_of_wk > 2 \
        or no_of_bat == 0 or no_of_bat < 3 or no_of_bowl == 0 or no_of_bowl < 3 \
            or no_of_all == 0 or total_point > 100 :
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



