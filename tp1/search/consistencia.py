
"""
Funciones para probar la consistencia de A*
en los problemas Corners y Food Search
"""

"""
Primero se prueba la admisibilidad de la heuristica
implementada. Para ello se necesita encontrar, para cada
nodo n en el arbol de busqueda, el camino optimo a un 
objetivo desde n. Sea h*(n) el costo de ese camino,
luego se debe verificar que h(n) <= h*(n).
"""

import util

"""
Esta version de BFS es muy similar a la implementada en search.py
excepto que el nodo inicial es pasado como argumento, y no devuelve
el camino encontrado sino su costo (getCostOfActions)
"""
def bfs(problem, start):
    fringe = util.Queue()
    fringe.push((start, list()))
    closed_set = set()
    while not fringe.isEmpty():
        state, actions = fringe.pop()
        if problem.isGoalState(state):
            return problem.getCostOfActions(actions)
        if state not in closed_set:
            closed_set.add(state)
            successors = problem.getSuccessors(state)
            successors = filter(lambda x: x[0] not in closed_set, successors)
            successors = map(lambda x: (x[0], actions+[x[1]]), successors)
            for succ in successors:
                fringe.push(succ)


"""
La funcion que prueba admisibilidad testea, para cada nodo en
el arbol de busqueda, si el costo bfs (optimal) es menor que
el valor de la heuristica en ese nodo. Si se evalua True, se
devuelve False, lo cual implica que la heuristica no es admisible
"""
def admisibilidad(problem, heuristic):
    state = problem.getStartState()
    closed_set = set([state])
    fringe = util.Queue()
    fringe.push(state)
    while not fringe.isEmpty():
        state = fringe.pop()
        optimal = bfs(problem, state)
        if optimal < heuristic(state,problem):
            return False
        else:
            for succ in problem.getSuccessors(state):
                if succ[0] not in closed_set:
                    closed_set.add(succ[0])
                    fringe.push(succ[0])
    return True

            
"""
Para probar la propiedad de consistencia, se debe evaluar la desigualdad
f(padre(n)) <= f(n) para cada nodo n en el arbol de busqueda.
"""
def consistencia(problem, heuristic):
    state = problem.getStartState()
    closed_set = set([state])
    fringe = util.Queue()
    """
    En la cola se guardan tuplas de la forma
    (Estado, g(Estado), f(Estado))
    """
    fringe.push((state,0,heuristic(state,problem)))
    while not fringe.isEmpty():
        state, cost, prevF = fringe.pop()
        for successor in problem.getSuccessors(state):
            if successor[0] not in closed_set:
                h = heuristic(successor[0],problem)
                f = (cost + 1) + h
                if prevF > f:
                    return False
                closed_set.add(successor[0])
                fringe.push((successor[0], cost+1, f))
    return True
                





