from search import UndirectedGraph, Edge

def get_graphs(file_name="graphs.txt", verbose=False):
    f = open(file_name)
    lines = [line.strip('\n').strip('\r').split(' ')
             for line in f.readlines() if line != '\n']
    f.close()

    graphs = {}
    g = None
    heuristicDict = None
    recordingHeuristic = False

    for line in lines:
        label = line[0]
        if label == '' or label == 'edges' or label[0] == '#':
            continue
        if recordingHeuristic:
            if label == 'heuristic-end':
                g.set_heuristic(heuristicDict)
                heuristicDict = None
                recordingHeuristic = False
            else: #add entry to heuristicDict
                innerDict = {}
                for kvPair in line[1:]:
                    [key, value] = kvPair.split('-')
                    innerDict[key] = float(value)
                heuristicDict[label] = innerDict
        elif label == 'graph':
            if len(line) != 2:
                raise Exception("invalid graph line. Expected syntax: 'graph graphName'")
            g = UndirectedGraph()
            graphs[line[1]] = g
        elif label == 'nodes':
            if g.nodes != []:
                raise Exception("graph already has nodes list: \n" + str(g))
            g.nodes = line[1:]
        elif label == 'heuristic-start':
            recordingHeuristic = True
            heuristicDict = {}
        else: #assume edge
            if len(line) == 2: #unweighted edge
                g.join(line[0], line[1])
            elif len(line) == 3: #weighted edge
                g.join(line[0], line[1], float(line[2]))
            else:
                raise Exception("invalid edge. Expected syntax: 'startNode endNode'"
                                + "OR 'startNode endNode edgeLength'")        
        if verbose:
            print line

    if verbose:
        for graphName in sorted(graphs.keys()):
            print graphName, ":", graphs[graphName]

    return graphs