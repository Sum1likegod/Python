# import logging        #logging module which is used to log the errors

# def log_function_call(func):        # decorator
#     def decorated(*arg, **wargs):
#         logging.basicConfig(filename='myapp.log', level=logging.INFO)     #basicconfig is used to store the logs in a file
#         logging.info(f"Calling {func.__name__} with args={arg}, kwargs={wargs}")
#         result = func(*arg, **wargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# # @log_function_call
# def my_function(a, b, a1,b2):
#     return a + b

# print(log_function_call(my_function)(2, 6, a1 = 'A', b2 = 'B'))

def decor(func):
  def inner(*a,**b):  
    print("this is the decoration for the function")
    print(func(*a,**b))
    print("this is after the function has run successfully")
  return inner
# @decor
def sum(A,B):
  return A+B
# decor(sum)()
decor(sum)(2,3)
# sum(2,3)