print("**Welcome to Temperature Teller**")

def temp_teller(temp):
    if temp > 28:
        return "Hot"
    elif 18 <= temp <= 28:
        return "Warm"
    else:
        return "Cold"

def check_error (user_input):
    while True:
        try:
            val = float(user_input)
            return val
        except ValueError:
            print("Error, Please enter a numeric value.")
            user_input = input("Enter temperature again: ")

temp = input("Enter temperature in Celcius: ")
error_temp = check_error(temp)
# print(f"Error: {error_temp}")
# print(temp_teller(temp))

print("Validated temperature:", error_temp)
print("Temperature feel:", temp_teller(temp))



