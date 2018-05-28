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

