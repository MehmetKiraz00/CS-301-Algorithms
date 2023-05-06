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
    for k in range(nodeAmount):        
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
  print("Following matrix shows the shortest distances for" , cityAmount , "cities:")
  print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in distanceMatrix]))

city_amounts = [10, 15, 20, 25, 30, 35, 40, 45, 50]
runtimes = []
for i in city_amounts:
  cityAmount = i
  nodeAmount = 2*cityAmount
  inputMatrix = [[random.randint(1, 50) for i in range(nodeAmount)] for j in range(nodeAmount)]
  zeroDiagonal(inputMatrix, nodeAmount, nodeAmount)

  destinatedStations = [2*(i-1), 2*(i-1)+1] #go to the end index for train and end-1 for the bus as showed above. This can be assigned as random but not necessary

  startNode = random.randint(0, (2*i)-1) #for test purposes start from a random station of a random city 

  if startNode % 2 == 0:
    startStation = "bus"
  else: 
    startStation = "train"
  startCity = (startNode // 2) + 1 

  startTime = time.time()
  result = allPairShortestPath(inputMatrix, nodeAmount, startNode, destinatedStations)
  if result[1] == 1:
    endStation = "train"
  elif result[1] == 0:
    endStation = "bus" 
  endTime = time.time()
  runtime = endTime-startTime
  runtimes.append(runtime)

  print("The minimum cost to target City" , str(i) + "'s", endStation , "station starting from City", str(startCity) + "'s", startStation ,"station is", result[0])

plt.plot(city_amounts, runtimes, linewidth=2.5)
plt.xlabel('Number of Cities')
plt.ylabel('Runtimes with Dynamic Programming Algorithm')
plt.show()