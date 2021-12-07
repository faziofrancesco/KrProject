from minizinc import Instance, Model, Solver, instance, result
import collections

def singleMachine(njobs: int, p):
    #print("Inserisci njobs x single machine")
    #njobs = int(input())
    
    #print("Inserisci p x single machine")
    # p = []
    # for _ in range(njobs) :
    #     p.append(int(input()))
    p.sort()

    model = Model("MiniZincModels/jobScheduling_singleMachine.mzn")
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode,model)
    instance['njobs'] = njobs
    instance['p'] = p
    
    result = instance.solve()

    if not result:
        print('NO SOLUTION!')
    else:
        solution = result['c']
        print(solution)
        print("total completion time minimized",sum(solution),"\n")

def mySort(mapping):
    jobs_sorted = {}

    for i in range(len(mapping)):
        jobs_sorted[i+1] = (mapping[i+1][0] / mapping[i+1][1])

    return list(collections.OrderedDict(sorted(jobs_sorted.items(), key=lambda x:x[1])).keys())

def singleMachineWeight():
    print("Inserisci njobs x single machine with weight")
    njobs = int(input())
    
    print("Inserisci p x single machine with weight")
    p = []
    for _ in range(njobs) :
        p.append(int(input()))
    
    print("Inserisci w x single machine with weight")
    w = []
    for _ in range(njobs) :
        w.append(int(input()))
    
    mapping = {}
    for i in range(njobs) :
        mapping[i+1]=(p[i],w[i])

    sorted_jobs = mySort(mapping)

    p_sorted = []
    w_sorted = []

    for i in range(njobs):
        p_sorted.append(mapping[sorted_jobs[i]][0])
        w_sorted.append(mapping[sorted_jobs[i]][1])

    print("p sorted=",p_sorted)
    print("w sorted=",w_sorted)

    model = Model("jobScheduling_singleMachine_weight.mzn")
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode,model)
    instance['njobs'] = njobs
    instance['p'] = p_sorted
    instance['w'] = w_sorted
    
    result = instance.solve()

    if not result:
        print('NO SOLUTION!')
    else:
        solution = result['c']
        print(solution)
        z=0
        for i in range(len(solution)):
            z += solution[i]*w_sorted[i]
        print("total completion time minimized",z,"\n")

def multipleMachine(njobs: int, nmachines: int, p):
    p.sort()

    model = Model("MiniZincModels/jobScheduling_multipleMachine.mzn")
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode,model)
    instance['njobs'] = njobs
    instance['nmachines'] = nmachines
    instance['p'] = p
    
    result = instance.solve()

    if not result:
        print('NO SOLUTION!')
    else:
        solution = result['v']
        print(solution)
        print("total completion time minimized",solution,"\n")

# def main():
#     multipleMachineWeight()

def multipleMachineWeight(njobs: int, nmachines: int, p, w, wMachines):
    
    # print("Inserisci n Jobs x Multiple Machine with weight")
    # njobs = int(input())

    # print("Inserisci n Machines x Multiple Machine with weight")
    # nmachines = int(input())

    # print("Inserisci i pesi sulle macchine x Multiple Machine with weight")
    # wMachines = []
    # for _ in range(nmachines) :
    #     wMachines.append(int(input()))

    # print("Inserisci p x Multiple Machine with weight")
    # p = []
    # for _ in range(njobs) :
    #     p.append(int(input()))
    
    # print("Inserisci w x Multiple Machine with weight")
    # w = []
    # for _ in range(njobs) :
    #     w.append(int(input()))
    
    mapping = {}
    for i in range(njobs) :
        mapping[i+1]=(p[i],w[i])

    sorted_jobs = mySort(mapping)

    p_sorted = []
    w_sorted = []

    for i in range(njobs):
        p_sorted.append(mapping[sorted_jobs[i]][0])
        w_sorted.append(mapping[sorted_jobs[i]][1])

    print("p=",p_sorted)
    print("w=",w_sorted)

    model = Model("MiniZincModels/jobScheduling_multipleMachine_weight.mzn")
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode,model)
    instance['njobs'] = njobs
    instance['nmachines'] = nmachines
    instance['p'] = p
    instance['w'] = w
    instance['wMachines'] = wMachines

    result = instance.solve()

    if not result:
        print('NO SOLUTION!')
    else:
        solution = result['assign']
        sol2 = result['v']
        print(solution)
        print("total completion time minimized",sol2,"\n")

# if __name__ == "__main__":
#     main()