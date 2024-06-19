clc;clear all;close all;

I = imread('cameraman.tif');
figure,imshow(uint8(I));

Inoisy = imnoise(I,'salt & pepper',0.1);
[h,w] = size(Inoisy);
B = ones(h,w);
S = zeros(h,w);
%proposed filter application

%Step 1: determining the noisy pixels in the matrix

for i=1:h
    for j=1:w
        if((Inoisy(i,j) == 0) || (Inoisy(i,j) == 255))
            B(i,j) = Inoisy(i,j); 
        else    
        end 
    end
end
%Step 2: Set the binary mask(to detect the position)
for i=1:h
    for j=1:w
        if(B(i,j) ~= 1)
            S(i,j) = 1;
        else
            S(i,j) = 0;
        end
    end
end
figure,imshow(Inoisy),title('before');
k = 3;
fkh = floor(k/2);
fkw = floor(k/2);

U = padarray(Inoisy,[1 1]);
Y = padarray(S,[1,1]);
m = 0;
n = 0;
for r=1:3
    for i=fkh+1:h-fkh
        for j=fkw+1:w-fkw
            if Y(i,j) ~= 0 && k == 3

            for c=1:3
                for e=1:3
                    if c == 2 && e == 2
                        continue
                    else     
                    q = V(c,e)* Z(c,e) * (1/(abs(c-2) + abs(e - 2)));
                    s = Z(c,e) * (1/(abs(c-2) + abs(e - 2)));
                    m = q + m;
                    n = s + n;
                    end
                end
            end
            p = m / n;
            U(i,j) = p;
            end 
        end
    end
end
figure,imshow(uint8(U)),title('after 1');
for r=1:10
    for i=fkh+1:h-fkh
        for j=fkw+1:w-fkw
            if Y(i,j) ~= 0 && k == 3
            V = uceuc(U,i,j);
            Z = uceuc(Y,i,j);
            for c=1:3
                for e=1:3
                    if c == 2 && e == 2
                        continue
                    else     
                    q = V(c,e)* Z(c,e) * (1/(abs(c-2) + abs(e - 2)));
                    s = Z(c,e) * (1/(abs(c-2) + abs(e - 2)));
                    m = q + m;
                    n = s + n;
                    end
                end
            end
            p = m / n;
            U(i,j) = p;
            end 
        end
    end
end

figure,imshow(uint8(U)),title('after 2');
function a = uceuc(b,x,y) 
    v = zeros(3,3);
    v(1,1) = b(x-1,y-1);
    v(1,2) = b(x,y-1);
    v(1,3) = b(x+1,y-1);
    
    v(2,1) = b(x-1,y);
    v(2,2) = b(x,y);
    v(2,3) = b(x+1,y);
    
    v(3,1) = b(x-1,y+1);
    v(3,2) = b(x,y+1);
    v(3,3) = b(x+1,y+1);
    
    a = v;
end


    



