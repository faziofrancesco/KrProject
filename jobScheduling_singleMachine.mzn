int: njobs;
set of int:indices=1..njobs;
array[indices] of int: p;%input tempi di processamento
constraint assert(njobs > 0, "ValueError: njobs must be non-negative");
constraint assert(forall(i in indices)(p[i]>0),"ValueError: p must be non-negative");


array[indices] of var int: c;% tempi di completamento
constraint c[1]=p[1];
set of int: range=2..njobs;
constraint forall(i in range)(c[i]=c[i-1]+p[i]);

solve minimize sum(c);
 
output[ "completion time per jobs = \(c)\n",
"total completion time minimized =\(sum(c))\n"];