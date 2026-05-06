def reverseWords(s):
        reverse = ""
        words = s.split()
        print(words)

        for word in words[-1::-1]:
            reverse += word
            reverse += " "
        
        return reverse.strip()

s = "the sky is blue"
output = reverseWords(s)
print(output)

#output = "blue is sky the"
