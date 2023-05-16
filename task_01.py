def is_palindrome(string):

    if (isinstance(string, str) ) == True:
        import re

        string = re.split(", | |-|'|:|!", string)
        string_1 = []

        for i in string:
            i = i.lower()
            string_1 +=i
    
        return (string_1 == list(reversed(string_1)))

    else:
        if (isinstance(string, str) ) == False: 
            string = str(string)
            string_1 = string[::-1]
            
            return (string_1 == string)
            
is_palindrome("A man, a plan, a canal -- Panama")
is_palindrome("Madam, I'm Adam!")
is_palindrome(333)
is_palindrome(None)
is_palindrome("Abracadabra")

