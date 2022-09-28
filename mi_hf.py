import math

# dijkstra algorithm

def dijkstra(gr, start, end):

    answer = {}
    unvisited = []

    for i in gr.keys():
        unvisited.append(i)
        if(start == i):
            answer[i] = 0
            continue
        answer[i] = math.inf

    s = start

    while(len(unvisited)>0):

        for i in gr[s]:
            if(answer[i[0]]==math.inf):
                answer[i[0]] = i[1]+answer[s]
            elif(answer[i[0]]>(i[1]+answer[s])):
                answer[i[0]] = i[1]+answer[s]
                

        unvisited.remove(s)

        minimum = math.inf
        
        for i in unvisited:
            if(answer[i]<minimum):
                minimum = answer[i]
                next_s = i
                
        s = next_s

    return answer[end]

def main():
    
    # beolvasás

    graph = {}
    paths = []
    nodes = {}

    p = int(input())
    n = int(input())
    e = int(input())

    # save the [start node, destination node] pairs in a list

    input().strip("\n")
    
    for i in range(p):
        u = input()
        u = u.split()
        paths.append([int(u[0]), int(u[1])])

    # save the coordinates of the nodes in a dicrionary
    # the key of each node is the ID of it

    input().strip("\n")
    
    for i in range(n):
        u = input()
        u = u.split()
        nodes[i] = [int(u[0]), int(u[1])]

    
    # make a graph dictionary while saving the ID's of the links

    # Each key is the ID of the node (0,1,2...) and each value is a 2d array with the values of
    #[ node ID, distance from the node ] but only if it's linked with the key node
    
    input().strip("\n")

    for i in range(e):
        u = input()
        u = u.split()
        u = [int(u[0]), int(u[1])]
        if not u[0] in graph.keys():
            graph[u[0]] = []
        if not u[1] in graph.keys():
            graph[u[1]] = []

        dist = math.sqrt((nodes[int(u[0])][0]-nodes[int(u[1])][0])**2 + (nodes[int(u[0])][1]-nodes[int(u[1])][1])**2)
        graph[u[0]].append([u[1], round(dist, 2)])
        graph[u[1]].append([u[0], round(dist, 2)])

    # print(graph)

    answers = []

    # run the dijkstra algorithm function for every [start-destination node] pairs
    
    for i in paths:
        answers.append(dijkstra(graph, i[0], i[1]))
        
    print('\t'.join(str(round(s,2)) for s in answers))
    

main()
