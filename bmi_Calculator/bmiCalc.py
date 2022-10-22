# BMI calculator v.0.0.1
def main():
    # Offers choice between metric and imperial system
    name = input('Enter name\n')
    print('Hello, ' + name)
    choice = input('Would you like to perform metric of imperial system calculations?\n')
    # Metric system for normal people
    if choice == 'metric':
        weight = float(input('Please enter your weight\n'))
        # Converting between metric and imperial systems
        unit = input('(K)g or (L)bs:\n')
        if unit.upper() == 'L':
            convertedWeight = round(weight / 2.2, 1)
            print('Weight in Kg: ' + str(convertedWeight))
        else:
            convertedWeight = round(weight * 2.2, 1)
            print('Weight in Lbs: ' + str(convertedWeight))

        height = float(input('Please enter your height\n'))
        # Converting between metric and imperial systems
        unitH = input('(M)eters or (F)eet:\n')
        if unitH.upper() == 'M':
            convertedHeight = round(height * 3.281, 1)
            print('Height in feet is: ' + str(convertedHeight))
        else:
            convertedHeight = round(height / 3.281, 1)
            print('Height in meters is: ' + str(convertedHeight))
        # BMI calculation
        bmi = round(weight / (height * height), 1)
        message = 'Your Body Mass Index is,'
        print(message, bmi)
        if bmi < 18.5:
            print('You are underweight')
        elif 18.5 >= bmi or bmi <= 24.9:
            print('Your body weight is ideal')
        elif 25 >= bmi or bmi <= 29:
            print('You are overweight for you height')
        elif bmi >= 30:
            print('You are obese and at a high risk of weight related disease')
    else:
        # Imperial for American weirdos
        weight = float(input('Please enter your weight\n'))
        height = float(input('Please enter your height\n'))
        bmi = round((weight * 703) / ((height * 12) ** 2), 1)
        message = 'Your Body Mass Index is,'
        print(message, bmi)
        if bmi < 18.5:
            print('You are underweight')
        elif 18.5 >= bmi or bmi <= 24.9:
            print('Your body weight is ideal')
        elif 25 >= bmi or bmi <= 29:
            print('You are overweight for you height')
        elif bmi >= 30:
            print('You are obese and at a high risk of weight related disease')

    restart = input('Would you like to start again? yes or no? ').lower()
    if restart == 'yes':
        main()
    else:
        exit()


main()
