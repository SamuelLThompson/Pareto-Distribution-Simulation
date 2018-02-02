import random

sample = [[100,100,100,100,100,100,100,100,100,100,],
          [100,100,100,100,100,100,100,100,100,100,],
          [100,100,100,100,100,100,100,100,100,100,],
          [100,100,100,100,100,100,100,100,100,100,],
          [100,100,100,100,100,100,100,100,100,100,],
          [100,100,100,100,100,100,100,100,100,100,],
          [100,100,100,100,100,100,100,100,100,100,],
          [100,100,100,100,100,100,100,100,100,100,],
          [100,100,100,100,100,100,100,100,100,100,],
          [100,100,100,100,100,100,100,100,100,100,],]

def displaysample(sample):              # code to display the sample in a nice grid
    for i in range(len(sample)):
        print(sample[i])
    print()

def trade(sample, x, y, a, b):          # code to perform a trade, gets passed the 4 "coordinates" of the two people and computes based on the pseudo-random outcome of a coin toss
    value = 1
    roll = random.randint(0,1)

    if sample[x][y] == 0 or sample[a][b] == 0:
        pass

    else:
        if roll == 0:
            sample[x][y] += value
            sample[a][b] -= value

        elif roll == 1:
            sample[a][b] += value
            sample[x][y] -= value

def selection():                        # code to randomly select two people to trade (if the same person is selected for both, the outcome is irrelevant)
    global x, y, a, b

    x = random.randint(0,9)
    y = random.randint(0,9)
    a = random.randint(0,9)
    b = random.randint(0,9)

def analysis(sample):                   # the analysis function
    broke = 0
    profit = 0
    loss = 0
    nochange = 0

    print("ANALYSIS OF SAMPLE")
    print()

    for i in range(len(sample)):        # determining the aggregate data for the differnet wealth status'
        for j in range(len(sample)):
            if sample[i][j] == 0:
                broke += 1
            elif 0 < sample[i][j] < 100:
                loss += 1
            elif sample[i][j] > 100:
                profit += 1
            elif sample[i][j] == 100:
                nochange += 1

    print(broke, "people are broke")
    print(profit, "people made profit")
    print(loss, "people made a loss but are not broke")
    print(nochange, "people have had no change in wealth")
    print()

    percentwithmoney = ((profit+loss)/100)*100          # determining pecentage prominence of the different status', keep in mind that will a sample of 100 people, this calculation is irrelevant however formats the data nicely 
    perecentbroke = (broke/100)*100

    print(percentwithmoney, "% of people have all the money")
    print(perecentbroke, "% of people have no money at all")
    print()

    totalmoney = 0

    for i in range(len(sample)):        # determining the total money in the system, should be the same before and after (if it's not and money entered or left the system during trades then the resulting data is useless), this is just a double check
        for j in range(len(sample)):
            totalmoney += sample[i][j]

    print("total money in system =", totalmoney)
    print()

def simulation(sample):                     # main module code that runs the simulation, uses all of the above functions
    print("SAMPLE BEFORE TRADING BEGINS")
    print()

    displaysample(sample)
    analysis(sample)

    print("Enter number of trades that you want to simulate")
    noftrades = int(input("(anything above 1000000 will take a VERY long time to compute):"))
    print()
    print("TRADING NOW IN PROGRESS, PLEASE STAND BY...")
    print()
    print()
    
    for i in range(noftrades):
        selection()
        trade(sample, x, y, a, b)

    print()
    print()
    print("SAMPLE AFTER", noftrades, "TRADES")
    print()

    displaysample(sample)
    analysis(sample)

simulation(sample)
