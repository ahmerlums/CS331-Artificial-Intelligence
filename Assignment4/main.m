clc
clear all

tar = imresize(imread('tar.jpg'), [50 50]);
tar = tar(:)';

im1 = imresize(imread('img1.jpg'), [50 50]);
im2 = imresize(imread('img2.jpg'), [50 50]);
im3 = imresize(imread('img3.jpg'), [50 50]);
im4 = imresize(imread('img4.jpg'), [50 50]);
im5 = imresize(imread('img5.jpg'), [50 50]);
im6 = imresize(imread('img6.jpg'), [50 50]);

pop = cell(1, 6);
pop{1} = im1(:)';
pop{2} = im2(:)';
pop{3} = im3(:)';
pop{4} = im4(:)';
pop{5} = im5(:)';
pop{6} = im6(:)';

c = 1;
while 1
    % finding fitness value
    vals = [];
    for i = 1:length(pop)
        val = fitval([pop{i}], tar);
        vals = [vals val];
    end

    % replicating best
    [temp, i1] = min(vals);
    vals(i1) = -Inf;
    [temp, i2] = min(vals);
    
    npop = cell(1, 6);
    npop{1} = pop{i1};
    npop{3} = pop{i1};
    npop{5} = pop{i1};
    
    npop{2} = pop{i2};
    npop{4} = pop{i2};
    npop{6} = pop{i2};
    
   
    pop = npop;

    % applying genetic operationg
    pop = geneticop(pop);
    
    c = c + 1;
    
    if mod(c, 2000) == 0
       
       savebest(pop, tar); 
    end
end