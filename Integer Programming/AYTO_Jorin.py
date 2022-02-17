from gurobipy import *

m = Model("AYTO-Matching")

girls = ["sabrina", "jill", "victoria", "christin", "leonie", "vanessa", "vanessa2", "melissa", "kathleen", "mirjam", "laura"]
boys = ["marko", "marvin", "dario", "maximilian", "germaine", "sascha", "dominik", "aaron", "marc", "marcel"]

numberOfGirls = len(girls) #11
numberOfBoys = len(boys) #10

Var_x = m.addVars(numberOfGirls, numberOfBoys, vtype = GRB.BINARY, name="x")
Var_y = m.addVars(numberOfBoys-1, vtype = GRB.BINARY, name="y") #-1 wegen marcel kein double match (und marcel als letztes in der liste)

#constraint 1: matching for girls:

m.addConstrs((quicksum(Var_x[g,b] for b in range(numberOfBoys)) == 1 for g in range(numberOfGirls)), "c1")

#constraint 2: matching for boys:

m.addConstrs((quicksum(Var_x[g,b] for g in range(numberOfGirls)) == 1 + Var_y[b]  for b in range(numberOfBoys-1)), "c2") 
m.addConstr((quicksum(Var_x[g,boys.index("marcel")] for g in range(numberOfGirls) if g != girls.index("vanessa2")) == 1), "c2 - marcel")

#constraint 3: double-matching:

m.addConstr((quicksum(Var_y[b] for b in range(numberOfBoys-1)) == 1), "c3")

#Matchbox constraints:

m.addConstr(Var_x[girls.index("sabrina"),boys.index("maximilian")] == 0, name="matchbox_1")
m.addConstr(Var_x[girls.index("kathleen"),boys.index("aaron")] == 0, name="matchbox_3")
m.addConstr(Var_x[girls.index("laura"),boys.index("marcel")] == 0, name="matchbox_4")
m.addConstr(Var_x[girls.index("leonie"),boys.index("marcel")] == 1, name="matchbox_5")

#Matching Night constraints:

m.addConstr(Var_x[girls.index("sabrina"),boys.index("marko")] + Var_x[girls.index("jill"),boys.index("marvin")] + Var_x[girls.index("victoria"),boys.index("dario")] + Var_x[girls.index("christin"),boys.index("maximilian")] + Var_x[girls.index("leonie"),boys.index("germaine")]+ Var_x[girls.index("vanessa"),boys.index("sascha")] + Var_x[girls.index("kathleen"),boys.index("aaron")] + Var_x[girls.index("mirjam"),boys.index("marc")] + Var_x[girls.index("laura"),boys.index("marcel")] + Var_x[girls.index("melissa"),boys.index("dominik")]== 2, name="matchingnight_1")
m.addConstr(Var_x[girls.index("sabrina"),boys.index("marko")] + Var_x[girls.index("jill"),boys.index("sascha")] + Var_x[girls.index("victoria"),boys.index("germaine")] + Var_x[girls.index("christin"),boys.index("maximilian")] +Var_x[girls.index("leonie"),boys.index("marcel")] +Var_x[girls.index("vanessa"),boys.index("marvin")] +Var_x[girls.index("kathleen"),boys.index("aaron")] +Var_x[girls.index("mirjam"),boys.index("marc")] +Var_x[girls.index("laura"),boys.index("dario")] +Var_x[girls.index("melissa"),boys.index("dominik")] == 2, name="matchingnight_2")
m.addConstr(Var_x[girls.index("sabrina"),boys.index("sascha")] + Var_x[girls.index("jill"),boys.index("maximilian")] +Var_x[girls.index("victoria"),boys.index("dario")] +Var_x[girls.index("christin"),boys.index("germaine")] +Var_x[girls.index("leonie"),boys.index("marc")] +Var_x[girls.index("vanessa"),boys.index("dominik")] +Var_x[girls.index("kathleen"),boys.index("marvin")] +Var_x[girls.index("mirjam"),boys.index("marko")] +Var_x[girls.index("laura"),boys.index("marcel")] +Var_x[girls.index("melissa"),boys.index("aaron")]  == 3, name="matchingnight_3")
m.addConstr(Var_x[girls.index("sabrina"),boys.index("marko")] + Var_x[girls.index("jill"),boys.index("maximilian")] + Var_x[girls.index("victoria"),boys.index("germaine")] + Var_x[girls.index("christin"),boys.index("marvin")] + Var_x[girls.index("leonie"),boys.index("marcel")] + Var_x[girls.index("vanessa"),boys.index("sascha")] + Var_x[girls.index("kathleen"),boys.index("dario")] + Var_x[girls.index("mirjam"),boys.index("marc")] + Var_x[girls.index("laura"),boys.index("dominik")] + Var_x[girls.index("melissa"),boys.index("aaron")] == 3, name="matchingnight_4") 
m.addConstr(Var_x[girls.index("vanessa2"),boys.index("marko")] + Var_x[girls.index("jill"),boys.index("sascha")] + Var_x[girls.index("victoria"),boys.index("dario")] + Var_x[girls.index("christin"),boys.index("germaine")] + Var_x[girls.index("vanessa"),boys.index("dominik")] + Var_x[girls.index("kathleen"),boys.index("marvin")] + Var_x[girls.index("mirjam"),boys.index("aaron")] + Var_x[girls.index("laura"),boys.index("maximilian")] + Var_x[girls.index("melissa"),boys.index("marc")] == 2, name="matchingnight_5")
m.addConstr(Var_x[girls.index("vanessa2"),boys.index("dario")] +Var_x[girls.index("melissa"),boys.index("aaron")] +Var_x[girls.index("mirjam"),boys.index("marc")] +Var_x[girls.index("victoria"),boys.index("germaine")] +Var_x[girls.index("laura"),boys.index("marvin")] +Var_x[girls.index("vanessa"),boys.index("dominik")] +Var_x[girls.index("sabrina"),boys.index("marko")] +Var_x[girls.index("jill"),boys.index("sascha")] +Var_x[girls.index("christin"),boys.index("maximilian")] == 3, name="matchingnight_6")




# to get names in solution:

boys_dict={}
j = 0
for item in boys:
    if(j>0 and item in boys_dict):
        continue
    else:   
        boys_dict[j] = item
        j = j+1

girls_dict={}
i = 0
for item in girls:
    if(i>0 and item in girls_dict):
        continue
    else:    
       girls_dict[i] = item
       i = i+1

m.setObjective(0)

m.setParam(GRB.Param.PoolSolutions, 2000000000)
m.setParam(GRB.Param.PoolSearchMode, 2)

m.update()

m.optimize()

# a model with 32 rows, 119 columns and 299 nonzeros
# Variable types: 0 continuous, 119 integer (119 binary)
# Presolve removed 6 rows and 26 columns
# Presolve time: 0.00s
# Presolved: 26 rows, 93 columns, 225 nonzeros
# Variable types: 0 continuous, 93 integer (93 binary)
# Explored 3244 nodes (1579 simplex iterations) in 0.16 seconds
# Thread count was 8 (of 8 available processors)

# Solution count 1387: 0 0 0 ... 0


#c1: 11 rows
#c2: 10 rows
#c3: 1 row
#Matchbox: 4 rows
#Matching night: 6 rows
