def count_numbers(which, numbers):
    # Your code goes here
    if which.lower() != "even" and which.lower() != "odd":
        return -1
    amount = 0
    for n in numbers:
        if which.lower() == "even" and n % 2 == 0:
                amount += 1
        if which.lower() == "odd" and n % 2 != 0:
                amount += 1   
    return amount

