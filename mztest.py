from minizinc import Instance, Model, Solver, instance, result
import collections

def singleMachine():
    njobs = int(input())
    
    p = []
    for _ in range(njobs) :
        p.append(int(input()))
    p.sort()

    model = Model("jobScheduling.mzn")
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

def mysortP(p,w):
    p_ordered = {}
    for i in range(len(p)):
        p_ordered[p[i]]=(p[i]/w[i])
  
    return collections.OrderedDict(sorted(p_ordered.items(), key=lambda x:x[1]))

def mysortW(p,w):
    w_sorted = {}
    for i in range(len(w)):
        w_sorted[w[i]] = (p[i]/w[i])
    
    return collections.OrderedDict(sorted(w_sorted.items(), key=lambda x:x[1]))

def mySort(mapping):
    jobs_sorted = {}

    for i in range(len(mapping)):
        jobs_sorted[i+1] = (mapping[i+1][0] / mapping[i+1][1])

    return list(collections.OrderedDict(sorted(jobs_sorted.items(), key=lambda x:x[1])).keys())


def singleMachineWeight():
    njobs = int(input())
    
    p = []
    for _ in range(njobs) :
        p.append(int(input()))
    
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

    print(p_sorted)
    print(w_sorted)

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

def main():
    #singleMachine()
    singleMachineWeight()

if __name__ == "__main__":
    main()