syms x y z w


maxIter = 100;
errMax = 1e-2;

i = 0;
x_end = input('enter end-eff x');
y_end = input('enter end-eff y');

link1 = input('Enter lenght of link1: ');
link2 = input('Enter lenght of link1: ');
link3 = input('Enter lenght of link1: ');
link4 = input('Enter lenght of link1: ');

F_x_end = link1*cos(x)+link2*cos((x+y)+link3* ...
    cos(x+y+z)+link4*cos(x+y+z+w));

F_y_end = link1*sin(x)+link2*sin((x+y)+link3* ...
    sin(x+y+z)+link4*sin(x+y+z+w));

Jacobian_x = Jacobian(F_x_end, [x, y, z, w]);
Jacobian_y = Jacobian(F_y_end, [x, y, z, w]);

F_x = x_end - F_x_end;
F_y = y_end - F_y_end;
dest_x = guess(1) + inv(Jacobian_x)*F_x;
dest_y = guess(2) + inv(Jacobian_y)*F_y;



