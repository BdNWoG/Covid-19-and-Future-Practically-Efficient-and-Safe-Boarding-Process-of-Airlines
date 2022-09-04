import random

passenger = []
rowlay = []
plane = []

luggaget = 5

time = 1

aisle = []
caisle = []
a = 1
b = 0
c = 0
trow = int(input("total rows: "))
while a != 0:
      a = int(input("aisle: "))
      b += a+c
      caisle.append(int(b))
      c = 1
      if a != 0:
            aisle.append(int(a))
caisle.pop()
caisle.pop()

for j in range (len(aisle)):
      for i in range(aisle[j]):
            rowlay.append("s")
      rowlay.append("a")

rowlay.pop()
taisle = int(len(rowlay)) 

frow = []
for i in range(taisle):
      frow.append("a")

plane += [frow]

for i in range(trow):
      plane += [rowlay]

#print(plane)

luggage = int(input("allowed luggage: "))
pn = int(input("number of passengers: "))

#seatingplan
plane2 = []
for x in range(len(plane)):
    temp = []
    for elem in plane[x]:
        temp.append(elem)
    plane2.append(temp)

#passengerflow
plane3 = []
for x in range(len(plane)):
    temp = []
    for elem in plane[x]:
        temp.append(elem)
    plane3.append(temp)

#emptyreference
plane4 = []
for x in range(len(plane)):
    temp = []
    for elem in plane[x]:
        temp.append(elem)
    plane4.append(temp)

#shimmercopy
plane5 = []
for x in range(len(plane)):
    temp = []
    for elem in plane[x]:
        temp.append(elem)
    plane5.append(temp)

plugload = []
shimmer = []

for i in range(int(pn/3)):
      done = False
      while done == False:
            r = int(random.randint(0, (trow-1)//3))
            c = int(random.randint(0, taisle-1))
            l = int(random.randint(0, luggage))
            if plane2[r+1][c] == 's':
                  a = [i+1, [r+1, c], l]
                  (plane2[r+1])[c] = str(i+1)
                  passenger.append(a)
                  plugload.append(int(0))
                  shimmer.append(int(0))
                  done = True
            else:
                  done = False
                  
for i in range(int(pn/3)):
      done = False
      while done == False:
            r = int(random.randint((trow-1)//3+1,  ((trow-1)//3)*2+1))
            c = int(random.randint(0, taisle-1))
            l = int(random.randint(0, luggage))
            if plane2[r+1][c] == 's':
                  a = [i+1, [r+1, c], l]
                  (plane2[r+1])[c] = str(i+1)
                  passenger.append(a)
                  plugload.append(int(0))
                  shimmer.append(int(0))
                  done = True
            else:
                  done = False
                  
for i in range(int(pn/3)):
      done = False
      while done == False:
            r = int(random.randint(((trow-1)//3)*2+2,  trow-1))
            c = int(random.randint(0, taisle-1))
            l = int(random.randint(0, luggage))
            if plane2[r+1][c] == 's':
                  a = [i+1, [r+1, c], l]
                  (plane2[r+1])[c] = str(i+1)
                  passenger.append(a)
                  plugload.append(int(0))
                  shimmer.append(int(0))
                  done = True
            else:
                  done = False

mn = int(input("Messiness rate: "))
messy = round(mn/100*pn)

for i in range(messy):
      q = random.randint(0, pn-1)
      r = random.randint(0, pn-1)
      temp = passenger[q]
      passenger[q] = passenger[r]
      passenger[r] = temp

#luggageloadtime
for i in range(pn):
      plug = passenger[i][2]
      plugload[i] = plug * luggaget
      shimmer[i] = 0

print(passenger)

bpas = 1

seated = False
#while seated == False:
while time < 600:
      print("Time: " + str(time))
      #pathfindersim
      for i in range(pn):
            moved = 0
            for o in range(0, trow+1):
                  for p in range(0, taisle):
                        if plane3[o][p] == str(i+1):
                              mina = taisle
                              seata = passenger[i][1][1]
                              seatr = passenger[i][1][0]
                              #go to aisle
                              for n in range(len(caisle)):
                                    a = abs(caisle[n] - seata)
                                    if a <= mina:
                                          mina = a
                                          chaisle = caisle[n]
                              if o == 0 and p != chaisle and moved == 0 and plane3[o][p+1] == "a":
                                    plane3[o][p] = plane4[o][p]
                                    plane3[o][p+1] = str(i+1)
                                    moved = 1
                              #go to row
                              elif p == chaisle and o != seatr and plane3[o+1][p] == "a" and moved == 0:
                                    plane3[o][p] = plane4[o][p]
                                    plane3[o+1][p] = str(i+1)
                                    moved = 1
                              #luggage
                              elif p == chaisle and o == seatr and plugload[i] != 0 and moved == 0:
                                    plugload[i] -= 1
                                    moved = 1
                              #move in
                              elif o == seatr and plugload[i] == 0 and p != seata and shimmer[i] == 0 and moved == 0:
                                    if p > seata:
                                          if plane3[o][p-1] == "s":
                                                plane3[o][p] = plane4[o][p]
                                                plane3[o][p-1] = str(i+1)
                                          else:
                                                shimmer[i] = 1
                                    elif seata > p:
                                          if plane3[o][p+1] == "s":
                                                plane3[o][p] = plane4[o][p]
                                                plane3[o][p+1] = str(i+1)
                                          else:
                                                shimmer[i] = 1
                                    if plane5[o][p] != "s" and plane5[o][p] != "a" and shimmer[i] == 0:
                                          plane3[o][p] = plane5[o][p]
                                          plane5[o][p] = "s"
                                    moved = 1
                              elif o == seatr and plugload[i] == 0 and p != seata and shimmer[i] == 1 and moved == 0: 
                                    shimmer[i] = 0
                                    if p > seata: 
                                          plane3[o][p] = plane4[o][p]
                                          plane5[o][p-1] = plane3[o][p-1]
                                          plane3[o][p-1] = str(i+1)
                                    elif seata > p:
                                          plane3[o][p] = plane4[o][p]
                                          plane5[o][p+1] = plane3[o][p+1]
                                          plane3[o][p+1] = str(i+1)
                                    if plane5[o][p] != "s" and plane5[o][p] != "a":
                                          plane3[o][p] = plane5[o][p]
                                          plane5[o][p] = "s"
                                    moved = 1
                              #shimmertime = 1
                              if plane3 == plane2:
                                    seated = True
      #enter
      if plane3[0][0] == "a" and bpas <= pn:
            plane3[0][0] = str(bpas)
            bpas += 1
      time += 1
      print(plane3)

print("The total time needed is: " + str(time))


