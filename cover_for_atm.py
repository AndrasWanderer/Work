import tkinter as tk
import traceback

############################ Блок логики ATM #################################

start_sum = 0
count_replainishment = 0
amount = 0

def balance(operation):
    atm_balance.delete(0, tk.END)
    atm_balance.insert(0, f"Ваш баланс: {start_sum}")


def wealth_tax(start_sum):
    if int(start_sum) >= 5000000:
        start_sum = start_sum - (start_sum * 10 / 100)
        return start_sum
    else:
        return start_sum

def withdrawal_percent(start_sum,amount):
    if amount > 30 and amount < 600:
                amount = amount - (amount * 1.5 / 100)
                start_sum -= amount
                return start_sum
    else:
        return start_sum

def percent_rep(start_sum,count_replainishment):
     if count_replainishment % 3 == 0:
        start_sum = start_sum + (start_sum * 3 / 100)
        return start_sum
     else:
         return start_sum

def check_sum(operation):
    global start_sum
    global count_replainishment
    value = atm_entry.get()
    a = test(int(value))
    if a != None:
        atm_entry.delete(0, tk.END)
        atm_entry.insert(0, a)
    try:
        start_sum += int(value)
        start_sum = int(wealth_tax(start_sum))
        # if wealth_tax == True:
        #         atm_info.insert(0, "Вычтен процент налога на богатство")
        count_replainishment += 1
        start_sum = percent_rep(start_sum,count_replainishment)
        # if percent_rep == True:
        #         atm_info.insert(0, "Начислен процент за третье пополнение")
        print(start_sum)
    except:
        traceback.print_exc()
        atm_entry.delete(0, tk.END)
        atm_info.insert(0, "Некорректный ввод")


def del_sum(operation):
    global start_sum
    global count_replainishment
    global amount
    value = atm_entry.get()
    a = test(int(value))
    if a != None:
        atm_entry.delete(0, tk.END)
        atm_entry.insert(0, a)
        
    elif start_sum < int(atm_entry.get()):
        atm_balance.delete(0, tk.END)
        atm_info.insert(0, f"Ошибка! Недостаточно средств!")

    else:
        try:
            start_sum -= int(value)
            start_sum = withdrawal_percent(start_sum,amount)
            # if withdrawal_percent == True:
            #     atm_info.insert(0, "Вычтен процент за снятие")
            start_sum = wealth_tax(start_sum)
            # if wealth_tax == True:
            #     atm_info.insert(0, "Вычтен процент налога на богатство")
            count_replainishment += 1
            start_sum = percent_rep(start_sum,count_replainishment)
            # if percent_rep == True:
            #     atm_info.insert(0, "Начислен процент за третье пополнение")
            print(start_sum)
        except:
            traceback.print_exc()
            atm_entry.delete(0, tk.END)
            atm_info.insert(0, "Некорректный ввод")
    


def test(amount):
    if amount % 50 != 0:
        return "Некорректная сумма"


##################### Блок интерфейса ########################


win = tk.Tk()
win.config(bg="midnightblue")
win.title("A T M")
win.geometry("410x460+100+200")


def add_digit(digit):
    value = atm_entry.get() + str(digit)
    atm_entry.delete(0, tk.END)
    atm_entry.insert(0, value)


def add_operation(operation):
    value = atm_entry.get()
    if value[-1] in "-+qEnterDel":
        value = value[:-1]
    atm_entry.delete(0, tk.END)
    atm_entry.insert(0, value + operation)


def make_button(digit):
    return tk.Button(text=digit, font=("Arial", 13), bg="slateblue4", bd=3, command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, font=("Arial", 13, "bold"), bg="slateblue", bd=3,
                     command=lambda: add_operation(operation))


def make_enter_button(operation):
    return tk.Button(text=operation, font=("Arial", 13), bg="royalblue4", bd=3, command=lambda: check_sum(operation))


def make_delete_button(operation):
    return tk.Button(text=operation, font=("Arial", 13), bg="royalblue4", bd=3, command=lambda: del_sum(operation))


def make_quit_button(operation):
    return tk.Button(text=operation, font=("Arial", 13, "bold"), bg="purple4", bd=3, command=lambda: balance(operation))


lbl_main = tk.Label(win, text="Welcome Stranger!",
                    font=("FranklinGothicBook", 20),
                    bg="black",
                    fg="green",
                    relief=tk.RAISED,
                    bd=2)

lbl_entry = tk.Label(win, text="Ввод",
                     font=("FranklinGothicBook", 20),
                     bg="black",
                     fg="green",
                     relief=tk.RAISED,
                     bd=2)

lbl_balance = tk.Label(win, text="Баланс",
                       font=("FranklinGothicBook", 20),
                       bg="black",
                       fg="green",
                       relief=tk.RAISED,
                       bd=2)

lbl_info = tk.Label(win, text="Информация",
                    font=("FranklinGothicBook", 20),
                    bg="black",
                    fg="green",
                    relief=tk.RAISED,
                    bd=2)
lbl_main.grid(column=0, row=0, columnspan=7)
lbl_entry.grid(row=1, column=4, columnspan=4)
lbl_balance.grid(row=2, column=4, columnspan=4)
lbl_info.grid(row=3, column=4, columnspan=4)

atm_entry = tk.Entry(win,
                     font=("Arial", 15),
                     bg="mediumslateblue",
                     fg="indigo",
                     justify=tk.RIGHT)

atm_balance = tk.Entry(win,
                       font=("Arial", 15),
                       bg="mediumslateblue",
                       fg="indigo",
                       justify=tk.RIGHT)

atm_info = tk.Entry(win,
                    font=("Arial", 15),
                    bg="mediumslateblue",
                    fg="indigo",
                    justify=tk.RIGHT)

atm_entry.grid(row=1, column=0, columnspan=4)
atm_balance.grid(row=2, column=0, columnspan=4)
atm_info.grid(row=3, column=0, columnspan=4)

make_button("1").grid(row=4, column=0, stick="wens", padx=3, pady=3)
make_button("2").grid(row=4, column=1, stick="wens", padx=3, pady=3)
make_button("3").grid(row=4, column=2, stick="wens", padx=3, pady=3)
make_button("4").grid(row=5, column=0, stick="wens", padx=3, pady=3)
make_button("5").grid(row=5, column=1, stick="wens", padx=3, pady=3)
make_button("6").grid(row=5, column=2, stick="wens", padx=3, pady=3)
make_button("7").grid(row=6, column=0, stick="wens", padx=3, pady=3)
make_button("8").grid(row=6, column=1, stick="wens", padx=3, pady=3)
make_button("9").grid(row=6, column=2, stick="wens", padx=3, pady=3)
make_button("0").grid(row=4, column=3, stick="wens", padx=3, pady=3, rowspan=3)

make_quit_button("balance").grid(row=7, column=0, stick="wens", padx=3, pady=3, columnspan=4)
make_enter_button("Enter").grid(row=4, column=4, columnspan=2, stick="wens", padx=3, pady=3, rowspan=2)
make_delete_button("Cash out").grid(row=6, column=4, columnspan=2, stick="wens", padx=3, pady=3, rowspan=2)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_columnconfigure(4, minsize=60)
win.grid_columnconfigure(5, minsize=60)

win.grid_rowconfigure(0, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)

win.mainloop()