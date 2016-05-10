function [ pop ] = savebest( pop, tar )
    vals = [];
    for i = 1:length(pop)
        val = fitval([pop{i}], tar);
        vals = [vals val];
    end
    
    disp(vals)
    
    [temp, idx] = min(vals);
    best = pop{idx};
   
    disp(size(best));    
    imshow(reshape(best, [50 50 3]));
    pause;
end

