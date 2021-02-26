from sthlmkollektivtrafik import platsuppslag

res = platsuppslag.search("Bandyvägen")

print(res.id)