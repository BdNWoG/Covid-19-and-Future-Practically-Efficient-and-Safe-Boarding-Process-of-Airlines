import random
import numpy as np

print("Input: ")
R = float(input("Luggage to carry-on ratio (>0, <1, can be decimals) (default = 0.9): "))
D = float(input("Disobediance rate: (>0, <100, can be decimals) (default = 5): "))
LT = float(input("Luggage stowing speed (+ve, can be decimals) (default = 5.55): "))
L = float(input("Maximum number of luggage (+ve) (default = 2): "))
times = int(input("Simulation times (+ve, integer only) (default = 100): "))

print("Output: ")
print("Model: Boarding by Section Back to Front Row by Row Optimized")
print("Luggage to carry-on ratio = " + str(R))
print("Disobediance rate = " + str(D))
print("Luggage stowing speed = " + str(LT))
print("Maximum luggage number = " + str(L))
print("Data * " + str(times) + ":")

for i in range(times):
      passenger = []
      rowlay = []
      plane = []

      #set walking time
      a = L / R
      walkingt = 0.889 / (1.18 - 0.08*a)
      luggaget = LT

      time = walkingt

      aisle = []
      caisle = []
      a = 1
      b = 0
      c = 0
      #trow = int(input("total rows: "))
      trow = 33
      aisle = [3, 3]
      caisle = [3]

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
      plane += [["s", "s", "s", "a", "a", "a", "a"]]

      for i in range(trow-1):
            plane += [rowlay]

      #print(plane)

      #luggage = int(input("allowed luggage: "))
      #set luggage
      luggage = L
      #pn = int(input("number of passengers: "))
      pn = 195

      #print(plane)

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
      #here! row by row
      for j in range(32):
            for i in range(6):
                  done = False
                  while done == False:
                        r = trow - j - 1
                        c = i
                        if c > 2:
                              c = 9 - i
                        l = np.random.normal(luggage/2, luggage/4, 1)[0]
                        if l < 0:
                              l = luggage/2
                        if plane2[r+1][c] == 's':
                              a = [i+6*j+1, [r+1, c], l]
                              (plane2[r+1])[c] = str(i+1+6*j)
                              passenger.append(a)
                              plugload.append(int(0))
                              shimmer.append(int(0))
                              done = True
                        else:
                              done = False
      for i in range(3):
                  done = False
                  while done == False:
                        r = 1 - 1
                        c = i
                        if c > 2:
                              c = 9 - i
                        l = np.random.normal(luggage/2, luggage/4, 1)[0]
                        if l < 0:
                              l = luggage/2
                        if plane2[r+1][c] == 's':
                              a = [i+192+1, [r+1, c], l]
                              (plane2[r+1])[c] = str(i+192+1)
                              passenger.append(a)
                              plugload.append(int(0))
                              shimmer.append(int(0))
                              done = True
                        else:
                              done = False
      #print(plane2)
      #mn = int(input("Messiness rate: "))
      mn = D
      messy = round(mn/100*pn)

      for i in range(messy):
            q = random.randint(0, pn-1)
            r = random.randint(0, pn-1)
            temp = passenger[q]
            passenger[q] = passenger[r]
            passenger[r] = temp
            for o in range(trow+1):
                  for p in range(taisle):
                        if plane2[o][p] == str(q+1):
                              fr = o
                              fa = p
            for o in range(trow+1):
                  for p in range(taisle):
                        if plane2[o][p] == str(r+1):
                              sr = o
                              sa = p
            temp = plane2[fr][fa]
            plane2[fr][fa] = plane2[sr][sa]
            plane2[sr][sa] = temp

      #luggageloadtime
      for i in range(pn):
            plug = passenger[i][2]
            plugload[i] = int(round(plug * luggaget))
            shimmer[i] = 0

      #print(passenger)

      bpas = 1

      seated = False
      while seated == False:
      #while time < 1300:
            #print("Time: " + str(time))
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
            time += walkingt
            #print(plane3)

      print(round(time, 1))

print("Simulation complete!")
k=input() 
#BdNWoG
