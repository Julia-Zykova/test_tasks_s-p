class Dessert:

	def __init__(self, name = None, calories = None):
		self._name = name
		self._calories = calories

		if self._check_name(name) and self._check_calories(calories):
			self._name = name
			self._calories = calories


	@classmethod
	def _check_name(cls,name):
		return type(name) == str

	@classmethod
	def _check_calories(cls, calories):
		return type(calories) in (int, float)


	def set_name(self, name):
		if self._check_name(name):
			self._name = name

	def set_calories(self, calories):
		if self._check_calories(calories):
			self._calories = calories


	def get_name(self):
		return self._name

	def get_calories(self):
		return self._calories


	def is_healfy(self):
		if ((isinstance(self._calories, int)) == True):
			return (self._calories <= 200)
		else:
			return (isinstance(self._calories,int))


	def is_delicious(self):
		return True

