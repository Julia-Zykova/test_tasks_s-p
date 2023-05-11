class Desert:

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
			print(self._calories <= 200)
		else:
			print(isinstance(self._calories,int))


	def is_delicios(self):
		return True

class JellyBean(Desert):
	def __init__(self, name = None, calories = None, flavor = None):
		super().__init__(name = None, calories = None)
		self._flavor = flavor

	def set_flavor(self):
		if type(self._flavor(flavor)) == str:
			self._flavor = flavor

	def get_flavor(self):
		return self._flavor

	def is_delicios(self):
		if self._flavor != 'black licorice':
			return True
		else:
			return False

			
		
j = JellyBean("BertyBobs", 175, 'black licorice')
print(j.is_delicios())