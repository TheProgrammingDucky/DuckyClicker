import math

save = open("save.txt", "rt")
global bgNum, score, clickPower, quacksPerSecond, clickPower_level, clickPower_cost, duckyHammer_level
bgNum = 1
score = math.ceil(int(save.readline()))
clickPower = math.ceil(int(save.readline()))
save.close()
quacksPerSecond = 0
clickPower_level = 0
clickPower_cost = 100
duckyHammer_level = 0
