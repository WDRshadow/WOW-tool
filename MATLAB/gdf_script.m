% packages
clearvars
clc

% design variables
r = 0.182/2; % Radius of cylinder
rH = 0.233/2; % Radius of Heave plate 
distance_column = 0.96; % Distance between columns
%thickness_hp = 0.03; % Thickness of heave plates
d = 0.3895; % Draft of cylinder
% panel size
panel_size = 0.025; % Panel size

% ------------------------------------------------------------------------
% ceil: Rounds up numbers to the nearest hole number. e.g 3.4 --> 4, 
% -1.9 --> 1

num_panels_z = ceil(d/panel_size); % Number of panels up the cylinder

num_panels_around = ceil((2*pi*r)/(panel_size)); % Number of panels around one circle of the column

num_panels_radial = ceil(r/panel_size); % Number of panels in the radial direction, for free surface and heave plate 

num_panels_around_HEAVE_PLATE = ceil((2*pi*rH)/(panel_size)); % Number of panels around the simplified heave plate

num_panels_radial_HEAVE_PLATE = ceil(rH/panel_size); % Number of panels in the radial direction of heave plate 

% ------------------------------------------------------------------------

delta_z = d/num_panels_z;
delta_theta = 2*pi/(num_panels_around);
delta_r = r/num_panels_radial; 
delta_theta_HeavePlate = 2*pi/(num_panels_around_HEAVE_PLATE);
delta_r_HeavePlate = rH/num_panels_radial_HEAVE_PLATE; 

% ------------------------------------------------------------------------

% Open file for storing panel vertices (for use in WAMIT ".gdf" input
% file):

num_panels = num_panels_radial_HEAVE_PLATE*num_panels_around_HEAVE_PLATE + num_panels_around*num_panels_radial + num_panels_around*num_panels_z; % total number of panels
fid=fopen('wow.gdf', 'wt'); % the code generates this .gdf file
fid2=fopen('wow.cfg', 'wt'); % the code generates this .cfg file

% all the following lines prints the actual lines in the GDF file
fprintf(fid,' !wow.gdf  modified WindFloat, multi column TLP -- ILOWHI=0, fine discretization -- IALTFRC=2 \n'); 
fprintf(fid,'    1.000000       9.806650     ULEN, GRAV \n');
fprintf(fid,'            0           0       ISX, ISY   \n');
fprintf(fid,'%d \n',num_panels*3);
% ------------------------------------------------------------------------

% get dipole panels settings to .cfg file
fprintf(fid2,'!wow.cfg  modified WindFloat, multi column TLP -- ILOWHI=0, fine discretization -- IALTFRC=2 \n'); 
fprintf(fid2,'ipltdat=1 \n');
fprintf(fid2,'ISOR=0 \n');
fprintf(fid2,'ISOLVE=0 \n');
fprintf(fid2,'ISCATT=1 \n');
fprintf(fid2,'ILOG=1 \n');
fprintf(fid2,'IRR=1 \n');
fprintf(fid2,'MONITR=0 \n');
fprintf(fid2,'NUMHDR=1 \n');
fprintf(fid2,'IALTFRC=2 \n');
fprintf(fid2, '%s', ['NPDIPOLE=(1 ', string(3*num_panels_radial_HEAVE_PLATE*num_panels_around_HEAVE_PLATE), ')'] );
% ------------------------------------------------------------------------

% Panelling the base of the heave plate (dipole panels):
for i = 1:3
    if i==1
        xoff = distance_column/2/sqrt(3); yoff = 1*distance_column/2; zoff = 0;
    elseif i==2
        xoff = -1*distance_column/sqrt(3); yoff = 0; zoff = 0;
    else
        xoff = distance_column/2/sqrt(3); yoff = -1*distance_column/2; zoff = 0;
    end 

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
end
    
for i = 1:3
    if i==1
        xoff = distance_column/2/sqrt(3); yoff = 1*distance_column/2; zoff = 0;
    elseif i==2
        xoff = -1*distance_column/sqrt(3); yoff = 0; zoff = 0;
    else
        xoff = distance_column/2/sqrt(3); yoff = -1*distance_column/2; zoff = 0;
    end  
    % Panelling the side of the cylinder:
    
    for n1 = 1:num_panels_around
        for n2 = 1:num_panels_z
            x1 =  r*cos(n1*delta_theta) + xoff;
            y1 =  r*sin(n1*delta_theta) + yoff;
            z1 = -d + (n2)*delta_z;
            x2 =  r*cos((n1-1)*delta_theta) + xoff;
            y2 =  r*sin((n1-1)*delta_theta) + yoff;
            z2 = -d + (n2)*delta_z;
            x3 =  r*cos((n1-1)*delta_theta) + xoff;
            y3 =  r*sin((n1-1)*delta_theta) + yoff;
            z3 = -d + (n2-1)*delta_z;
            x4 =  r*cos(n1*delta_theta) + xoff;
            y4 =  r*sin(n1*delta_theta) + yoff;
            z4 = -d + (n2-1)*delta_z;
            
            plot3([x1 x2 x3 x4 x1],[y1 y2 y3 y4 y1],[z1 z2 z3 z4 z1],'b')
            hold on
            
            fprintf(fid,'%11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f \n', ...
                    x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4);
        end
    end
    
    % Panelling the free surface of the cylinder:
    
    for n1 = 1:num_panels_around
        for n2 = 1:num_panels_radial
            x1 = (n2-1)*delta_r*cos((n1)*delta_theta) + xoff;
            y1 = (n2-1)*delta_r*sin((n1)*delta_theta) + yoff;
            z1 = 0;
            x2 = (n2-1)*delta_r*cos((n1-1)*delta_theta) + xoff;
            y2 = (n2-1)*delta_r*sin((n1-1)*delta_theta) + yoff;
            z2 = 0;
            x3 = n2*delta_r*cos((n1-1)*delta_theta) + xoff;
            y3 = n2*delta_r*sin((n1-1)*delta_theta) + yoff;
            z3 = 0;
            x4 = n2*delta_r*cos(n1*delta_theta) + xoff;
            y4 = n2*delta_r*sin(n1*delta_theta) + yoff;
            z4 = 0;
            
            plot3([x1 x2 x3 x4 x1],[y1 y2 y3 y4 y1],[z1 z2 z3 z4 z1],'r')
            hold on
            
            fprintf(fid,'%11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f \n', ...
                    x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4);
        end
    end

%     % Panelling the bottom surface of the cylinder:
%     
%     for n1 = 1:num_panels_around
%         for n2 = 1:num_panels_radial
%             x1 = (n2-1)*delta_r*cos((n1)*delta_theta) + xoff;
%             y1 = (n2-1)*delta_r*sin((n1)*delta_theta) + yoff;
%             z1 = -d;
%             x4 = (n2-1)*delta_r*cos((n1-1)*delta_theta) + xoff;
%             y4 = (n2-1)*delta_r*sin((n1-1)*delta_theta) + yoff;
%             z4 = -d;
%             x3 = n2*delta_r*cos((n1-1)*delta_theta) + xoff;
%             y3 = n2*delta_r*sin((n1-1)*delta_theta) + yoff;
%             z3 = -d;
%             x2 = n2*delta_r*cos(n1*delta_theta) + xoff;
%             y2 = n2*delta_r*sin(n1*delta_theta) + yoff;
%             z2 = -d;
%             
%             plot3([x1 x2 x3 x4 x1],[y1 y2 y3 y4 y1],[z1 z2 z3 z4 z1],'b')
%             hold on
%             
%             fprintf(fid,'%11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f \n', ...
%                     x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4);
%         end
%     end
    
end

axis equal