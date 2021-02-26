from sthlmkollektivtrafik import reseplanerare

res = reseplanerare.searchJourney(1080, 9703)

for leg in res.journey[0]:
    print("{} {}: Ta {} mot {} ".format(leg[1], leg[0], leg[2], leg[4]))