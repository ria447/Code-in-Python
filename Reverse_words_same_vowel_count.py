def reverseWords(s):
        
        words = s.split()
        altered_string = words[0] 
        
        vow_count = 0

        for i in words[0]:
            if i in 'aeiou':
                vow_count += 1

        for i in range(1, len(words)):
            count = 0
            for j in words[i]:
                if j in 'aeiou':
                    count += 1
                
            if count == vow_count:
                altered_string += " "
                altered_string += words[i][::-1]
                
                
            else:
                altered_string += " "
                altered_string += words[i]

        return altered_string

s = "cat and mice"
output = reverseWords(s)
print(output)

#output = "cat dna mice"
