
import util

            
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
                





