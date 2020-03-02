import math
class Calculator:


	def add(self, num1, num2):
		return num1 + num2

	def subtract(self, num1, num2):
		return num1 - num2

	def multiply(self, num1, num2):
		return num1 * num2

	def divide(self, num1, num2):
		return num1 / num2

	def square(self, num1):
		return num1 * num1

	def squareroot(self, num1):
		return math.sqrt(num1)


if __name__ == "__main__":
	c=Calculator()
	print("Select operation.")
	print("1.Add")
	print("2.Subtract")
	print("3.Multiply")
	print("4.Divide")
	print("5.Square")
	print("6.Squareroot")

	# Take input from the user
	choice = input("Enter choice:")



	if choice == '1':
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

		print(num1, "+", num2, "=", c.add(num1, num2))

	elif choice == '2':
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

		print(num1, "-", num2, "=", c.subtract(num1, num2))

	elif choice == '3':
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

		print(num1, "*", num2, "=", c.multiply(num1, num2))

	elif choice == '4':
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

		print(num1, "/", num2, "=", c.divide(num1, num2))

	elif choice == '5':
		num = float(input("Enter first number: "))

		print(c.square(num))

	elif choice == '6':
		num = float(input("Enter first number: "))

		print(c.squareroot(num))

	else:
		print("Invalid input")

