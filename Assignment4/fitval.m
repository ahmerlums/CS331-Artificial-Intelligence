function [ val ] = fitval( s, t )
    val = sum((t - s) .^ 2);
end

