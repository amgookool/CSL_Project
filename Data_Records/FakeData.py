from faker import Faker

faker = Faker()
old_person_conditions = ['Arthritis', 'Hypertension', 'Asthma', 'Blindness', 'Cancer', 'Chronic Bronchitis',
                         'Heart Disease', 'Dementia', 'Diabetes', 'Epilepsy', "Parkinson's Disease", 'Stroke', 'Shingles', 'High Cholesterol']
medical_history = [faker.word(old_person_conditions) for i in range(10)]

driver_permit = [faker.unique.numerify(text='#######')for i in range(10)]

passport_number = [faker.unique.bothify(text='??######') for i in range(10)]

national_id = [faker.unique.numerify(text='###########')for i in range(10)]

dosage = [faker.random_elements(
    elements=('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'),unique = True )for i in range(10)]

frequency = [faker.random_digit_not_null() for i in range(10)] 

first_names = [faker.unique.first_name() for i in range (10)]

last_names = [faker.unique.last_name() for i in range(10)]

temp= [faker.date_of_birth() for i in range(10)]
date_of_birth  =[]
for i in temp:
 date_of_birth .append('{}'.format(i))
  
gender = faker.random_choices(elements=('Male','Female'),length = 10)

marital_status = faker.random_choices(elements=('Single','Married','Widowed','Divorce'),length=10)

next_of_kin = [faker.unique.first_name() for i in range(10)]
