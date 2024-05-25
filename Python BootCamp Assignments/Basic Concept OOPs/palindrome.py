class PaliChek:
    def __init__(self,value):
        self.value=value
    
    def is_palindrome(self):
        return self.value == self.value[::-1]
    

number=input("Enter the Number of string: ")

pali=PaliChek(number)

print(pali.is_palindrome())