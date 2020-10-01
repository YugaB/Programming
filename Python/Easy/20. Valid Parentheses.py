class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mydict = {")":"(", "]":"[", "}":"{" }
   
        for char in s:
            if char in mydict.values():
                stack.append(char)
            elif char in mydict.keys():
                if stack == [] or mydict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
    
#we can also use this way to approach this question     
def check(my_string): 
    brackets = ['()', '{}', '[]'] 
    while any(x in my_string for x in brackets): 
        for br in brackets: 
            my_string = my_string.replace(br, '') 
    return not my_string 
   
# Driver code 
string = "{[]{()}}"
print(string, "-", "Balanced" 
      if check(string) else "Unbalanced") 


# Output::
# {[]{()}} - Balanced
