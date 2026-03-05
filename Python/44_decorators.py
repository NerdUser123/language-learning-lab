# decorators

def decorator(fucn):
    def wrapper():
        print("i am about to exeute a fucntion")
        fucn()
        print("the function executed sucessfully")
    return wrapper

@decorator      # another methond to print 
def Hello():
    print("hello!!!")

Hello()

f = decorator(Hello)

f()



