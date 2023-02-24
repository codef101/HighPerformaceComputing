clear all; close all;

maxIterations = 1000;
gridSize = 1000;
xlim = [-0.748766713922161, -0.748766707771757];
ylim = [ 0.123640844894862,  0.123640851045266];

% Setup
tic();
x = linspace(xlim(1),xlim(2),gridSize );
y = linspace(ylim(1),ylim(2),gridSize );
[xGrid,yGrid] = meshgrid(x,y);
z0 = xGrid + 1i*yGrid;
count = ones(size(z0));

% Iteration
z = z0;
for n = 0:maxIterations
    z = z.*z + z0; % Main iteration formula
    
    % update color data
    inside = abs(z)<=2;
    count = count + inside;
end
count = log(count);
% Show
cpuTime = toc();
% Plot
set( gcf, 'Position', [200 200 600 600] );
imagesc(x,y,count);
axis image; axis off;
colormap([jet();flipud(jet());0 0 0]); drawnow;
title(sprintf('%1.2fsecs (serial)',cpuTime));