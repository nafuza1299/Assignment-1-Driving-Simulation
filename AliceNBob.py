def alicenbob():
    stones = int(input())
    if int(stones) % 2 == 0: #If stones is divisible by 2, Alice wins
        print("Alice")
    else:
        print("Bob")
    return
alicenbob()
