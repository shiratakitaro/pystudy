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



if x:
    print("x is nonzero")


lines = 50000

if lines < 1000:
    print("small")
elif lines < 10000:
    print("medium")
else:
    print("large")



for country in ["Denmark", "Finland", "Norway", "Sweden"]:
    print(country)
countries = ["Denmark", "Finland", "Norway", "Sweden"]
for country in countries:
    print(country)

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter in "AIUEO":
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonant")

