def resultant_magnitude(resultant_vector_x, resultant_vector_y):
    resultant_vector_magnitude = np.sqrt((resultant_vector_x**2) + (resultant_vector_y**2))
    print(colored("\n-----------------------------------------------------------", "green"))
    print(colored("Magnitude of the Resultant Vector: " + "{:.4f}".format(resultant_vector_magnitude), "green"), end="")
    print()
