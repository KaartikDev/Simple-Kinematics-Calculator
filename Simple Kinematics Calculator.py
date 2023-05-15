# All code created by me

# List of dictionary keys, lets each key has a index
variables = ("displacement", "velocity final", "velocity initial", "time", "acceleration")
# Dict of known variables. variables that is unneeded/unknown will have an assigned value "n_a"
known_variables = {"displacement": "n_a", "velocity final": "n_a", "velocity initial": "n_a", "time": "n_a",
                   "acceleration": "n_a"}
# Dict of assigned equations(values) for each variable(key)
equation_variables = {"displacement": "d = vi*t + 1/2(a)(t^2)", "velocity final": "vf = (2d/t) - vi",
                      "velocity initial": "vi=vf-at", "time": "t = (vf-vi)/a", "acceleration": "a=(vf-vi)/t"}
# Variable that contains the index of the variable they are solving for./. the index correlates to a key
variable_index_picked = "NA"
# List of indexes that correspond to uneeded variables. The index correspond to keys, if variable is in this list, their value will not be taken
unneeded_var_indexes = []
# Repeats code  while variable is equal to true. Stops once is assigned false
repeat = True


def variable_picker():
    """
    Lets user choose a valid index that corresponds to a variable. That variable acts as key in the 'equation variables' dictionary
     and appends the key to unneeded_var_indexes
    """
    for i in range(len(variables)):
        print(str(i) + ") " + str(variables[i]))
    while True:
        try:
            variable_picked = int(input("What variable would you like to solve for?(Please enter a number) "))

            if variable_picked < 5 and variable_picked > -1:
                print("You are solving for " + variables[variable_picked])
                unneeded_var_indexes.append(variable_picked)
                return variable_picked
                break
            else:
                print("please pick a valid interger less then 5 and greater then -1")
                continue
        except ValueError:
            print("please pick a interger")


# Plugs in assigned values from dictionary. Prints result.
def solve_displacement(inputs):
    d = inputs["velocity initial"] * inputs["time"] + (1 / 2) * inputs["acceleration"] * (
        inputs["time"]) ** 2
    print()
    print("Your displacement is " + str(d) + " meters")


# Plugs in assigned values from dictionary. Prints result.
def solve_velf(inputs):
    vf = ((inputs["displacement"] * 2) / inputs["time"]) - inputs["velocity initial"]
    print()
    print("Your velocity final is " + str(vf) + " m/s")


# Plugs in assigned values from dictionary. Prints result.
def solve_veli(inputs):
    vi = inputs["velocity final"] - inputs["acceleration"] * inputs["time"]
    print()
    print("Your velocity initial is " + str(vi) + " m/s")


# Plugs in assigned values from dictionary. Prints result.
def solve_time(inputs):
    t = (inputs["velocity final"] - inputs["velocity initial"]) / inputs["acceleration"]
    print()
    print("Your time is " + str(t) + " seconds")


def solve_acc(inputs):
    a = (inputs["velocity final"] - inputs["velocity initial"]) / inputs["time"]
    print()
    print("Your acceleration is " + str(a) + " m/s^2")





def filling_in_knowns_picking_eqations(variable_index_picked):
    """
    The function first has if/elif that say what formula you are using based on what index user picked
    Then have them fill in needed known variables. We know the variables that are needed because they are used in the equation
    Finally, it runs the respective solve function to print result of inputs
    """
    # solving displacemnt
    if variable_index_picked == 0:
        print("So you will be using the " + equation_variables[variables[variable_index_picked]] + " equation")
        print("This means you will need to input the following variables: velocity initial, time, acceleration")
        unneeded_var_indexes.append(1)
        for index in range(len(known_variables)):
            if index not in unneeded_var_indexes:
                while True:
                    try:
                        known_variables[variables[index]] = int(input("What is the given value for " + variables[
                            index] + " in base SI units.(meters,m/s,s,m/s^2) "))
                        break
                    except:
                        print("please enter a valid number")
        solve_displacement(known_variables)
    # solving velf
    elif variable_index_picked == 1:
        print("So you will be using the " + equation_variables[variables[variable_index_picked]] + " equation")
        print("This means you will need to input the following variables: velocity initial, time, displacement")
        unneeded_var_indexes.append(4)
        for index in range(len(known_variables)):
            if index not in unneeded_var_indexes:
                while True:
                    try:
                        known_variables[variables[index]] = int(input("What is the given value for " + variables[
                            index] + " in base SI units.(meters,m/s,s,m/s^2) "))
                        break
                    except:
                        print("please enter a valid number")
        solve_velf(known_variables)
    # solve veli
    elif variable_index_picked == 2:
        print("So you will be using the " + equation_variables[variables[variable_index_picked]] + " equation")
        print("This means you will need to input the following variables: velocity final, time, acceleration")
        unneeded_var_indexes.append(0)
        for index in range(len(known_variables)):
            if index not in unneeded_var_indexes:
                while True:
                    try:
                        known_variables[variables[index]] = int(input("What is the given value for " + variables[
                            index] + " in base SI units.(meters,m/s,s,m/s^2) "))
                        break
                    except:
                        print("please enter a valid number")
        solve_veli(known_variables)
    # solve time
    elif variable_index_picked == 3:
        print("So you will be using the " + equation_variables[variables[variable_index_picked]] + " equation")
        print(
            "This means you will need to input the following variables: velocity final, velocity initial, acceleration")
        unneeded_var_indexes.append(0)
        for index in range(len(known_variables)):
            if index not in unneeded_var_indexes:
                while True:
                    try:
                        known_variables[variables[index]] = int(input("What is the given value for " + variables[
                            index] + " in base SI units.(meters,m/s,s,m/s^2) "))
                        break
                    except:
                        print("please enter a valid number")
        solve_time(known_variables)
    # solve acc
    else:
        print("So you will be using the " + equation_variables[variables[variable_index_picked]] + " equation")
        print("This means you will need to input the following variables: velocity final, velocity initial, time")
        unneeded_var_indexes.append(0)
        for index in range(len(known_variables)):
            if index not in unneeded_var_indexes:
                while True:
                    try:
                        known_variables[variables[index]] = int(input("What is the given value for " + variables[
                            index] + " in base SI units.(meters,m/s,s,m/s^2) "))
                        break
                    except:
                        print("please enter a valid number")
        solve_acc(known_variables)


# Repeats code until user decides to exit
while repeat:
    variable_index_picked = variable_picker()
    filling_in_knowns_picking_eqations(variable_index_picked)
    print()
    print("Thanks for using our kinematics calculator")
    unneeded_var_indexes = []
    new_calc = input("would you like to run again? (y/n) ")
    if new_calc == "n":
        repeat = False

    print("Ok")
    print()
