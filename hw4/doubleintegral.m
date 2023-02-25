clear all;

if isempty(gcp())
    parpool();
end

nworkers = gcp().NumWorkers;

f = @(x,y) x.^2 + y.^2;

% Rectangular domain
a = -1; b = 1; % x limits
c = -1; d = 1; % y limits

spmd
    xidx = labindex:nworkers:size(a,1)-1;
    yidx = labindex:nworkers:size(c,1)-1;
    dx = (b-a)/nworkers;
    dy = (d-c)/nworkers;
    locint = 0;
    for i = xidx+1
        for j = yidx+1
            x0 = a + (i-1)*dx; % left point of subinterval along x
            x1 = a + i*dx; % right point of subinterval along x
            y0 = c + (j-1)*dy; % left point of subinterval along y
            y1 = c + j*dy; % right point of subinterval along y
            locint = locint + integral2(f, x0, x1, y0, y1); % subinterval integration
        end
    end
    
    totalint = gplus(locint);
end

% Send value to client
totalvalue = totalint{1}
