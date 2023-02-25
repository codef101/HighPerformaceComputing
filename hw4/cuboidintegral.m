% Reset
clear all; 
if isempty(gcp())
    parpool();
end
nworkers = gcp().NumWorkers;
% Integral function
f = @(x,y,z) x.^2 + y.^2 + z.^2;

% cuboid domain
a = -1; b = 1; % x limits
c = -1; d = 1; % y limits
e = -1; f = 1; % z limits

spmd
    xidx = labindex:nworkers:size(a,1)-1;
    yidx = labindex:nworkers:size(c,1)-1;
    zidx = labindex:nworkers:size(e,1)-1;
    
    dx = (b-a)/nworkers;
    dy = (d-c)/nworkers;
    dz = (f-e)/nworkers;
    locint = 0;
    for i = xidx+1
        for j = yidx+1
            for k = zidx+1
                x0 = a + (i-1)*dx; % left point of subinterval along x
                x1 = a + i*dx; % right point of subinterval along x
                y0 = c + (j-1)*dy; % left point of subinterval along y
                y1 = c + j*dy; % right point of subinterval along y
                z0 = e + (k-1)*dz; % left point of subinterval along z
                z1 = e + k*dz; % right point of subinterval along z
                locint = locint + integral3(f, x0, x1, y0, y1, z0, z1); % subinterval integration
            end
        end
    end
    
    totalint = gplus(locint);
end

% Send value to client
totalvalue = totalint{1}
