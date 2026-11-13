my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

print("List:", my_list)
print("Tuple:", my_tuple)

my_list[0] = 100

print("Changed list:", my_list)

#A list can be changed:
#my_list[0] = 100

#But this will cause an error:
#my_tuple[0] = 100
#because tuples are immutable.

#Easy way to remember:
#List  → [ ] → Can change / collection of data
#Tuple → ( ) → Cannot change / fixed collections
#Set   → { } → Unique values / unique values