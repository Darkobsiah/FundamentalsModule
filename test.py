import time

# initialize a counter
counter = 0
for i in range(5, 0, -1):
    print(i)
    counter += 1
    time.sleep(1)
    if counter % 5 == 0:
        while 1 == 1:
            print('Slavi Hubostnika' * 10)
            time.sleep(0.5)

