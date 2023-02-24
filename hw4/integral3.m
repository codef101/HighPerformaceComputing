close all; clear all; clc;
% I want to do this triple integral using SPMD
fun = @(x,y,z) z
totalval_s = integral3(fun,0,4,0,4,0,4)
% So I know the answer is 128, and integral3 works well
%
% Now I want to do the same triple integral but using SPMD
% Create a parallel pool if none exists
if isempty(gcp())
    parpool();
end
nworkers = gcp().NumWorkers;
% Define the function
f = @(x,y,z) z
% Discretize the interval on the client
x = linspace(0,4,nworkers+1)
y = linspace(0,4,nworkers+1)
z = linspace(0,4,nworkers+1)

% On the workers
spmd
    ainit = x(labindex()) %left point of subinterval
    bfin =  x(labindex()+1) %right point of subinterval
    cinit = y(labindex()) 
    dfin =  y(labindex()+1)
    einit = z(labindex()) 
    ffin =  z(labindex()+1)
    locint = integral3(f,ainit,bfin,cinit,dfin,einit,ffin) % subinterval integration
    totalint = gplus(locint) % Add all values.
end
% Send the value back the client
totalvalue_spmd = totalint{1}
% However, the answer, totalvalue_spmd = 32, is incorrect. 
% I am novice at using SPMD, need help troubleshooting what I did wrong