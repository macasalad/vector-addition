def resultant_direction(resultant_vector_x, resultant_vector_y):
    resultant_vector_direction = np.rad2deg(np.arctan(abs(resultant_vector_y / resultant_vector_x)))
    print(colored("Direction of the Resultant Vector: ", "green"), end="")
    if resultant_vector_x > 0 and resultant_vector_y == 0:
        print(colored("0° East", "green"))
    elif resultant_vector_x > 0 and resultant_vector_y > 0:
        print(colored(str("{:.4f}".format(resultant_vector_direction)) + "° North of East", "green"))
    elif resultant_vector_x == 0 and resultant_vector_y > 0:
        print(colored("90° East", "green"))
    elif resultant_vector_x < 0 and resultant_vector_y > 0:
        print(colored(str("{:.4f}".format(resultant_vector_direction)) + "° North of West", "green"))
    elif resultant_vector_x < 0 and resultant_vector_y == 0:
        print(colored("180° East", "green"))
    elif resultant_vector_x < 0 and resultant_vector_y < 0:
        print(colored(str("{:.4f}".format(resultant_vector_direction)) + "° South of West", "green"))
    elif resultant_vector_x == 0 and resultant_vector_y < 0:
        print(colored("270° East", "green"))
    else:
        print(colored(str("{:.4f}".format(resultant_vector_direction)) + "° South of East", "green"))
    print(colored("\nThank you for using our program!\n-----------------------------------------------------------", "green"))
