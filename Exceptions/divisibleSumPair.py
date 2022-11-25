def divisibleSumPairs(n, k, ar):
    pairC = 0
    
    for i in range(len(ar)):
        
        for j in ar[i+1:]:
            if (ar[i] + j) % k == 0:
                pairC += 1
    
    return pairC
    