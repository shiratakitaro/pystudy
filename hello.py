#!/usr/bin/env python3

print("Hello", "World!")

x = "blue"
y = "green"
z = x

print(x, y, z)

z = y

print(x, y, z)

x = z

print(x, y, z)


route = 865
print(route, type(route)) #865 <class 'int'> と表示
route = "North"
print(route, type(route)) #North- <class 'str'> と表示

[1, 4, 9, 16, 25, 36, 49]
['alpha', 'bravo', 'charlie', 'delta', 'echo']
['zebra', 49. -879. 'aardvark', 200]
[]


if boolean_expression1:
    suite1
elif boolean_expression2:
    suite2
elif boolean_expressionN:
    suiteN
else:
    else_suite

if x:
    print("x is nonzero")
if lines < 1000:
    print("small")
elif lines < 10000:
    print("medium")
else:
    print("large")


while boolean_expression
    suite

while True:
    item = get_next_item()
    if not item:
        break
process_item(item)


for variable if iterable:
    suite

for country in ["Denmark", "Finland", "Norway", "Sweden"]:
    print(country)

countries = ["Denmark", "Finland", "Norway", "Sweden"]
for country in coutries:
    print(country)

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter in "AIUEO":
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonant")
