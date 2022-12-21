save = open("save.txt", "rt")
global bgNum, score, clickPower, clickPower_level, clickPower_cost, duckyHammer_level
bgNum = 1
score = int(save.readline())
clickPower = int(save.readline())
save.close()
clickPower_level = 0
clickPower_cost = 100
duckyHammer_level = 0
