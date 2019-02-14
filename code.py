import math
import os

def hello(a_name):
	print("Hello! " + a_name)
	

def hello2(name_a, name_b):
	print("Hello! " + name_a + " and " + name_b)


def sum_two(x,y):
	z = x + y
	return z


def circle_area(radius):
    return radius**2*math.pi


def my_sum(a_list):
	total = 0
	for n in a_list:
		total = total + n
	return total


def my_prod(a_list):
	total = 1
	for n in a_list:
		total = total * n
	return total


def my_count(a_list):
	total = 0
	for n in a_list:
		total = total + 1
	return total


def my_count_less_5(a_list):
	count = 0
	for n in a_list:
		if n < 5:
			count = count + 1
	return count


def my_count_ones(a_list):
	count = 0
	for n in a_list:
		if n == 1:
			count = count + 1
	return count


def is_list_empty(a_list):
	if my_count(a_list)==0:
		return True
	else:
		return False


def my_max(a_list):
	if is_list_empty(a_list):
		return None
	b = a_list[0]
	for n in a_list:
		if n > b:
			b = n
	return b

def get_filenames(a_dirname):
	list_of_files = os.listdir(a_dirname)
	all_files = []
	for n in list_of_files:
		full_path = os.path.join(a_dirname,n)
		if not os.path.isdir(full_path):
			all_files.append(full_path)
	return all_files



def flatten(a_list_with_lists):
	new_list = []
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				new_list.append(i)
		else:	
			new_list.append(n)
	return a_list


def print_right(a_list_with_lists):
	new_list = []
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				print(i, end ="")
		else:
			print(n, end = "")
		print()


def single_row_stars(number):
	for n in range(number):
		print("*",end = "")

def single_row_of(number,string):
	for n in range(number):
		print(string, end = "")

def square_of_stars(numbers):
	for n in range(numbers):
		for m in range(numbers):
			print("*", end = "")
		print()

def rectangle_of_stars(rows, cols):
	for n in range(rows):
		for m in range(cols):
			print("*", end = "")
		print()

def list_by_2(a_list):
	new_list = []
	for n in a_list:
		new_list.append(n*2)
	return new_list

def create_grid(size):
	a_list = []
	for row in range(size):
		new_list = []
		for column in range(size):
			new_list.append("-")
		a_list.append(new_list)
	return a_list

a = ["x","y","z","r"]

l = len(a)

for i in range(len(a)):
    a[i] = "rrr"

print("hi")