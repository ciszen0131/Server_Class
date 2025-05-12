# import test_package.test as circle
# import test_package.test_module
from test_package import *

print(test.get_circumference(10))
print(test.get_circle_area(10))

test_module.say_hello("석성택")
test_module.whoareyou()
print(__name__)