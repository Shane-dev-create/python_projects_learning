from xml.dom import UserDataHandler
import time
 
def user_details():
    try:#Asking for user input and shortening the first and last name to the last 3 letters
        #We accept or convert all input to lowercase
        #If first and last name is shorter than 1 or 2 letters we add "oo"
        #We also validate the user input 
        first_name = input('Insert your first name:\n').lower()
        while len(first_name) < 3:
            if first_name == 1:
                first_name = first_name + "oo"
            else:
                first_name = first_name + "o"
        if any(i.isdigit() for i in first_name):
            raise ValueError('Invalid first name')
    except ValueError as e:
        print(e)
        first_name = input('Insert your first name:\n').lower()

    try:
        last_name = input('Insert your last name:\n').lower()
        while len(last_name) < 3:
            if last_name == 1:
                last_name = last_name + "oo"
            else:
                last_name = last_name + "o"
        if any(i.isdigit() for i in last_name):
            raise ValueError("Invalid last name!")
    except ValueError as e:
        print(e)
        last_name = input('Insert your last name:\n').lower()

    try:
        cohort = int(input("Insert your cohort:\n"))
        if cohort != time.localtime().tm_year:
            print("Invalid cohort")
            cohort = int(input("Insert your cohort:\n"))
        else:
            pass
    except:
        print("Invalid cohort")

    try:
        final_campus = input("Insert the campus you will be attending in:\n").lower()
        #Validating campus name
    
        if final_campus == "cape town":
            final_campus = "Cape town"
        elif final_campus == "durban":
            final_campus = "Durban"
        elif final_campus == "johannesburg":
            final_campus = "Johannesburg"
        elif final_campus == "phokeng":
            final_campus = "Phokeng"
        else:
            print("Invalid campus")
            final_campus = input("Insert the campus you will be attending in:\n").lower()
        #Validating campus name
            campus = ["Cape Town", "Durban", "Johannesburg", "Phokeng"]
            if final_campus == "cape town":
                final_campus = campus[0]
            elif final_campus == "durban":
                final_campus = campus[1]
            elif final_campus == "johannesburg":
                final_campus = campus[2]
            elif final_campus == "phokeng":
                final_campus = campus[3]
            else:
                print("Invalid campus")
                quit()

        
    except:
        print("Campus name cannot contain any numbers!")
    # Print out the student details as listed in point number 4
    print(f"First Name: {first_name.capitalize()}\nLast Name: {last_name.capitalize()}\nCohort: {cohort}\nCampus: {final_campus.capitalize()}\nFinal Username: ")
    create_user_name(first_name, last_name, cohort, final_campus) 
    print("Thank you!")


# Creates the username
def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    var = first_name[-3:] + last_name[:3] + user_campus(final_campus) + str(cohort) 
    print(var)
    quest = input("is your username correct?").lower()
    if quest != "yes":

        print("Username format is:\n We take the last 3 letters of first name and first 3 letters of last name and combine that with your abbreviated campus name and cohort year")
        selfUsername = input("Please enter your own username:\n")
        print(f"Your username is: {selfUsername}")

    else:
        pass

#Create the campus abbreviations
def user_campus(final_campus):
    """
    Return valid campus abbreviations
    """
    campus = ["CPT", "DBN", "PHO", "JHB"]
    
    if final_campus == "Cape town":
        final_campus = campus[0]
    elif final_campus == "Durban":
        final_campus = campus[1]
    elif final_campus == "Phokeng":
        final_campus = campus[2]   
    else:
        final_campus = campus[3]  

    return final_campus
    



if __name__ == '__main__':
    user_details()
    