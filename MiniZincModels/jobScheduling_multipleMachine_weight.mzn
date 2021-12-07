% Use this editor as a MiniZinc scratch book
int: njobs;
int: nmachines;
set of int:jobs=1..njobs;
set of int:machines=1..nmachines;
set of int: dom = 0..1;

array[jobs] of int: p;%input tempi di processamento
array[jobs] of int: w;%input dei pesi
array[machines] of int: wMachines;%input dei pesi sulle macchine

constraint assert(njobs > 0, "ValueError: njobs must be non-negative");
constraint assert(nmachines > 1, "ValueError: machines must be more than one");
constraint assert(nmachines < njobs, "ValueError: machines must be less than jobs");
constraint assert(forall(i in jobs)(p[i]>0),"ValueError: p must be non-negative");
constraint assert(forall(i in indices)(w[i]>0),"ValueError: w must be non-negative");


array[machines,jobs] of var dom: assign;% tempi di completamento

var int: v;
constraint forall(i in machines)(assign[i,i]=1);
constraint forall(j in jobs)(sum(i in machines)(assign[i,j]) = 1);
constraint forall(i in machines)(v>=sum(j in jobs)(assign[i,j]*p[j]+w[j]));

%vincolo sulle macchine che possono processare job con pesi > wMachines[i]
constraint forall(i in machines, j in jobs)(assign[i,j]*w[j] >= wMachines[i]);

solve minimize v;

output[
  show_int(3, assign[i,j]) ++ if j==njobs then "\n" else " " endif | i in machines, j in jobs
];
output["total completion time minimized =\(v)\n"];