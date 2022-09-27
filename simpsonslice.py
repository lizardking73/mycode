#!/usr/bin/env python3
### webpage: https://github.com/csfeeser/Python/blob/master/challenges/SLICING-%20simpsons.md ###
"""Morning Slicing Challenge!"""

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def main():
    """write your code in this function to solve the challenge"""

    # write one print function for each list above
    # get the strings "eyes," "goggles," and "nothing from each
    # final output for each print should look like this:
    """My eyes! The goggles do nothing!"""

    a = challenge[2][1]
    b = challenge[2][0]
    c = challenge[3]
    print (f"My {a}! The {b} do {c}!")

    a = trial[2]["goggles"]
    b = trial[2]["eyes"]
    c = trial[3]
    print (f"My {a}! The {b} do {c}!")

    a = nightmare[0]["user"]["name"]["first"]
    b = nightmare[0]["kumquat"]
    c = nightmare[0]["d"]
    print (f"My {a}! The {b} do {c}!")

    print(len(nightmare))


    #print("My", challenge[2][1] + "!" + " " + "These", challenge[2][0], "do", challenge[3] + "!")
    #print("My", trial[2]["goggles"] +"!", "These", trial[2]["eyes"], "do", trial[3] + "!")
    # print()

if __name__ == "__main__": # <-- what is this??? we will review later :)
    main()
