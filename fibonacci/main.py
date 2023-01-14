
def fibo(final_index):
    current_number, next_number = 0, 1

    for _ in range(final_index):
        yield current_number
        temp = current_number
        current_number = next_number
        next_number = current_number + temp


for number in fibo(1000):
    print(number)
