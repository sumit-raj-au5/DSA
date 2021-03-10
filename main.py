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
