from __future__ import division
from collections import defaultdict
import math
import sys

def classes(A):
	""" Return the count of each item in a list A."""
	return {key : A.count(key) for key in A}

def list_range(key,length):
	""" Return a list of a single value of some length."""
	return [key for j in range(0,length)]

def attr_set(*args):
	""" Return a list of lists returned from list_range."""
	import itertools
	lists = list()
	if type(args[0]) is list:
		lists = [list_range(key,length) for key, length in enumerate(args[0])]
	else:
		lists = [list_range(key,length) for key, length in enumerate(args)]
	return list(itertools.chain(*lists))

def entropy(A,weight=None):
	"""	Return the entropy (information theory) of a list A. Possibly Weighted."""
	entropy = 0
	for count in classes(A).values():
		p = count / len(A)
		entropy += p * math.log(p,2)
	if weight is None:
		return entropy * (-1)
	else:
		return weight * entropy * (-1)

def information_gain(n_instances,attrs_list,H):
	""" Return the Information Gain of a list of attributes."""
	s = 0
	for attrs in attrs_list:
		nums = attr_set(attrs)
		s += entropy(nums, len(nums) / n_instances)
	return H - s










