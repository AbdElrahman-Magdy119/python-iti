import math
def calculate_area(*shape):
  if shape[0].lower() == "triangle":
    area = (shape[1] * shape[2]) / 2
    print(f"The area of triangle is {area}.")
  elif shape[0].lower() == "rectangle":
    area = shape[1] * shape[2]
    print(f"The area of rectangle is {area}.")
  elif shape[0].lower() == "square":
    area = shape[1] ** 2
    print(f"The area of rectangle is {area}.")
  elif shape[0].lower() == "circle":
    area = math.pi * shape[1] ** 2
    print(f"The area of circle is {area}.")
  else:
    print("Invalid shape.")
