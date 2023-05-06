import random
import sys
import matplotlib.pyplot as plt
import time

#the algorithm is utilized from the floyd warshall algorithm that is located at: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
INF = 10000  # for maxint which is for no connection

def zeroDiagonal(matrix, n, m):
  for i in range(n):
    for j in range(m):
      if i == j:
        matrix[i][j] = 0

def allPairShortestPath(graph, nodeAmount, start, targetStation):
    distanceMatrix = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(nodeAmount):  # intermediate city       
      for i in range(nodeAmount):             
        for j in range(nodeAmount): 
            distanceMatrix[i][j] = min(distanceMatrix[i][j], distanceMatrix[i][k] + distanceMatrix[k][j])
            # If vertex k is on the shortest path from
            # i to j, then take that value otherwise update it to 
            # stay the same
    cityAmount = nodeAmount/2
    matrixPrint(distanceMatrix, int(cityAmount))

    if distanceMatrix[start][targetStation[1]] <= distanceMatrix[start][targetStation[0]]: #train is shorter
      return [distanceMatrix[start][targetStation[1]], 1]

    else:
      return [distanceMatrix[start][targetStation[0]], 0]  #bus is shorter

#     The end result will be something like this
#       1 2 3 4
#     1[0 2 9 8]-> B     The indices 1 and 2 represent the bus and train stations for city 1.
#     2[5 0 8 9]-> T     For example, if we were to go from 1 to 4 (1,4) that would 
#     3[3 1 0 4]-> B     be 9 which stands for starting from city 1's bus station to 
#     4[7 6 1 0]-> T     end on city 2's train station. 
#       | | | |
#       v v v v
#       B T B T

def matrixPrint(distanceMatrix,cityAmount):
  matrixLength = len(distanceMatrix[0])  
  print("Following matrix shows the shortest distances for" , cityAmount , "cities:")
  for i in range(matrixLength):
    printingStr= ""
    for j in range(matrixLength):
      if distanceMatrix[i][j] == INF:
          printingStr+= ("%2s\t" % "INF")
      else:
          printingStr+= ("%2d\t" % (distanceMatrix[i][j]))
      if j == matrixLength - 1:
          printingStr+= ""
    print(printingStr)

runtimes = []
nodeAmount = 8
inputMatrix =       [[0, 11,INF, 4, 13, 24,INF, 27],           #The input matrices can be changed however pleased. There's already a file for test cases.
                     [12, 0,INF, 12, 8, 4,INF, 12],            #This here shows that the code works fine with INF values 
                     [INF,INF,INF,INF,INF,INF,INF,INF],
                     [8, 15,INF, 0, 33, 27,INF, 9],
                     [25, 9,INF, 31, 0, 2,INF, 15],
                     [5, 1,INF, 37, 1, 0,INF, 36],
                     [INF,INF,INF,INF,INF,INF,INF,INF],
                     [16, 19,INF, 5, 7, 9,INF, 0]]

zeroDiagonal(inputMatrix, nodeAmount, nodeAmount)
destinatedStations = [6,7]

startNode = 0
if startNode % 2 == 0:
  startStation = "bus"
else: 
  startStation = "train"
startCity = (startNode // 2) + 1 

  
  
start = time.time()
result = allPairShortestPath(inputMatrix, nodeAmount, startNode, destinatedStations)
if result[1] == 1:
  endStation = "train"
elif result[1] == 0:
  endStation = "bus" 
end = time.time()
runtime = end-start
runtimes.append(runtime)

print("The minimum cost to target City" , "4" + "'s", endStation , "station starting from City", str(startCity) + "'s", startStation ,"station is", result[0])