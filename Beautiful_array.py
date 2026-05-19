#An array is beautiful if two adjacent integers, arr[i] and arr[i+1] are either negative or positive. You can do the following operation any number of times until the array becomes beautiful.
#If two adjacent are different i.e. one of them is negative and other is positive, remove them. 

def makeBeautiful(arr):
        
        result = []
        
        for num in arr:
            if result and (((result[-1] >= 0) and (num < 0)) or ((result[-1] < 0) and (num >= 0))):
                result.pop()
                
            else:
                result.append(num)
                
        
        return result

arr[] = [4, 2,-2, 1]
output = makeBeautiful(arr)
print(output)
