"""
	This is a real world hospital problem modelled using Object Oriented Programming
	The module takes advantage of inheritance, encapsulation, polymophism
	This program can also calculate BMI (Body Mass Index)

	Args:
		Provide firstname, lastname, height, weight and age for parent (super class)
		Other subclass contain specific properties like Speciality and staff_iD FOR Doctor
		and The Patient subclass containes disease as subclass

	Results:
	    The program can generate name, BMI and status of body weight if the get_bmi function is called.


"""
class Person():
	"""Super class from which all other classes inherit methods"""
	def __init__(self, firstname, lastname, height, weight, age):
		self.firstname  = firstname,
		self.lastname = lastname
		self.height = height
		self.weight = weight
		self.age = age

	def __str__(self):
		return "Names: %s %s" % (self.firstname, self.lastname )

	def get_weight(self):
		"""Weight is in Kgs"""
		return self.weight

	def get_height(self):
		"""Height is in meters"""
		return self.height

	def get_bmi(self):
		"""calculate BMI and compare with accepted standard values"""
		bmi = self.weight/(self.weight **2)

		if bmi <= 18.5:
			return Person.__str__(self) + " ," + "BMI: %2.2f," % (bmi) + " You are Underweight"

		elif 18.5 <= bmi <=24.9:
			return Person.__str__(self) + " ," + "BMI:  %2.2f," % (bmi)  + " You are Normal"

		elif 25 <= bmi <=29.9:
			return Person.__str__(self) + " ," + "BMI: %2.2f," % (bmi) + " You are overweight"

		elif bmi >= 30:
			return Person.__str__(self) + " ," + "BMI: %2.2f," % (bmi) + " You are Obese"


class Doctor(Person):
	"""Doctor class inherits from Person. Additional properties include speciality and staff_id"""
	def __init__(self, firstname, lastname, height, weight, age, speciality, staff_id):
		Person.__init__(self, firstname, lastname, height, weight, age)
		self.speciality = speciality
		self.staff_id = staff_id

	def __str__(self):
		return Person.__str__(self) + " :" + "Speciality: %s + ID: %s" % (speciality, staff_id)


class Patient(Doctor):
	"""Patient class inherits from Doctor. Additional property is disease"""
	def __init__(self, patient_no):
		Person.__init__(self, firstname, lastname, height, weight, age, disease)
		self.patient_no = patient_no
		self.disease = disease

	def __str__(self):
		return Person.__str__(self) + " :" + "Patient No: %s disease: %s " (patient_no, disease)


