# #MAP
# str_lis = ['this','is','a','list','of','strings']

# nw_str = map(lambda x: x + '.',str_lis)      #map(function, iterable_object)
# print(' '.join(nw_str))


# #FILTER
# def re_dot(x):
#   return x != 'list' and x != 'of' 

# fil_str = filter(re_dot,str_lis)
# print(' '.join(list(fil_str)))


#REDUCE
# from functools import reduce      # importing reduce is the most crucial part for using

# print(reduce(lambda x,y: x+y,str_lis))

