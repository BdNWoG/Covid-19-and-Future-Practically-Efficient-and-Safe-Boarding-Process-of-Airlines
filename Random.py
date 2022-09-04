import random
import numpy as np

#input for simulation
print("Input: ")
R = float(input("Luggage to carry-on ratio (>0, <1, can be decimals): "))
LT = float(input("Luggage stowing speed (+ve, can be decimals) : "))
L = float(input("Maximum number of luggage (+ve) : "))
times = int(input("Simulation times (+ve, integer only) : "))

#output for simulation
print("Output: ")
print("Model: Random Boarding")
print("Luggage to carry-on ratio = " + str(R))
print("Disobediance rate = N/A")
print("Luggage stowing speed = " + str(LT))
print("Maximum luggage number = " + str(L))
print("Data * " + str(times) + ":")

for i in range(times):
      #empty lists
      passenger = []
      rowlay = []
      plane = []
      plugload = []
      shimmer = []

      #luggage and passenger variables
      a = L / R
      walkingt = 0.889 / (1.18 - 0.08*a)
      luggaget = LT
      time = walkingt
      luggage = L
      pn = 195

      #creating the plane
      aisle = []
      caisle = []
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

      #creating passengers
      for i in range(pn):
            done = False
            while done == False:
                  r = int(random.randint(0, trow-1))
                  c = int(random.randint(0, taisle-1))
                  l = np.random.normal(luggage/2, luggage/4, 1)[0]
                  if l < 0:
                        l = luggage/2
                  if plane2[r+1][c] == 's':
                        a = [i+1, [r+1, c], l]
                        (plane2[r+1])[c] = str(i+1)
                        passenger.append(a)
                        plugload.append(int(0))
                        shimmer.append(int(0))
                        done = True
                  else:
                        done = False

      #luggageloadtime
      for i in range(pn):
            plug = passenger[i][2]
            plugload[i] = int(round(plug * luggaget))
            shimmer[i] = 0

      #simulation core
      bpas = 1
      seated = False
      while seated == False:
            for i in range(pn):
                  moved = 0
                  for o in range(0, trow+1):
                        for p in range(0, taisle):
                              #passnger spawn
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
                                    #move in + shimmering
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
                                    if plane3 == plane2:
                                          seated = True
            #1 unit time
            if plane3[0][0] == "a" and bpas <= pn:
                  plane3[0][0] = str(bpas)
                  bpas += 1
            time += walkingt

      #output time
      print(round(time, 1))

#simulation ending
print("Simulation complete!")
k=input() 
#BdNWoG
