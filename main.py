# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

mon_exp = [2200, 2350, 2600, 2130, 2190]
extra_expense_in_feb = mon_exp[1] - mon_exp[0]
print(extra_expense_in_feb)

expense_first_qua = mon_exp[0] + mon_exp[1] + mon_exp [2]
print(expense_first_qua)

exactly_2k_spent = False
for exp in mon_exp:
  if exp == 2000:
    exactly_2k_spent = True

print(f'Exact $2k in any month : {exactly_2k_spent}')
#list.insert(pos, val)
mon_exp.append(1980)
mon_exp[3] = mon_exp[3] - 200

print(mon_exp)


heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append('black panther')
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(heros.index('hulk')+1, 'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
heros.remove('thor')
heros.remove('hulk')
heros.insert(1, 'dr strange')
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max = int(input('Limit: '))
odd_num = []
for i in range(1, max+1,2):
  odd_num.append(i)

print(odd_num)