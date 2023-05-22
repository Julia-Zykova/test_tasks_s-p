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


	def is_healthy(self):
		if (isinstance(self._calories, int)) == True:
			return(self._calories <= 200)
		elif (isinstance(self._calories, float)) == True:
			return(self._calories <= 200)
		else:
			return(isinstance(self._calories,int))


	def is_delicious(self):
		return True

class JellyBean(Dessert):
	def __init__(self, name = None, calories = None, flavor = None):
		super().__init__(name = None, calories = None)
		self._flavor = flavor

	def set_flavor(self):
		if type(self._flavor(flavor)) == str:
			self._flavor = flavor

	def get_flavor(self):
		return self._flavor

	def is_delicious(self):
		if self._flavor != 'black licorice':
			return True
		else:
			return False
