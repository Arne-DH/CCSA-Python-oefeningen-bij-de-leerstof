
def zoek_binair(rij,value):
  l = 0
  r = len(rij) -1

  while l != r:
    print(f"{l}, {r}")
    m = int((l+r)/2)
    if rij[m] < value:
      l = m+1
    else:
      r = m
  
  if rij[l] == value:
    i = l
  else:
    i = -1
  return i


#testen

i = zoek_binair([0,10,20,30,40,50,60,70,80,90],70)
print(f"index = {i}")
