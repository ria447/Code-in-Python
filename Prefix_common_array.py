def findThePrefixCommonArray(A, B):
        C = []
        common = 0
        if A[0] == B[0]:
            common += 1
            C.append(1)
        else:
            C.append(0)
        for i in range(1, len(A)):
            for j in range(i, -1, -1):
                if i != j:
                    if A[j] == B[i]:
                        common += 1
                    if B[j] == A[i]:
                        common += 1
                else:
                    if A[j] == B[i]:
                        common += 1

            C.append(common)
        
        return C

A = [1,3,2,4]
B = [3,1,2,4]
output = findThePrefixCommonArray(A, B)
print(output)

# output: [0,2,3,4]

# explanation: 
# At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4
