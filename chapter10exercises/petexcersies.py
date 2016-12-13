import Pet

def main():
    #Get pet data
    name = input('What is the name of your pet? ')
    animal_type = input('What is the type of your pet? ')
    age = input(int('How old is your pet? '))
entry = Pet(name,animal_type,age)

#display data entered
print('Here is your pet information:')
print('Name:', name)
print('Type:', animal_type)
print('Age:', age)
