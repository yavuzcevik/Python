# -*- coding: utf-8 -*-

"""
Programmer : Halil Yavuz Çevik - Galatasaray University/Istanbul

Main goal of this programme : 
    1-) Generating two 3x3 matrix and calculating basic operations between them. 
    2-) Converting results to IEEE 754 single-precision floating-point format.

For more information you may visit the following links:
    1-) https://en.wikipedia.org/wiki/IEEE_floating_point
    2-) https://en.wikipedia.org/wiki/IEEE_754-1985
    3-) https://en.wikipedia.org/wiki/Single-precision_floating-point_format
    4-) https://www.h-schmidt.net/FloatConverter/IEEE754.html
    
"""   
import numpy as np 


def sp_decimal_to_ieee754(x):
    # Main steps of this algorithm:
    #    1-) Calculating the sign of the number
    #    2-) Calculating the fraction & exponent(decimal)
    #    3-) Calculating the exponent in binary form
    #    5-) Calculating the result(32 bit)
    # x equal to : ((-1)**signe)*(decimal_temp)*(2**exponent)
     
    #Calculating sign of the x
    if x>0 :
        sign=0
        
    if x<0 :
        sign=1
        x=-x
   
    #Initialization and assignment of bias
        # We are splitting integer and float part of the number.
        # binary_fraction_integer list will be including the integer part of the number in binary format
        # binary_fraction_float list will be including the float part (right part of the comma) of the number in binary format
        # binary_fraction list will be including the x in binary format
        # binary_exponent list will be including the exponent ( which is equal to sign+bias) in binary format
        # x_ieee754 list will be including the IEEE754 form of the decimal x 
        # We are taking the bias for the single precision as 127
    bias = 127
    exponent=0
    x_integer_part=int(x-(x%1))
    x_float_part=x-(x_integer_part)
    float_temp=x_float_part
    integer_temp=x_integer_part
    binary_fraction_integer=[]
    binary_fraction_float=[]
    binary_fraction=[]
    binary_exponent=[]
    x_ieee754=[]
    
    #conversion of the integer part of x to binary form.
    if x_integer_part>0:
       while True:
             if len(binary_fraction_integer)>22:
                 break
             binary_fraction_integer.append(integer_temp%2)
             integer_temp=int(integer_temp/2)
             
             
             if integer_temp==0:
                 break
    # We used append() method hence the list will be inverse. We must reverse the list
    binary_fraction_integer.reverse()
   
    #conversion of the float part of x to binary form.
    while True:
        if len(binary_fraction_float)>22:
            break
        binary_fraction_float.append(int(float_temp*2))
        float_temp=float_temp*2
        if(float_temp>=1.0):
            float_temp=float_temp%1
        if(float_temp==0.0):
            break
   
    # if the integer part of the x is greater than 0, we carry the binary numbers from fraction_integer list to fraction list
    if len(binary_fraction_integer)>0:
        exponent=len(binary_fraction_integer)-1
        
        while True:
            if len(binary_fraction_integer)==1:
                break
            
            binary_fraction.append(binary_fraction_integer.pop(-(len(binary_fraction_integer)-1)))
        
        binary_fraction=binary_fraction+binary_fraction_float

    #Finding fraction and exponent
    if len(binary_fraction_integer)==0:
        float_temp=x_float_part
       #Finding exponent
        while True:
            float_temp = float_temp*2
            exponent=exponent-1
            if float_temp>=1:
                break
        
        #Carrying numbers from fraction_float list to fraction list and adding them right behind the integer part.
        if len(binary_fraction_float)>2:
            while True:
                if len(binary_fraction_float)==23:
                    break
                binary_fraction_float.append(0)
                
         #We are adding and additional ',' character for separating integer part from float part in binary form.
            binary_fraction_float.insert(-exponent,',')
            while True:
                if(binary_fraction_float[len(binary_fraction_float)-1]==','):
                    break
                binary_fraction.append(binary_fraction_float.pop(-1))
           
            binary_fraction.reverse()
        # This if aiming a special condition like 0.25(decimal)=1.0x2^-2(binary)    
        if len(binary_fraction_float)==2:
            for a in range(1,23):
                binary_fraction.append(0)        
    
    # Fraction part of the ieee754 for of the x will be 23 bit thus we must delete the numbers which pass beyond 23 bit.
    if len(binary_fraction)>23:
        while True:
            if len(binary_fraction)!=23:
                 del binary_fraction[-1]
            else:
                break
    
    if len(binary_fraction)<23:
        while True:
            if len(binary_fraction)!=23:
                binary_fraction.append(0)
            else:
                break
            
    #Calculating Bias & exponent in binary form 

    bias=bias+exponent
    bias_temp=bias       
    while True:
        binary_exponent.append(bias_temp%2)
        bias_temp=int(bias_temp/2)
        if bias_temp==0:
            break
    while True:
        if len(binary_exponent)==8:
            break
        binary_exponent.append(0)
    binary_exponent.reverse()
    
    # X in IEEE-754 is equal to : sign + exponent + fraction 
    x_ieee754.append(sign)
    x_ieee754=x_ieee754+binary_exponent+binary_fraction
    
    
    
    
    # Following comment lines are just for the correction. You can see the values of parameters if you want to.

    #print('SIGN:',sign)
    #print('BIAS:',bias)
    #print('BIAS_BINARY:',binary_exponent)       
    #print('EXPONENT',exponent)    
    #print(binary_fraction_integer)
    #print(binary_fraction_float)
    #print('FRACTION:',binary_fraction)
    #print('X : ',x_ieee754)
   
    #Converting x_ieee754 list to integer ( final result).
    x=map(str, x_ieee754)
    x=''.join(x)
    return x
    
#Some examples for understanding.
#print(sp_decimal_to_ieee754(12.375))
#print(sp_decimal_to_ieee754(-12.375))
#print(sp_decimal_to_ieee754(0.375))
#print(sp_decimal_to_ieee754(0.25))
#print(sp_decimal_to_ieee754(0.1))
#print(sp_decimal_to_ieee754(0.48018187))

matrix_sum=np.zeros((3,3),dtype=float)
matrix_sub=np.zeros((3,3),dtype=float)
matrix_mul=np.zeros((3,3),dtype=float)
matrix_div=np.zeros((3,3),dtype=float)

#Generating random float numbers and assigning them to matrices.
matrix_A=np.random.uniform(0,10,(3,3))
matrix_B=np.random.uniform(0,10,(3,3))

print('Matrix A\n',matrix_A,'\n')
print('Matrix B\n',matrix_B,'\n')

print('Addition 2 Matrices')
for x in range(0,3):
    for y in range(0,3):
        print('Matrix A',x+1,y+1,'+ Matrix B',x+1,y+1,'=',matrix_A[x,y]+matrix_B[x,y],'(Decimal Format)')
        print('Same result in IEEE-754 format : ',sp_decimal_to_ieee754(matrix_A[x,y]+matrix_B[x,y]))
        matrix_sum[x,y]=sp_decimal_to_ieee754(matrix_A[x,y]+matrix_B[x,y])
        print('')
print('')
print('A+B Sonuc:')
print(matrix_sum)
print('')
print('')       
print('Subtraction of 2 Matrices')

for x in range(0,3):
    for y in range(0,3):
        print('Matrix A',x+1,y+1,'- Matrix B',x+1,y+1,'=',matrix_A[x,y]-matrix_B[x,y],'(Decimal Format)')
        print('Same result in IEEE-754 format : ',sp_decimal_to_ieee754(matrix_A[x,y]-matrix_B[x,y]))
        matrix_sub[x,y]=sp_decimal_to_ieee754(matrix_A[x,y]-matrix_B[x,y])
        print('')

print('')
print('A-B Sonuc:')
print(matrix_sub)
print('')
print('')          
print('Multiplication 2 Matrices')
for x in range(0,3):
    for y in range(0,3):
        print('Matrix A',x+1,y+1,'* Matrix B',x+1,y+1,'=',matrix_A[x,y]*matrix_B[x,y],'(Decimal Format)')
        print('Same result in IEEE-754 format : ',sp_decimal_to_ieee754(matrix_A[x,y]*matrix_B[x,y]))
        matrix_mul[x,y]=sp_decimal_to_ieee754(matrix_A[x,y]*matrix_B[x,y])
        print('')
print('')
print('A*B Sonuc:')
print(matrix_mul)
print('')
print('')  
print('Division 2 Matrices')
for x in range(0,3):
    for y in range(0,3):
        print('Matrix A',x+1,y+1,'/ Matrix B',x+1,y+1,'=',matrix_A[x,y]/matrix_B[x,y],'(Decimal Format)')
        print('Same result in IEEE-754 format : ',sp_decimal_to_ieee754(matrix_A[x,y]/matrix_B[x,y]))
        matrix_div[x,y]=sp_decimal_to_ieee754(matrix_A[x,y]/matrix_B[x,y])
        print('')
print('A/B Sonuc:')
print(matrix_div)       

