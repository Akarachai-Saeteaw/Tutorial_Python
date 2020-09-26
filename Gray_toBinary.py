#Create list for collect data
collect = []
collect_2 = []

#def function for change form input to binary
def perms(n):
    global collect
    word = ""
    if not n:
        return

    for i in range(2**n):
        s = bin(i)[2:] #change i from number to binary
        word = "0" * (n-len(s)) + s # Create 00 to front of binary
        collect.append(word)
        yield s # Show result

#change binary to gray
def xor_c(a, b): 
    return '0' if(a == b) else '1'; 
  
def flip(c): 
    return '1' if(c == '0') else '0'; 
  
def binarytoGray(binary): 
    gray = ""; 
    gray += binary[0]; 

    for i in range(1, len(binary)): 
          
        # Concatenate XOR of previous  
        # bit with current bit 
        gray += xor_c(binary[i - 1],  
                      binary[i]); 
  
    return gray; 

user = int(input()) #input from user (int)
list(perms(user))

#for loop show data
for i in range(len(collect)):
  collect_2.append(binarytoGray(collect[i]))
print(collect_2)
