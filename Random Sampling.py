def calculate_sample_size(populaiton_size, confidence_level, margin_of_error):
    if confidence_level == 90:
        z_score = 1.64
    elif confidence_level == 95:
        z_score = 1.96
    elif confidence_level == 99:
        z_score = 2.58
    else:
        print("Unsupported value, please input one of the following values, 90, 95, 99: ")
        return None
#Specify Unknown population value
    p = 0.5

#Perform the calculation
    sample_size = ((z_score * z_score * p * (1-p)) / (margin_of_error * margin_of_error))
    return int(sample_size)

def systematic_sample(population, sample_size):
    interval = len(population) / sample_size
    interval = round(interval)

    selected_elements = []

    for i in range(0, len(population), interval):
        selected_elements.append(population[i])
    return selected_elements

#getting use rinput
population_size = int(input("Enter the population size: "))
confidence_level = int(input("Enter the confidence level, ex. 90, 95, or 99: "))
margin_of_error = float(input("Enter the desired margin of error, ex. 0.1, 0.05, 0.01: "))

sample_size = (calculate_sample_size(population_size, confidence_level, margin_of_error))
print(f"The calculated sample size was aproximately {sample_size}. ")

user_sample_size = int(input("Enter your desired sample size: "))

maximum_sample_size = calculate_sample_size(population_size, 99, 0.01)
if user_sample_size > maximum_sample_size:
    print("Sorry, the requested sample size is most likely mot feisable, please enter a feasable value")
else:
    systematic_sample = systematic_sample(list(range(1, population_size + 1)), sample_size)
    print("The following elements were selected by systematic random sampling: ")
    print(systematic_sample)