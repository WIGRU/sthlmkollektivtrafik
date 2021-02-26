from sthlmkollektivtrafik import realtidsinformation

res = realtidsinformation.departure(5473, 100)

print("--------------------------------------------------------")
print("Bussar:")
print("--------------------------------------------------------")
for i in range(len(res.busDest)):
    print("Buss {} mot {} avgår om {}".format(res.busNum[i], res.busDest[i], res.busTime[i]))
print("--------------------------------------------------------")

print("Tåg:")
print("--------------------------------------------------------")
for i in range(len(res.trainDest)):
    print("Tåg {} mot {} avgår om {}".format(res.trainNum[i], res.trainDest[i], res.trainTime[i]))
print("--------------------------------------------------------")

print("Tunnelbana:")
print("--------------------------------------------------------")
for i in range(len(res.trainDest)):
    print("Buss {} mot {} avgår om {}".format(res.metroNum[i], res.metroDest[i], res.metroTime[i]))
print("--------------------------------------------------------")