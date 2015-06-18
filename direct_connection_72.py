from sys import argv 
from sets import Set  
import numpy as np

def length_of_cable(N, ptr_1 = 0, ptr_2 = 2):
    global city_dis_array	# Array having coordinates of cities
    global Pi_array		# Array having population of cities
    global edge_counted		# Set storing connected cities.

    #Handle trivial case of N = 2
    if(N == 2):
	temp1 = city_dis_array[ptr_1] - city_dis_array[ptr_1+1]

	if(temp1 < 0 ):
	    temp1 *= -1
	if( Pi_array[ptr_1] > Pi_array[ptr_1+1]):
	    temp1 *= Pi_array[ptr_1]
	else: 
	    temp1 *= Pi_array[ptr_2]

	return (temp1,1)

    current_edge_cnt    = 0
    total_length	= 0
    #######################################
    #Max possible connections is N*(N-1)/2.
    #every N should connect to N-1 cities.
    #divide by two as each edge will be counted twice
    ######################################
    max_edge_cnt	= N*(N-1)/2
    sub_n		= N/2 + 1

    #Base case is 3 cities with 3 connection
    if (N==3):
	#print "PTR1 : ", ptr_1
	#print "PTR2 : ",  ptr_2
	if (`ptr_1`+`ptr_2` in edge_counted):
	    temp1 = 0
	else:
	    temp1 = city_dis_array[ptr_1] - city_dis_array[ptr_2] 
	    edge_counted.add(`ptr_1`+`ptr_2`)
	    edge_counted.add(`ptr_2`+`ptr_1`)
	    if(temp1 < 0 ):
		temp1 *= -1
	    if( Pi_array[ptr_1] > Pi_array[ptr_2]):
		temp1 *= Pi_array[ptr_1]
	    else: 
		temp1 *= Pi_array[ptr_2]
	    current_edge_cnt += 1

	if (ptr_1+1 < len(city_dis_array)):
	    if (`ptr_1`+`ptr_1+1` in edge_counted):
	        temp2 = 0
	    else:
	        edge_counted.add(`ptr_1`+`ptr_1+1`)
	        edge_counted.add(`ptr_2`+`ptr_1`)
	        temp2 = city_dis_array[ptr_1] - city_dis_array[ptr_1 + 1] 
	        if(temp2 < 0 ):
	            temp2 *= -1
	        if( Pi_array[ptr_1] > Pi_array[ptr_1+1]):
		   temp2 *= Pi_array[ptr_1]
	        else: 
		   temp2 *= Pi_array[ptr_1+1]
		current_edge_cnt += 1

	    if (`ptr_2`+`ptr_1+1` in edge_counted):
	        temp3 = 0	
	    else:
	        edge_counted.add(`ptr_2`+`ptr_1+1`)
	        edge_counted.add(`ptr_1+1`+`ptr_2`)
	        temp3 = city_dis_array[ptr_2] - city_dis_array[ptr_1 + 1] 
	        if(temp3 < 0 ):
		   temp3 *= -1
	        if( Pi_array[ptr_2] > Pi_array[ptr_1+1]):
		   temp3 *= Pi_array[ptr_2]
	        else: 
		   temp3 *= Pi_array[ptr_1+1]
		current_edge_cnt += 1
	else:
	    temp2 = 0
	    temp3 = 0
	return  (temp1 + temp2 + temp3, current_edge_cnt)



    ptr_1		= 0
    ptr_2		= sub_n - 1
    
    ##########################################################################
    #Divide problem of N cities into (N/2 +1) problems of size (N/2+1)
    # Exit condition set by known number of max edges.
    # An edge is a link between two cities.
    ##########################################################################
    while (current_edge_cnt < max_edge_cnt):
	#print "Sub_n: " , sub_n
	#print "ptr1 in while: " , ptr_1 
	#print "ptr2 in while: " , ptr_2 
	#print "current_edge_cnt in while: " , current_edge_cnt 
	#print "max_edge_cnt while: " , max_edge_cnt 
	
	length, cnt = length_of_cable(sub_n, ptr_1, ptr_2)
	total_length += length

	ptr_1 += 1
	ptr_2 += 1
    
	# for wrap arround in city coordinates and population arrays
	if ( ptr_1 == N):
	    ptr_1 = 0
	if ( ptr_2 == N):
	    ptr_2 = 0

	current_edge_cnt += cnt	

    return (total_length, current_edge_cnt)


script, input_file = argv

f = open(input_file) 
T = int(f.readline())


for i in range(0, T):
    N_cities = int(f.readline())
    city_dis_array = [int(x) for x in f.readline().split()]
    Pi_array	   = [int(x) for x in f.readline().split()]
    edge_counted  = set()
    print N_cities
    print city_dis_array
    print Pi_array

    print "Calling length_of_cable() on T = %d" % i
    output,connections = length_of_cable(N_cities)
    print "Length of Cable required (modulo 1,000,000,007 is:" , output%1000000007

f.close

	
    
     
