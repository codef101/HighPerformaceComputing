% Reset
clear all; close all;
if isempty(gcp())
    parpool();
end

nworkers = gcp().NumWorkers;
maxIterations = 1000;
gridSize = 1000;
chunks = sqrt(nworkers);
xlim = [-0.748766713922161, -0.748766707771757];
ylim = [ 0.123640844894862,  0.123640851045266];

% split xlim and ylim into chunks subintervals
x = linspace(xlim(1),xlim(2),chunks+1);
y = linspace(ylim(1),ylim(end),chunks+1);

% On the workers
% Setup
tic();
spmd
    % Define subgrid
    xsub = linspace(x(labindex()),x(labindex()+1),gridSize/chunks);
    ysub = linspace(y(mod(labindex()-1,chunks)+1),y(mod(labindex(),chunks)+1),gridSize/chunks);
    [xGrid,yGrid] = meshgrid(xsub,ysub);
    z0 = xGrid + 1i*yGrid;
    count = ones(size(z0));
    
    % Calculate
    z = z0;
    for n = 0:maxIterations
        z = z.*z + z0;
        inside = abs( z )<=2;
        count = count + inside;
    end
    count = log(count);
end

% On the client
% Show
cpuTime = toc();
set( gcf,'Position',[200 200 600 600] );
imagesc(cat(2,xGrid{:}),cat(1,yGrid{:}),cat(1,count{:}));
axis image; axis off;
colormap([jet();flipud(jet());0 0 0]); drawnow;
title( sprintf('%1.2fsecs (with spmd)',cpuTime));
