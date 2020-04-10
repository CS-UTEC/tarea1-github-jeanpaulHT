def is_palindrome(string):
    for i in range(0, len(string)//2):
        if(string[i] != string[len(string)-i-1]):
            return False;
    return True;

string = input()
if(is_palindrome(string)):
    print("el texto es palindromo")
else:
    print("el texto no es palindromo")
