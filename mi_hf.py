import math

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
    
    #beolvasás

    graph = {}
    paths = []
    nodes = {}

    path = int(input())
    n = int(input())
    edges = int(input())

    # melyik csúcsok között megy él

    input().strip("\n")
    
    for i in range(path):
        u = input()
        u = u.split()
        paths.append([int(u[0]), int(u[1])])

    # csúcsok koordinátái

    input().strip("\n")
    
    for i in range(n):
        u = input()
        u = u.split()
        nodes[i] = [int(u[0]), int(u[1])]

    # élek
    
    input().strip("\n")

    for i in range(edges):
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

    #print(paths)
    #print(nodes)
    #print(graph)

    answers = []

    for i in paths:
        answers.append(dijkstra(graph, i[0], i[1]))
        
    print('\t'.join(str(round(s,2)) for s in answers))
    

main()
