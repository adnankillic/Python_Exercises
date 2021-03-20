def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_in_house = 0
    orange_in_house = 0
    
    for apple in apples:
        if apple + a >= s and apple + a <= t:
            apple_in_house += 1
    for orange in oranges:
        if orange + b >= s and orange + b <= t:
            orange_in_house += 1
    print(apple_in_house)
    print(orange_in_house)