import re
file_path = "input.txt"
contents = []
new_calib = []

# Part 1
def first_and_last_digit(s):
    if len(s) == 1:
        return s + s
    else:
        return s[0] + s[-1]

with open(file_path, "r") as file:

    def numeric_data(s):
        return ''.join(c for c in s if c.isdigit())

    for line in file:
        num = numeric_data(line.strip())
        contents.append(int(num))
        new_calib.append(first_and_last_digit(num))

# print(new_calib)
print(sum(int(i) for i in new_calib))

# Part 2

word_to_digit = {
    "eighthree" : "83",
    "sevenine" : "79",
    "oneight" : "18", 
    "threeight" : "38",
    "fiveight" : "58",
    "nineight" : "98",
    "twone" : "21",
    "eightwo" : "82",
    "twoseven" : "27",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",           
}

def first_and_last_digit(s):
    if len(s) == 1:
        return s + s
    else:
        return s[0] + s[-1]

with open(file_path, "r") as file:
    def numeric_data(s):
        for word, digit in word_to_digit.items():
            s = s.replace(word, digit)
        return ''.join(c for c in s if c.isdigit())
    
    for line in file:
        num = numeric_data(line.strip())
        contents.append(int(num))
        new_calib.append(first_and_last_digit(num))
# print(contents)
# print(new_calib)

print(sum(int(i) for i in new_calib))