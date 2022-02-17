from gurobipy import *

m = Model("AYTO-Matching")
girls = ["sabrina", "jill", "victoria", "christin", "leonie", "vanessa", "melissa", "kathleen", "mirjam", "laura"]
boys = ["marko", "marvin", "dario", "maximilian", "germaine", "sascha", "dominik", "aaron", "marc", "marcel"]

x_sabrina_marko = m.addVar(name="x_sabrina_marko")
x_sabrina_marko.vtype = GRB.BINARY
x_sabrina_marvin = m.addVar(name="x_sabrina_marvin")
x_sabrina_marvin.vtype = GRB.BINARY
x_sabrina_dario = m.addVar(name="x_sabrina_dario")
x_sabrina_dario.vtype = GRB.BINARY
x_sabrina_maximilian = m.addVar(name="x_sabrina_maximilian")
x_sabrina_maximilian.vtype = GRB.BINARY
x_sabrina_germaine = m.addVar(name="x_sabrina_germaine")
x_sabrina_germaine.vtype = GRB.BINARY
x_sabrina_sascha = m.addVar(name="x_sabrina_sascha")
x_sabrina_sascha.vtype = GRB.BINARY
x_sabrina_dominik = m.addVar(name="x_sabrina_dominik")
x_sabrina_dominik.vtype = GRB.BINARY
x_sabrina_aaron = m.addVar(name="x_sabrina_aaron")
x_sabrina_aaron.vtype = GRB.BINARY
x_sabrina_marc = m.addVar(name="x_sabrina_marc")
x_sabrina_marc.vtype = GRB.BINARY
x_sabrina_marcel = m.addVar(name="x_sabrina_marcel")
x_sabrina_marcel.vtype = GRB.BINARY
x_jill_marko = m.addVar(name="x_jill_marko")
x_jill_marko.vtype = GRB.BINARY
x_jill_marvin = m.addVar(name="x_jill_marvin")
x_jill_marvin.vtype = GRB.BINARY
x_jill_dario = m.addVar(name="x_jill_dario")
x_jill_dario.vtype = GRB.BINARY
x_jill_maximilian = m.addVar(name="x_jill_maximilian")
x_jill_maximilian.vtype = GRB.BINARY
x_jill_germaine = m.addVar(name="x_jill_germaine")
x_jill_germaine.vtype = GRB.BINARY
x_jill_sascha = m.addVar(name="x_jill_sascha")
x_jill_sascha.vtype = GRB.BINARY
x_jill_dominik = m.addVar(name="x_jill_dominik")
x_jill_dominik.vtype = GRB.BINARY
x_jill_aaron = m.addVar(name="x_jill_aaron")
x_jill_aaron.vtype = GRB.BINARY
x_jill_marc = m.addVar(name="x_jill_marc")
x_jill_marc.vtype = GRB.BINARY
x_jill_marcel = m.addVar(name="x_jill_marcel")
x_jill_marcel.vtype = GRB.BINARY
x_victoria_marko = m.addVar(name="x_victoria_marko")
x_victoria_marko.vtype = GRB.BINARY
x_victoria_marvin = m.addVar(name="x_victoria_marvin")
x_victoria_marvin.vtype = GRB.BINARY
x_victoria_dario = m.addVar(name="x_victoria_dario")
x_victoria_dario.vtype = GRB.BINARY
x_victoria_maximilian = m.addVar(name="x_victoria_maximilian")
x_victoria_maximilian.vtype = GRB.BINARY
x_victoria_germaine = m.addVar(name="x_victoria_germaine")
x_victoria_germaine.vtype = GRB.BINARY
x_victoria_sascha = m.addVar(name="x_victoria_sascha")
x_victoria_sascha.vtype = GRB.BINARY
x_victoria_dominik = m.addVar(name="x_victoria_dominik")
x_victoria_dominik.vtype = GRB.BINARY
x_victoria_aaron = m.addVar(name="x_victoria_aaron")
x_victoria_aaron.vtype = GRB.BINARY
x_victoria_marc = m.addVar(name="x_victoria_marc")
x_victoria_marc.vtype = GRB.BINARY
x_victoria_marcel = m.addVar(name="x_victoria_marcel")
x_victoria_marcel.vtype = GRB.BINARY
x_christin_marko = m.addVar(name="x_christin_marko")
x_christin_marko.vtype = GRB.BINARY
x_christin_marvin = m.addVar(name="x_christin_marvin")
x_christin_marvin.vtype = GRB.BINARY
x_christin_dario = m.addVar(name="x_christin_dario")
x_christin_dario.vtype = GRB.BINARY
x_christin_maximilian = m.addVar(name="x_christin_maximilian")
x_christin_maximilian.vtype = GRB.BINARY
x_christin_germaine = m.addVar(name="x_christin_germaine")
x_christin_germaine.vtype = GRB.BINARY
x_christin_sascha = m.addVar(name="x_christin_sascha")
x_christin_sascha.vtype = GRB.BINARY
x_christin_dominik = m.addVar(name="x_christin_dominik")
x_christin_dominik.vtype = GRB.BINARY
x_christin_aaron = m.addVar(name="x_christin_aaron")
x_christin_aaron.vtype = GRB.BINARY
x_christin_marc = m.addVar(name="x_christin_marc")
x_christin_marc.vtype = GRB.BINARY
x_christin_marcel = m.addVar(name="x_christin_marcel")
x_christin_marcel.vtype = GRB.BINARY
x_leonie_marko = m.addVar(name="x_leonie_marko")
x_leonie_marko.vtype = GRB.BINARY
x_leonie_marvin = m.addVar(name="x_leonie_marvin")
x_leonie_marvin.vtype = GRB.BINARY
x_leonie_dario = m.addVar(name="x_leonie_dario")
x_leonie_dario.vtype = GRB.BINARY
x_leonie_maximilian = m.addVar(name="x_leonie_maximilian")
x_leonie_maximilian.vtype = GRB.BINARY
x_leonie_germaine = m.addVar(name="x_leonie_germaine")
x_leonie_germaine.vtype = GRB.BINARY
x_leonie_sascha = m.addVar(name="x_leonie_sascha")
x_leonie_sascha.vtype = GRB.BINARY
x_leonie_dominik = m.addVar(name="x_leonie_dominik")
x_leonie_dominik.vtype = GRB.BINARY
x_leonie_aaron = m.addVar(name="x_leonie_aaron")
x_leonie_aaron.vtype = GRB.BINARY
x_leonie_marc = m.addVar(name="x_leonie_marc")
x_leonie_marc.vtype = GRB.BINARY
x_leonie_marcel = m.addVar(name="x_leonie_marcel")
x_leonie_marcel.vtype = GRB.BINARY
x_vanessa_marko = m.addVar(name="x_vanessa_marko")
x_vanessa_marko.vtype = GRB.BINARY
x_vanessa_marvin = m.addVar(name="x_vanessa_marvin")
x_vanessa_marvin.vtype = GRB.BINARY
x_vanessa_dario = m.addVar(name="x_vanessa_dario")
x_vanessa_dario.vtype = GRB.BINARY
x_vanessa_maximilian = m.addVar(name="x_vanessa_maximilian")
x_vanessa_maximilian.vtype = GRB.BINARY
x_vanessa_germaine = m.addVar(name="x_vanessa_germaine")
x_vanessa_germaine.vtype = GRB.BINARY
x_vanessa_sascha = m.addVar(name="x_vanessa_sascha")
x_vanessa_sascha.vtype = GRB.BINARY
x_vanessa_dominik = m.addVar(name="x_vanessa_dominik")
x_vanessa_dominik.vtype = GRB.BINARY
x_vanessa_aaron = m.addVar(name="x_vanessa_aaron")
x_vanessa_aaron.vtype = GRB.BINARY
x_vanessa_marc = m.addVar(name="x_vanessa_marc")
x_vanessa_marc.vtype = GRB.BINARY
x_vanessa_marcel = m.addVar(name="x_vanessa_marcel")
x_vanessa_marcel.vtype = GRB.BINARY
x_vanessa2_marko = m.addVar(name="x_vanessa2_marko")
x_vanessa2_marko.vtype = GRB.BINARY
x_vanessa2_marvin = m.addVar(name="x_vanessa2_marvin")
x_vanessa2_marvin.vtype = GRB.BINARY
x_vanessa2_dario = m.addVar(name="x_vanessa2_dario")
x_vanessa2_dario.vtype = GRB.BINARY
x_vanessa2_maximilian = m.addVar(name="x_vanessa2_maximilian")
x_vanessa2_maximilian.vtype = GRB.BINARY
x_vanessa2_germaine = m.addVar(name="x_vanessa2_germaine")
x_vanessa2_germaine.vtype = GRB.BINARY
x_vanessa2_sascha = m.addVar(name="x_vanessa2_sascha")
x_vanessa2_sascha.vtype = GRB.BINARY
x_vanessa2_dominik = m.addVar(name="x_vanessa2_dominik")
x_vanessa2_dominik.vtype = GRB.BINARY
x_vanessa2_aaron = m.addVar(name="x_vanessa2_aaron")
x_vanessa2_aaron.vtype = GRB.BINARY
x_vanessa2_marc = m.addVar(name="x_vanessa2_marc")
x_vanessa2_marc.vtype = GRB.BINARY
x_vanessa2_marcel = m.addVar(name="x_vanessa2_marcel")
x_vanessa2_marcel.vtype = GRB.BINARY
x_melissa_marko = m.addVar(name="x_melissa_marko")
x_melissa_marko.vtype = GRB.BINARY
x_melissa_marvin = m.addVar(name="x_melissa_marvin")
x_melissa_marvin.vtype = GRB.BINARY
x_melissa_dario = m.addVar(name="x_melissa_dario")
x_melissa_dario.vtype = GRB.BINARY
x_melissa_maximilian = m.addVar(name="x_melissa_maximilian")
x_melissa_maximilian.vtype = GRB.BINARY
x_melissa_germaine = m.addVar(name="x_melissa_germaine")
x_melissa_germaine.vtype = GRB.BINARY
x_melissa_sascha = m.addVar(name="x_melissa_sascha")
x_melissa_sascha.vtype = GRB.BINARY
x_melissa_dominik = m.addVar(name="x_melissa_dominik")
x_melissa_dominik.vtype = GRB.BINARY
x_melissa_aaron = m.addVar(name="x_melissa_aaron")
x_melissa_aaron.vtype = GRB.BINARY
x_melissa_marc = m.addVar(name="x_melissa_marc")
x_melissa_marc.vtype = GRB.BINARY
x_melissa_marcel = m.addVar(name="x_melissa_marcel")
x_melissa_marcel.vtype = GRB.BINARY
x_kathleen_marko = m.addVar(name="x_kathleen_marko")
x_kathleen_marko.vtype = GRB.BINARY
x_kathleen_marvin = m.addVar(name="x_kathleen_marvin")
x_kathleen_marvin.vtype = GRB.BINARY
x_kathleen_dario = m.addVar(name="x_kathleen_dario")
x_kathleen_dario.vtype = GRB.BINARY
x_kathleen_maximilian = m.addVar(name="x_kathleen_maximilian")
x_kathleen_maximilian.vtype = GRB.BINARY
x_kathleen_germaine = m.addVar(name="x_kathleen_germaine")
x_kathleen_germaine.vtype = GRB.BINARY
x_kathleen_sascha = m.addVar(name="x_kathleen_sascha")
x_kathleen_sascha.vtype = GRB.BINARY
x_kathleen_dominik = m.addVar(name="x_kathleen_dominik")
x_kathleen_dominik.vtype = GRB.BINARY
x_kathleen_aaron = m.addVar(name="x_kathleen_aaron")
x_kathleen_aaron.vtype = GRB.BINARY
x_kathleen_marc = m.addVar(name="x_kathleen_marc")
x_kathleen_marc.vtype = GRB.BINARY
x_kathleen_marcel = m.addVar(name="x_kathleen_marcel")
x_kathleen_marcel.vtype = GRB.BINARY
x_mirjam_marko = m.addVar(name="x_mirjam_marko")
x_mirjam_marko.vtype = GRB.BINARY
x_mirjam_marvin = m.addVar(name="x_mirjam_marvin")
x_mirjam_marvin.vtype = GRB.BINARY
x_mirjam_dario = m.addVar(name="x_mirjam_dario")
x_mirjam_dario.vtype = GRB.BINARY
x_mirjam_maximilian = m.addVar(name="x_mirjam_maximilian")
x_mirjam_maximilian.vtype = GRB.BINARY
x_mirjam_germaine = m.addVar(name="x_mirjam_germaine")
x_mirjam_germaine.vtype = GRB.BINARY
x_mirjam_sascha = m.addVar(name="x_mirjam_sascha")
x_mirjam_sascha.vtype = GRB.BINARY
x_mirjam_dominik = m.addVar(name="x_mirjam_dominik")
x_mirjam_dominik.vtype = GRB.BINARY
x_mirjam_aaron = m.addVar(name="x_mirjam_aaron")
x_mirjam_aaron.vtype = GRB.BINARY
x_mirjam_marc = m.addVar(name="x_mirjam_marc")
x_mirjam_marc.vtype = GRB.BINARY
x_mirjam_marcel = m.addVar(name="x_mirjam_marcel")
x_mirjam_marcel.vtype = GRB.BINARY
x_laura_marko = m.addVar(name="x_laura_marko")
x_laura_marko.vtype = GRB.BINARY
x_laura_marvin = m.addVar(name="x_laura_marvin")
x_laura_marvin.vtype = GRB.BINARY
x_laura_dario = m.addVar(name="x_laura_dario")
x_laura_dario.vtype = GRB.BINARY
x_laura_maximilian = m.addVar(name="x_laura_maximilian")
x_laura_maximilian.vtype = GRB.BINARY
x_laura_germaine = m.addVar(name="x_laura_germaine")
x_laura_germaine.vtype = GRB.BINARY
x_laura_sascha = m.addVar(name="x_laura_sascha")
x_laura_sascha.vtype = GRB.BINARY
x_laura_dominik = m.addVar(name="x_laura_dominik")
x_laura_dominik.vtype = GRB.BINARY
x_laura_aaron = m.addVar(name="x_laura_aaron")
x_laura_aaron.vtype = GRB.BINARY
x_laura_marc = m.addVar(name="x_laura_marc")
x_laura_marc.vtype = GRB.BINARY
x_laura_marcel = m.addVar(name="x_laura_marcel")
x_laura_marcel.vtype = GRB.BINARY

y_maximilian = m.addVar(name="y_maximilian")
y_maximilian.vtype = GRB.BINARY
y_marvin = m.addVar(name="y_marvin")
y_marvin.vtype = GRB.BINARY
y_marc = m.addVar(name="y_marc")
y_marc.vtype = GRB.BINARY
y_dominik = m.addVar(name="y_dominik")
y_dominik.vtype = GRB.BINARY
y_sascha = m.addVar(name="y_sascha")
y_sascha.vtype = GRB.BINARY
y_germaine = m.addVar(name="y_germaine")
y_germaine.vtype = GRB.BINARY
y_marko = m.addVar(name="y_marko")
y_marko.vtype = GRB.BINARY
y_dario = m.addVar(name="y_dario")
y_dario.vtype = GRB.BINARY
y_aaron = m.addVar(name="y_aaron")
y_aaron.vtype = GRB.BINARY

m.addConstr(y_maximilian + y_marc + y_marvin + y_marko + y_dario + y_dominik + y_aaron + y_sascha + y_germaine == 1, name="double_matching")

m.addConstr(x_sabrina_marko + x_sabrina_marvin + x_sabrina_dario + x_sabrina_maximilian + x_sabrina_germaine + x_sabrina_sascha + x_sabrina_dominik + x_sabrina_aaron + x_sabrina_marc + x_sabrina_marcel == 1, name="matching_sabrina")
m.addConstr(x_jill_marko + x_jill_marvin + x_jill_dario + x_jill_maximilian + x_jill_germaine + x_jill_sascha + x_jill_dominik + x_jill_aaron + x_jill_marc + x_jill_marcel == 1, name="matching_jill")
m.addConstr(x_victoria_marko + x_victoria_marvin + x_victoria_dario + x_victoria_maximilian + x_victoria_germaine + x_victoria_sascha + x_victoria_dominik + x_victoria_aaron + x_victoria_marc + x_victoria_marcel == 1, name="matching_victoria")
m.addConstr(x_christin_marko + x_christin_marvin + x_christin_dario + x_christin_maximilian + x_christin_germaine + x_christin_sascha + x_christin_dominik + x_christin_aaron + x_christin_marc + x_christin_marcel == 1, name="matching_christin")
m.addConstr(x_leonie_marko + x_leonie_marvin + x_leonie_dario + x_leonie_maximilian + x_leonie_germaine + x_leonie_sascha + x_leonie_dominik + x_leonie_aaron + x_leonie_marc + x_leonie_marcel == 1, name="matching_leonie")
m.addConstr(x_vanessa2_marko + x_vanessa2_marvin + x_vanessa2_dario + x_vanessa2_maximilian + x_vanessa2_germaine + x_vanessa2_sascha + x_vanessa2_dominik + x_vanessa2_aaron + x_vanessa2_marc + x_vanessa2_marcel == 1, name="matching_vanessa2")
m.addConstr(x_vanessa_marko + x_vanessa_marvin + x_vanessa_dario + x_vanessa_maximilian + x_vanessa_germaine + x_vanessa_sascha + x_vanessa_dominik + x_vanessa_aaron + x_vanessa_marc + x_vanessa_marcel == 1, name="matching_vanessa")
m.addConstr(x_melissa_marko + x_melissa_marvin + x_melissa_dario + x_melissa_maximilian + x_melissa_germaine + x_melissa_sascha + x_melissa_dominik + x_melissa_aaron + x_melissa_marc + x_melissa_marcel == 1, name="matching_melissa")
m.addConstr(x_kathleen_marko + x_kathleen_marvin + x_kathleen_dario + x_kathleen_maximilian + x_kathleen_germaine + x_kathleen_sascha + x_kathleen_dominik + x_kathleen_aaron + x_kathleen_marc + x_kathleen_marcel == 1, name="matching_kathleen")
m.addConstr(x_mirjam_marko + x_mirjam_marvin + x_mirjam_dario + x_mirjam_maximilian + x_mirjam_germaine + x_mirjam_sascha + x_mirjam_dominik + x_mirjam_aaron + x_mirjam_marc + x_mirjam_marcel == 1, name="matching_mirjam")
m.addConstr(x_laura_marko + x_laura_marvin + x_laura_dario + x_laura_maximilian + x_laura_germaine + x_laura_sascha + x_laura_dominik + x_laura_aaron + x_laura_marc + x_laura_marcel == 1, name="matching_laura")
m.addConstr(x_sabrina_marko + x_jill_marko + x_victoria_marko + x_christin_marko + x_leonie_marko + x_vanessa_marko + x_melissa_marko + x_kathleen_marko + x_mirjam_marko + x_laura_marko + x_vanessa2_marko == 1 + y_marko, name="matching_marko")
m.addConstr(x_sabrina_marvin + x_jill_marvin + x_victoria_marvin + x_christin_marvin + x_leonie_marvin + x_vanessa_marvin + x_melissa_marvin + x_kathleen_marvin + x_mirjam_marvin + x_laura_marvin + x_vanessa2_marvin == 1 + y_marvin, name="matching_marvin")
m.addConstr(x_sabrina_dario + x_jill_dario + x_victoria_dario + x_christin_dario + x_leonie_dario + x_vanessa_dario + x_melissa_dario + x_kathleen_dario + x_mirjam_dario + x_laura_dario + x_vanessa2_dario == 1 + y_dario, name="matching_dario")
m.addConstr(x_sabrina_maximilian + x_jill_maximilian + x_victoria_maximilian + x_christin_maximilian + x_leonie_maximilian + x_vanessa_maximilian + x_melissa_maximilian + x_kathleen_maximilian + x_mirjam_maximilian + x_laura_maximilian + x_vanessa2_maximilian == 1 + y_maximilian, name="matching_maximilian")
m.addConstr(x_sabrina_germaine + x_jill_germaine + x_victoria_germaine + x_christin_germaine + x_leonie_germaine + x_vanessa_germaine + x_melissa_germaine + x_kathleen_germaine + x_mirjam_germaine + x_laura_germaine + x_vanessa2_germaine == 1 + y_germaine, name="matching_germaine")
m.addConstr(x_sabrina_sascha + x_jill_sascha + x_victoria_sascha + x_christin_sascha + x_leonie_sascha + x_vanessa_sascha + x_melissa_sascha + x_kathleen_sascha + x_mirjam_sascha + x_laura_sascha + x_vanessa_sascha == 1 + y_sascha, name="matching_sascha")
m.addConstr(x_sabrina_dominik + x_jill_dominik + x_victoria_dominik + x_christin_dominik + x_leonie_dominik + x_vanessa_dominik + x_melissa_dominik + x_kathleen_dominik + x_mirjam_dominik + x_laura_dominik + x_vanessa2_dominik == 1 + y_dominik, name="matching_dominik")
m.addConstr(x_sabrina_aaron + x_jill_aaron + x_victoria_aaron + x_christin_aaron + x_leonie_aaron + x_vanessa_aaron + x_melissa_aaron + x_kathleen_aaron + x_mirjam_aaron + x_laura_aaron + x_vanessa2_aaron == 1 + y_aaron, name="matching_aaron")
m.addConstr(x_sabrina_marc + x_jill_marc + x_victoria_marc + x_christin_marc + x_leonie_marc + x_vanessa_marc + x_melissa_marc + x_kathleen_marc + x_mirjam_marc + x_laura_marc + x_vanessa2_marc == 1 + y_marc, name="matching_marc")
m.addConstr(x_sabrina_marcel + x_jill_marcel + x_victoria_marcel + x_christin_marcel + x_leonie_marcel + x_vanessa_marcel + x_melissa_marcel + x_kathleen_marcel + x_mirjam_marcel + x_laura_marcel == 1, name="matching_marcel")

m.addConstr(x_sabrina_maximilian == 0, name="matchbox_1")
m.addConstr(x_kathleen_aaron == 0, name="matchbox_3")
m.addConstr(x_laura_marcel == 0, name="matchbox_4")
m.addConstr(x_leonie_marcel == 1, name="matchbox_5")

m.addConstr(x_sabrina_marko + x_jill_marvin + x_victoria_dario + x_christin_maximilian + x_leonie_germaine + x_vanessa_sascha + x_kathleen_aaron + x_mirjam_marc + x_laura_marcel + x_melissa_dominik == 2, name="matchingnight_1")
m.addConstr(x_sabrina_marko + x_jill_sascha + x_victoria_germaine + x_christin_maximilian + x_leonie_marcel + x_vanessa_marvin + x_kathleen_aaron + x_mirjam_marc + x_laura_dario + x_melissa_dominik== 2, name="matchingnight_2")
m.addConstr(x_sabrina_sascha + x_jill_maximilian + x_victoria_dario + x_christin_germaine + x_leonie_marc + x_vanessa_dominik + x_kathleen_marvin + x_mirjam_marko + x_laura_marcel + x_melissa_aaron == 3, name="matchingnight_3")
m.addConstr(x_sabrina_marko + x_jill_maximilian + x_victoria_germaine + x_christin_marvin + x_leonie_marcel + x_vanessa_sascha + x_kathleen_dario + x_mirjam_marc + x_laura_dominik + x_melissa_aaron == 3, name="matchingnight_4")
m.addConstr(x_vanessa2_marko + x_jill_sascha + x_victoria_dario + x_christin_germaine + x_vanessa_dominik + x_kathleen_marvin + x_mirjam_aaron + x_laura_maximilian + x_melissa_marc == 2, name="matchingnight_5")
m.addConstr(x_vanessa2_dario + x_melissa_aaron + x_mirjam_marc + x_victoria_germaine + x_laura_marvin + x_vanessa_dominik + x_sabrina_marko + x_jill_sascha + x_christin_maximilian == 3, name="martchingnight_6")

m.setObjective(0)

m.setParam(GRB.Param.PoolSolutions, 2000000000)
m.setParam(GRB.Param.PoolSearchMode, 2)

m.update()

m.optimize()

# a model with 32 rows, 119 columns and 298 nonzeros
# Variable types: 0 continuous, 119 integer (119 binary)

# Presolve removed 6 rows and 26 columns
# Presolve time: 0.00s
# Presolved: 26 rows, 93 columns, 218 nonzeros
# Variable types: 0 continuous, 93 integer (93 binary)
# Explored 2675 nodes (1578 simplex iterations) in 0.10 seconds
# Thread count was 8 (of 8 available processors)

# Solution count 1125: 0 0 0 ... 0