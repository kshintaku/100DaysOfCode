'''
Day 1

Project: Return the volume of a cylinder or truncated cone
Math needed: formulas for cyliner and truncated cone
Edge cases: differentiating cylinder and cone
  sanitizing input
Necessary Expressions:
  Cylinder equation - v= pi*r^2*h
  Truncated cone equation - v= 1/3*pi*(r1^2+r1*r2+r2^2)*h
'''
import math


def calculate_cylinder_volume(radius, height, radius_second = 0):
  if not radius_second:
    return math.pi*height*math.pow(radius, 2)
  else:
    return 1/3*math.pi*(radius**2+radius*radius_second+radius_second**2.0)*height


def test_volume(expected_volume, radius, height, radius_second = 0):
  # Set up a method to perform tests to verify our results
  return '{:.1f}'.format(
    calculate_cylinder_volume(radius, height, radius_second)) == str(expected_volume)


'''
Test 1
Radius: 5
Height: 12
Volume: 942.5
'''
print('Test 1: ' + str(test_volume(942.5, 5, 12)))

'''
Test 2
Radius: 3
Radius_Second: 4
Height: 5
Volume: 193.7
'''
print('Test 2: ' + str(test_volume(193.7, 3, 5, 4)))

'''
Test 3
Radius: 1.5
Height: 4
Volume: 28.27
'''
print('Test 3: ' + str(test_volume(28.3, 1.5, 4)))


'''
Things reviewed in this exercise:
* converting to string with str()
* formatting floats to single decimal
* using math.pow() or ** for exponentials
* formatting floats does automatic rounding (test 3)
* unable to split expressions to multiple lines at comparison (==)
'''