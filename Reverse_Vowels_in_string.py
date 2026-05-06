def reverseVowels(s):
        vowel = []
        for i in s:
            if i in 'AEIOUaeiou':
                vowel.append(i)

        reverse = ""

        for char in s:
            if char in 'AEIOUaeiou':
                reverse += vowel.pop()
            else:
                reverse += char

        return reverse

s = "IceCreAm"
output = reverseVowels(s)
print(output)

#output = "AceCreIm"
