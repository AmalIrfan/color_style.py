## STYLE ##

styles     = (1,2,4,5,7,8)

## COLOR RANGES ##

dark_for   = range(30,38)
'''Dark Forground Color from 30 to 37'''
dark_back  = range(40,48)
'''Dark Background Color from 40 to 37'''
light_for  = range(90,98)
'''Light Forground Color from 90 to 97'''
light_back = range(100,108)
'''Dark Background Color from 100 to 107'''

## LIST OF COLORS ##
all =[
    [*styles],
    [*dark_for],
    [*dark_back],
    [*light_for],
    [*light_back]
]
'''All the Available Options Of Colors'''

## COLOR FUCNTION ##
def color(*nums):
    """Takes integer inputs and returns
    a color character based on the args
    and return none if none was in the 
    ## COLOR RANGE ##"""
    num_in_op = [False*(a+1) for a in range(len(nums))] #Making a list with an index same as nums, its filled with 0 (False)
    if not nums:return                                  #If nums is empty then returns None
    for num in nums:                                    #Looping through nums
        for i in all:                                   #Looping through all
            if num_in_op[nums.index(num)]:break         #break If this num was already found
            #*print(i)
            for j in i:                                 #Looping through i (individual lists in all i.e. dark_for, etc.)
                if num_in_op[nums.index(num)]:break     #break If this num was already found
                #*print(j)
                if j == num:                            #if j == num then set the correspondind bool True
                    num_in_op[nums.index(num)] = True
                    #*print(0)
    #*print(num_in_op)
    for i in num_in_op:                                 #Looping through entire bool list and return None if any is False
        if not i:return
        else:continue                                   #else continue

    n = ''                                              #Creating a str n from list num
    for i in nums:                                      #Looping through nums
        n += str(i)+';'                                 #Adding semi-colen at the end of each number
    n = n[:-1]                                          #Removing last charecter (';')
    n = nums[0]
    return '\033[%sm'%n                                 #Returning the String

## FIXME:style numbers doesn't like to work ##
print(color(31,42),'Hello, World')
