
def operations(start_sum,operation,count_operations,ammount):
    while operation != "q":
        operation = input("Введите тип операции: ")
        if operation == "q":
                return start_sum
        amount = int(input("Введите сумму: "))    
        if amount % 50 != 0:
            print("Ошибка!Внесенная сумма не кратна 50!")
        if operation == "+":
            count_operations += 1
            wealth_tax(start_sum)
            start_sum += amount 
            percent_operation(start_sum,count_operations)             
        elif operation == "-":
            if start_sum < amount:
                print("Ошибка! На счету недостаточно средств!") 
                return start_sum
            count_operations += 1
            wealth_tax(start_sum)
            if amount > 30 and amount < 600:
                amount = amount - (amount * 1.5 / 100)
            start_sum -= amount
            percent_operation(start_sum,count_operations)

def entry(start_sum):
    operation = ""
    amount = 0
    count_operations = 0
    start_sum = operations(start_sum,operation,count_operations,amount)
    return start_sum
            

def percent_operation(start_sum,count_operations):
    if count_operations % 3 == 0:
                start_sum = start_sum * (3 + start_sum) / start_sum
                return start_sum

def wealth_tax(start_sum):    
    if start_sum >= 5000000:
        start_sum = start_sum - (start_sum * 10 / 100)
        return start_sum

       
    
    

start_sum = 0
result = entry(start_sum)
print(f"Остаток средств на счете: {result}")



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Попробуй разбить operations на подфункции