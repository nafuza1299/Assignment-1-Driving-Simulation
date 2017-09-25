acceleration = int(input("Input Acceleration:"))
initial_vel = 0
distance = int(input("Input Distance:"))
time = int(input("Input Time:"))
speed = (distance/time)
velocity = initial_vel + (acceleration*time)
speed_lim = 60
for x in range(time):
    displacement = velocity*time + (acceleration / 2 * time ** 2)
    print("Duration:"+ "" + str(x)+ " "+"Distance:"+ " "+"*"*x)
if speed > speed_lim:
    print("The person went over the speed limit"+ " "+"Max speed was"+ " "+str(speed_lim), "m/s")
else:
    print("The person did not go over the speed limit."+ " "+"Max speed was"+ " "+str(speed_lim), "m/s")
if distance >= displacement:
    print("The person reached the destination."+ " "+"Reached"+ " "+str(displacement), "m")
else:
    print("The person did not reach the destination."+ " "+"Reached"+ " "+str(displacement), "m")
