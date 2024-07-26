# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю +++++++++++++++++++
# ✔ Допустимые действия: пополнить, снять, выйти ++++++++++++++++
# ✔ Сумма пополнения и снятия кратны 50 у.е. +++++++++++++++++
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. ++++++++++++++++++++
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3% +++++++++++++++++++++++
# ✔ Нельзя снять больше, чем на счёте++++++++++++++++++++
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой +++++++++++++++
# операцией, даже ошибочной +++++++++++++++



def entry(start_sum):
    operation = ""
    amount = 0
    count_replainishment = 0
    while operation != "q":
        operation = input("Введите тип операции: ")
        if operation == "q":
                return start_sum
        amount = int(input("Введите сумму: "))    
        if amount % 50 != 0:
            print("Ошибка!Внесенная сумма не кратна 50!")
        if operation == "+":
            count_replainishment += 1
            wealth_tax(start_sum)
            start_sum += amount 
            percent_rep(start_sum,count_replainishment)             
        elif operation == "-":
            if start_sum < amount:
                print("Ошибка! На счету недостаточно средств!") 
                return start_sum
            count_replainishment += 1
            wealth_tax(start_sum)
            if amount > 30 and amount < 600:
                amount = amount - (amount * 1.5 / 100)
            start_sum -= amount
            percent_rep(start_sum,count_replainishment) 
            

def percent_rep(start_sum,count_replainishment):
    if count_replainishment % 3 == 0:
                start_sum = start_sum + (start_sum * 3 / 100)
                return start_sum

def wealth_tax(start_sum):    
    if start_sum >= 5000000:
        start_sum = start_sum - (start_sum * 10 / 100)
        return start_sum

       
    
    

start_sum = 0
result = entry(start_sum)
print(result)