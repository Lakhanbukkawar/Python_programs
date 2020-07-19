def maxoftwo(p1,p2):
    if p1>p2:
        return p1
    return p2
def max_of_three(p1,p2,p3):
    return maxoftwo(p1,maxoftwo(p2,p3))
print(max_of_three(3,6,7))
