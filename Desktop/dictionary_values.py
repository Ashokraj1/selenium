class DicValue:
	def __init__(self,val):
		self.val = val
		check_val = self.val
		check_val = list(check_val.values())
		if len(check_val) != len(set(check_val)):
			raise ValueError("Dupllicate values found")

	def get_val(self,v):
		'''To get the key and value from dictionary base on value'''
		val = self.val
		print(v)
		keys = list(val.keys())
		values = list(val.values())
		if v in values:
			for index,act_val in enumerate(values):
				if values[index] == v:
					return {keys[index]:v}
		else:
			raise ValueError('{} value is not found in dict'.format(v))			
	def update(self,v):
		'''to update a dictionary if we give key and value and it convert to value and key'''
		dic = self.val
		key = list(v.keys())
		val = list(v.values())
		if val[0] not in dic.keys() and key[0] not in dic.values():
			dic.update({val[0]:key[0]})
			return dic
		elif key[0] in dic.values():
			raise ValueError('value {} is exist in dict'.format(key[0]))
		else:
			raise KeyError(key[0])

	def remove(self,v):
		'''this is like pop function based on value'''
		dic = self.val
		key = list(dic.keys())
		val = list(dic.values())
		if v in val:
			ind_val = val.index(v)
			del dic[key[ind_val]]
			return dic
		else:
			raise ValueError('{} value is not found in dict'.format(v))
	def sort(self):
		'''to sort a dictionary bassed on value'''
		val = self.val
		sorted_val = sorted(val.items(),key=lambda x : x[1])
		return sorted_val #result will be list containn tuples

	def max(self):
		'''to get maximum values key and pair base on value'''
		val = self.val
		max_val = max(val, key=val.get)
		return {max_val:val[max_val]}

	def min(self):
		'''to get minimum values key and pair base on value'''
		val = self.val
		max_val = min(val, key=val.get)
		return {max_val:val[max_val]}

	def keys(self):
		'''to get keys opposite of dictionary => here values are keys'''
		val = self.val
		key = val.values()
		return list(key)

	def values(self):
		'''to get values opposite of dictionary => here keys are values'''
		val = self.val
		value = val.keys()
		return list(value)

	def popitem(self):
		'''remove last key value pair in ditionary'''
		val = self.val
		pop_val = list(val.keys())[-1]
		del val[pop_val]
		return val


"Sample object"
								
v = DicValue({'a':1,'b':2,'c':3,'d':4,'e':6})
print(v.update({7:'g'}))
print(v.remove(2))
print(v.sort())
print(v.max())
print(v.min())
print(v.keys())
print(v.values())
print(v.popitem())