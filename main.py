def get_special_data():
    # Define your special data here
    special_data = "This is the special data you've unlocked!"
    return special_data

def main():
    # Define your 4-digit combination here
    correct_combination = "4234"  # Change this to your desired combination

    # Prompt the user to enter the combination
    combination_attempt = input("Enter the 4-digit combination to access special data: ")

    # Check if the entered combination is correct
    if combination_attempt == correct_combination:
        # If the combination is correct, provide access to special data
        special_data = get_special_data()
        print("Access granted! now you need to look at the text document named udhhwu32738dhdu3. You need to decypher the code using the engima machine.:")
        print(special_data)
    else:
        # If the combination is incorrect, deny access
        print("Incorrect combination. Access denied.")

if __name__ == "__main__":
    main()
