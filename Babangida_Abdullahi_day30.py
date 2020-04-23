def nester(n):
    """Given a string of digits S, This function inserts a minimum number of opening and closing parentheses into it such that the resulting
string is balanced and each digit d is inside exactly d pairs of matching parentheses.Let the nesting of two parentheses within a string be
the substring that occurs strictly between them. An opening parenthesis and a closing parenthesis that is further to its right
are said to match if their nesting is empty, or if every parenthesis in their nesting matches with another parenthesis in their nesting.
The nesting depth of a position p is the number of pairs of matching parentheses m such that p is included in the nesting of m.
"""
    if type(n) is not str:
        return "Parameter must be in string"
    for t in n:
        if t not in "0123456789":
            return "Parameters must be numbers and greater than zero"
    if len(n)==1:
        return "("*int(n)+n+")"*int(n)
    no=list(n)
    u=no
    no[0]="("*int(no[0])+no[0]
    no[-1]=no[-1]+")"*int(no[-1])
    num=[int(i) for i in list(n)]
    diff=[int(num[i])-int(num[i+1]) for i in range(len(no)-1)]
    for d in range(len(diff)):
        if diff[d]>0:
            u[d]=u[d]+")"*diff[d]
        if diff[d]<0:
            u[d]=u[d]+"("*abs(diff[d])
    return "".join(u)
#test cases
print(nester("-111000"))
print(nester("4512"))
print(nester("000"))
print(nester("302"))
