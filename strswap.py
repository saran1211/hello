while True:

	print("Enter 'y' for exit.")

	str1 = input("Enter First Str: ")

	str2 = input("Enter Second Str: ")

	if str1 == 'y':

		break

	else:

		temp = str1

		str1 = str2

		str2 = temp

		print("\nString after swapping:")

		print("First String:", str1)

		print("Second String:", str2,"\n")
