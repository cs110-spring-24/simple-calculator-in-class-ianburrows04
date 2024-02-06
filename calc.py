num1 = int(input("Enter you first number: "))
op = input("Enter your operator: ")
num2 = int(input("Enter your second number: "))

if op == "+" or op == "-" or op == "/" or op == "*" or op == "**" or op == "//" or op == "%":
	if op == "+":
		print(f"{num1} + {num2} = {num1 + num2}")

	elif op == "-":
		print(f"{num1} - {num2} = {num1 - num2}")

	elif op == "*":
		print(f"{num1} * {num2} = {num1 * num2}")

	elif op == "/":
		if num2 == 0:
			print("Cannot divide by zero, the answer is undefined.")
		else:
			print(f"{num1} / {num2} = {num1 / num2}")
	
	elif op == "**":
		print(f"{num1} ** {num2} = {num1 ** num2}")

	elif op == "//":
		if num2 == 0:
			print("Cannot divide by zero, the answer is undefined.")
		else:
			print(f"{num1} // {num2} = {num1 // num2}")
	elif op == "%":
		print(f"{num1} % {num2} = {num1 % num2}")

else:
	print("Invalid operator.")