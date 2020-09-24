x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x != y)
# to demonstrate the difference between "is not" and "!=": this comparison returns False because x is equal to y


x = ["apple", "banana"]

print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]

print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list
