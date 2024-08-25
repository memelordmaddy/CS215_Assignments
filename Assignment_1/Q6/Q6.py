def UpdateMean(OldMean, NewDataValue, n, A):
    return (n*OldMean + NewDataValue)/(n+1)

def UpdateMedian(OldMedian, NewDataValue, n, A):
    if(n==1):
        return (OldMedian + NewDataValue)/2
    if(n==0):
        return NewDataValue
    if n % 2 == 0:
        if NewDataValue<A[n//2-1]:
            return A[n//2-1]
        elif NewDataValue>A[n//2]:
            return A[n//2]
        else:
            return NewDataValue
    else:
        mid = n // 2
        if NewDataValue>=A[mid] and NewDataValue <= A[mid+1]:
            return (A[mid]+ NewDataValue)/2
        elif NewDataValue<=A[mid] and NewDataValue >= A[mid-1]:
            return (A[mid] + NewDataValue)/2
        elif A[mid]<NewDataValue:
            return (A[mid]+ A[mid+1])/2
        else:
            return (A[mid]+ A[mid-1])/2
        
import math      
def UpdateStd(OldMean, OldStd, NewMean, NewDataValue, n, A):
    n=float(n)
    OldMean= float(OldMean)
    OldStd= float(OldStd)
    NewDataValue= float(NewDataValue)
    NewMean= float(NewMean)
    sigma_xsquare_old= (pow(OldStd, 2))*(n-1) + (pow(OldMean,2))*(n)
    sigma_xsquare_new = sigma_xsquare_old + (pow(NewDataValue, 2))
    new_var= (sigma_xsquare_new- (pow(NewMean, 2))*(n+1))/(n)
    return math.sqrt(new_var)
         