def score(i, r, d, temp = 10, final = 10, initial_d = 0):
    print(round(temp))
 
    if d == 1:
        print(f"Your final score: {final}")
 
        if initial_d >= 4:
            if final >= 80:
                print("You are qualified.")
            else:
                print("You are NOT qualified.")
 
        return i
 
    return r * score(i, r, d - 1, temp * r, final + round(temp * r), initial_d)
 
def main():
 
    i = 10
    r = 1.2
 
    pressed = False
 
    while not pressed:
        print("To exit, enter number less than 2, or press Enter")
 
        d = int(input("Enter your D: "))
 
        if d >= 2:
            score(i, r, d, initial_d=d)
        else:
            pressed = True
 
 
if __name__ == '__main__':
    main()