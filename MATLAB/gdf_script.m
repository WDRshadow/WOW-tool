clearvars
clc

r = 0.182/2; % Radius of cylinder
rH = 0.233/2; % Radius of Heave plate
d = 0.3895; % Draft of cylinder 
panel_size = 0.035; % Panel size

% calculating draft at a given radius point 

step = 0.001; % defining step
radius_at_z = 0:step:r; % defines radius range
D=(d/r).*sqrt(r^2-radius_at_z.^2); % gives the draft at each radius. You might have to times it by -1


% ------------------------------------------------------------------------
% ceil: Rounds up numbers to the nearest hole number. e.g 3.4 --> 4, 
% -1.9 --> 1

num_panels_up = ceil(d/panel_size); % Number of panels up the cylinder CHANGE

num_panels_around = ceil((2*pi*r)/(panel_size)); % Number of panels around
                                                 % a quarter of the
                                                 % cylinder

num_panels_around_HEAVE_PLATE = ceil((2*pi*r)/(panel_size)); % Number of panels
                                                             % around a quarter of the
                                                             % heave plate


num_panels_radial = ceil(r/panel_size); % Number of panels in the radial direction 

num_panels_radial_HEAVE_PLATE = ceil(rH/panel_size); % Number of panels in the radial direction of heave plate 


% CHANGES - probably doesn't need to be changed

% ------------------------------------------------------------------------

delta_theta = 2*pi/(num_panels_around);
delta_r = r/num_panels_radial; % CHANGE - needs to be a function of the radius
delta_z = d/num_panels_up; % CHANGE - needs to be a function of the depth

delta_theta_HeavePlate = 2*pi/(num_panels_around_HEAVE_PLATE);
delta_r_HeavePlate = rH/num_panels_radial_HEAVE_PLATE; % CHANGE - needs to be a function of the radius


% ------------------------------------------------------------------------



% Open file for storing panel vertices (for use in WAMIT ".gdf" input
% file):
fid=fopen('Column2.gdf','wt'); % the code generates this file

num_panels = 2*num_panels_around*num_panels_radial + num_panels_around*num_panels_up; % total number of panels in the quarter

% all the following lines prints the actual lines in the GDF file
fprintf(fid,'Column2.GDF  --  circular cylinder with heave plate, R=1.05, ILOWHI=0, IRR=1 \n'); 
fprintf(fid,'    1.000000       9.806650     ULEN, GRAV \n');
fprintf(fid,'            0           0       ISX, ISY   \n');
fprintf(fid,'%d \n',num_panels);


% ------------------------------------------------------------------------


% Defining the offset of the column

xoff = 0; % offset the x axis position of the column
yoff = -0.55386; % offset the y axis position of the column
zoff = 0; % offset the z axis position of the column

% Pre-set values of offsets for an equilateral triangle of 3 columns:
% Column 1: xoff = -0.47965; yoff = 0.27694; zoff = 0;
% Column 2: xoff = 0; yoff = -0.55386; zoff = 0;
% Column 3: xoff = 0.47965; yoff = 0.27694; zoff = 0;

% Panelling a quarter of the base of the heave plate:

for n1 = 1:num_panels_around_HEAVE_PLATE
    for n2 = 1:num_panels_radial_HEAVE_PLATE
        x1 = (n2-1)*delta_r_HeavePlate*cos((n1-1)*delta_theta_HeavePlate) + xoff;
        y1 = (n2-1)*delta_r_HeavePlate*sin((n1-1)*delta_theta_HeavePlate) + yoff;
        z1 = -d;
        x2 = (n2-1)*delta_r_HeavePlate*cos(n1*delta_theta_HeavePlate) + xoff ;
        y2 = (n2-1)*delta_r_HeavePlate*sin(n1*delta_theta_HeavePlate) + yoff;
        z2 = -d;
        x3 = n2*delta_r_HeavePlate*cos(n1*delta_theta_HeavePlate) + xoff;
        y3 = n2*delta_r_HeavePlate*sin(n1*delta_theta_HeavePlate) + yoff;
        z3 = -d;
        x4 = n2*delta_r_HeavePlate*cos((n1-1)*delta_theta_HeavePlate) + xoff;
        y4 = n2*delta_r_HeavePlate*sin((n1-1)*delta_theta_HeavePlate) + yoff;
        z4 = -d;
        
        plot3([x1 x2 x3 x4 x1],[y1 y2 y3 y4 y1],[z1 z2 z3 z4 z1],'b')
        hold on
        
        fprintf(fid,'%11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f \n', ...
                x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4);
    end
end


% Panelling a quarter of the side of the cylinder:

for n1 = 1:num_panels_around
    for n2 = 1:num_panels_up
        x1 =  r*cos((n1-1)*delta_theta) + xoff;
        y1 =  r*sin((n1-1)*delta_theta) + yoff;
        z1 = -d + (n2-1)*delta_z;
        x2 =  r*cos(n1*delta_theta) + xoff;
        y2 =  r*sin(n1*delta_theta) + yoff;
        z2 = -d + (n2-1)*delta_z;
        x3 =  r*cos(n1*delta_theta) + xoff;
        y3 =  r*sin(n1*delta_theta) + yoff;
        z3 = -d + n2*delta_z;
        x4 =  r*cos((n1-1)*delta_theta) + xoff;
        y4 =  r*sin((n1-1)*delta_theta) + yoff;
        z4 = -d + n2*delta_z;
        
        plot3([x1 x2 x3 x4 x1],[y1 y2 y3 y4 y1],[z1 z2 z3 z4 z1],'b')
        hold on
        
        fprintf(fid,'%11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f \n', ...
                x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4);
    end
end

% Panelling a quarter of the interior free surface of the cylinder:

for n1 = 1:num_panels_around
    for n2 = 1:num_panels_radial
        x1 = (n2-1)*delta_r*cos((n1-1)*delta_theta) + xoff;
        y1 = (n2-1)*delta_r*sin((n1-1)*delta_theta) + yoff;
        z1 = 0;
        x2 = n2*delta_r*cos((n1-1)*delta_theta) + xoff;
        y2 = n2*delta_r*sin((n1-1)*delta_theta) + yoff;
        z2 = 0;
        x3 = n2*delta_r*cos(n1*delta_theta) + xoff;
        y3 = n2*delta_r*sin(n1*delta_theta) + yoff;
        z3 = 0;
        x4 = (n2-1)*delta_r*cos(n1*delta_theta) + xoff;
        y4 = (n2-1)*delta_r*sin(n1*delta_theta) + yoff;
        z4 = 0;
        
        plot3([x1 x2 x3 x4 x1],[y1 y2 y3 y4 y1],[z1 z2 z3 z4 z1],'r')
        hold on
        
        fprintf(fid,'%11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f \n', ...
                x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4);
    end
end


axis equal