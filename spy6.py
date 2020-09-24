# 2. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.'''

print('1 product is of rupees 200')
print('10% discount on purchasing of min 1000 rupees')
no_of_product = input('enter the number of products = ')
print(end='\n')
no_of_product = int(no_of_product)
total_amt = 200 * no_of_product
print("total_amt = {} rupees".format(total_amt))
if total_amt >= 1000:
    amt_paid = (total_amt - ((10/100) * total_amt))
    print('paying_amt = {} rupees '.format(amt_paid), end='')
else:
    amt_paid = total_amt
    print('paying_amt = {} rupees '.format(amt_paid), end='')
