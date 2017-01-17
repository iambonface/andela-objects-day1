
class Person():
	def __init__(self, firstname, lastname, height, weight, age):
		self.firstname = firstname
		self.lastname = lastname
		self.height = height
		self.weight = weight
		self.age = age

	def __str__(self):
		return "Names: %s %s" % (self.firstname, self.lastname )

	def get_weight(self):
		"""in Kgs"""
		return self.weight

	def get_height(self):
		"""in meters"""
		return self.height
	def get_bmi(self):
		"""height m and weight kg"""
		bmi = self.weight/(self.weight **2)
		if bmi <= 18.5:
			return Person.__str__(self) + " ," +  " BMI: %2.2f," % (bmi) + " You are Underweight"
		elif 18.5 <= bmi <=24.9:
			return Person.__str__(self) + " ," + " BMI:  %2.2f," % (bmi)  + " You are Normal"
		elif 25 <= bmi <=29.9:
			return Person.__str__(self) + " ," + " BMI: %2.2f," % (bmi) + " You are overweight"

		elif bmi >= 30:
			return Person.__str__(self) + " ," + " BMI: %2.2f," % (bmi) + " You are Obese"


class Doctor(Person):
	def __init__(self, firstname, lastname, height, weight, age, speciality, staff_id):
		Person.__init__(self, firstname, lastname, height, weight, age)
		self.speciality = speciality
		self.staff_id = staff_id
	def __str__(self):
		return Person.__str__(self) + " :" + "Speciality: %s + ID: %s" % (speciality, staff_id)


class Patient(Doctor):
	def __init__(self, patient_no):
		Person.__init__(self, firstname, lastname, height, weight, age, disease)
		self.patient_no = patient_no
		self.disease = disease
	def __str__(self):
		return Person.__str__(self) + " :" + "Patient No: %s disease: %s " (patient_no, disease)


