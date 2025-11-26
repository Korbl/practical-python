# bounce.py
#
# Exercise 1.5
height = 100
height_loss = 0.6

for i in range(1, 11):
    height = height * height_loss
    print(i, height)
