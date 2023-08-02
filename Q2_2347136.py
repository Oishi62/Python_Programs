li=[3,9,12,15,10,7,8,3,9,10]
div_three=[x for x in li if x%3==0]
not_div_three=[x for x in li if x%3!=0]
print("---------------------------------")
print("QUESTION NUMBER 1")
print("The original list")
print(li)
print("The elements in the list that are divisible by 3 are")
print(div_three)
print("The elements in the list that are not divisible by 3 are")
print(not_div_three)
sq_even=[x*x for x in li if x%2==0]
print("The squares of all the even numbers in the list are ")
print(sq_even)
sum=0
for x in li:
    if(x%2==0):
        sum=sum+x
print("The sum of all the even numbers in the list is")
print(sum)
fin = [] 
[fin.append(x) for x in li if x not in fin] 
print ("The final list where the duplicate elements are removed " + str(fin))
print("---------------------------------")
print("QUESTION NUMBER 2")
birthday={"Soniya Singh":"5 November 1988","Rahul Roy":"7 December 1970","Julia Roberts":"14 January 2001","Shreya Chowdhury":"5th February 2002","Harry Styles":"4th February 1994","Taniya Bala":"24 October 1997"}
def birthDate(name):
    print("The birthdate of ",name," is ",birthday[name])
name=input("Enter the name of the Employee ")
birthDate(name)
print("----------------------------------")
 


