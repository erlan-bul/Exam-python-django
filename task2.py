

# def is_number(str):
#     try:
#         float(str)
#         return True
#     except ValueError:
#         return False
# a = is_number()
# print(a)

def decor (func):
    def test(a,b):
        try:
            if type(a) == int and type(b) == int:
                func(a,b)
        except ZeroDivisionError:
            print('b == 0')
    return test
@decor
def function(a,b):
    print(a/b)
function(100,25)