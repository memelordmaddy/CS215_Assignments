#Do the othe rpart involving histogram and try some testcases

def UpdateMean(OldMean, NewDataValue, n, A):
    return (n*OldMean + NewDataValue)/(n+1)

def UpdateMedian(OldMedian, NewDataValue, n, A):
    if(n%2==0):
        if(NewDataValue>=A[n/2] or NewDataValue<=A[n/2-1]):
            if(NewDataValue>=A[n/2]):
                return A[n/2]
            else:
                return A[n/2-1]
        else:
            return NewDataValue
    else:
        if((NewDataValue>=A[n//2] and NewDataValue<=A[n//2 +1]) or (NewDataValue<=A[n//2] and NewDataValue>=A[n//2-1])):
            return (A[n//2]+ NewDataValue)/2
        elif(NewDataValue<A[n//2-1]):
            return (A[n//2]+ A[n//2-1])/2
        else:
            return (A[n//2]+ A[n//2+1])/2
            
def   UpdateStd(OldMean, OldStd, NewMean, NewDataValue, n, A):
    sigma_xsquare_old= ((OldStd**2)+(OldMean**2))*(n-1)
    sigma_xsquare_new = sigma_xsquare_old + (NewDataValue**2)
    new_var= sigma_xsquare_new/(n) - (NewMean**2)
    return new_var**(0.5)
         
            
        