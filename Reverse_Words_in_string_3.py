def reverseWords(s):
        words = s.split()
        reverse = ""

        for i in words:
            reverse += i[::-1]
            reverse += " "
        return reverse.strip()

s = "Let's take LeetCode contest"
output = reverseWords(s)
print(output)

#output = "s'teL ekat edoCteeL tsetnoc"
