function [ pop ] = geneticop( pop )
    % doing crossover
    for i = 1:2:length(pop) - 1
       ov1 = pop{i};
       ov2 = pop{i + 1};
        
       ridx = 1 + round((length(ov1) - 1)*rand());
       nv1 = [ov1(1:ridx) ov2(ridx+1:end)];
       nv2 = [ov2(1:ridx) ov1(ridx+1:end)];
       
       pop{i} = nv1;
       pop{i + 1} = nv2;
    end
    
    % doing mutation
    for i = 1:length(pop)
        mutate = rand();
        
        if mutate > 0.5
            nv = pop{i};
            ridx = 1 + round((length(nv) - 1)*rand());
            nv(ridx) = round(255*rand());
            pop{i} = nv;
        end
    end
end

