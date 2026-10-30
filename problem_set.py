#ana gazoni problemset1
#i am sorry this is a late! I got really caught up in all my classes after my regatta and took a while to understand what to do. 

def blue():
    # 
    red = 3
    purple = red * 12
    print(purple)
    
def blastoff():
    count = int(input("pick a number"))
    for i in range(count, 0, -1):
        print(i)4
    print("blastoff!")
    
def candy_shop():
    # manage list fo candies
    candies = ["100grands", "twix", "rolos"] 
    candies.append("kitkat")
    candies.insert(1, "reeses pieces")
    candies.sort()
    candies.remove("kitkat")
    print(candies)

    user_candies = []
    for i in range(3):
        user_candies.append(input("enter your favorite candy; "))

    all_candies = candies + user_candies
    print(len(all_candies))
    for candy in all_candies:
        print(candy)
def main():
    blue()
    blastoff()
    candy_shop()
    


main()
