"""" Калькулятор """

import tkinter as tk

"""функция вывода на экран цифр"""
def add_digit(digit):
    value = calc.get()                                          # считываем данные с экрана калькулятора.
    if value[0] == '0' and len(value) == 1 and digit != '.':    # для удаления нуля перед вводом цифр.
        value = value[1:]                                       # делаем срез строки с 1-го символа.
    calc.delete(0, tk.END)                                      # очищаем экран.
    calc.insert(0, value + digit)                               # выводим уже новое значение.

"""функция вывода на экран арифметического знака"""
def add_operation(operation):
    value = calc.get()                          # считываем данные с экрана калькулятора.
    if value[-1] in '+-*/':                     # для замены знака на знак при повторном выборе действия.
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()                             # если ар.действие уже есть в выражении, то при нажатии сл.действия,
                                                # первое выполняется автоматически.
        value = calc.get()                      # считываем данные с экрана калькулятора.
    calc.delete(0, tk.END)                      # очищаем экран.
    calc.insert(0, value + operation)           # выводим уже новое значение.

"""функция вычисления процентов"""
def percent():
    value = calc.get()                          # выводим уже новое значение.
    try:
        value_1 = ''
        value_2 = ''
        operation = ''
        i = 0                               # считываем посимвольно данные с экрана и формируем первое число,
                                            # пока не дойдём до арифметического знака, записываем знак, а то,
                                            #что осталось, это второе число.
        while operation != '*' and operation != '/' and operation != '+' and operation != '-':
            value_1 += value[i]
            operation = value[i + 1]
            i += 1
        value_1 = float(value_1)

        value_2 = float(value[i + 1:])
                                            # взависимости от знака выполняем вычисление
        percent_dict = {'*': value_1 * value_2 / 100, '+': value_1 + value_1 * value_2 / 100, \
                        '-': value_1 - value_1 * value_2 / 100, '/': value_1 / value_2 * 100}
        result = percent_dict.get(operation, 'error')
        calc.delete(0, tk.END)
        calc.insert(0, result)
    except:                                 # при не корректнов вводе операции выходит сообщение об ошибке
        calc.delete(0, tk.END)
        calc.insert(0, 'error')

"""функция вычисления"""
def calculate():
    value = calc.get()
    if value[-1] in '/*-+':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))         # выполняем вычисление
    except ZeroDivisionError:
        calc.delete(0, tk.END)
        calc.insert(0, 'error')             # приделении на ноль выводим сообщение об ошибке

"""функция очистки и обнуления экрана"""
def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')

"""функция удаления цифры(знака) справа"""
def backspace():
    value = calc.get()
    if len(value) > 0 and value != '0':      # если на экране есть цифры и это не единственный ноль,
                                             # то срабатывает функция удаления
        calc.delete(0, tk.END)
        calc.insert(0, value[:-1])           # вырезаем строку до последнего символа и выводим на экран новое значение
    else:
        calc.delete(0, tk.END)
        calc.insert(0, '0')

"""функция работы цифровых кнопок"""
def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))

"""функция работы знаковых кнопок"""
def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation))

"""функция работы кнопки равно"""
def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=calculate)

"""функция работы кнопки сброс"""
def make_clear_button():                                 # fg - цвет надписи,bg - цвет кнопки
    return tk.Button(text='C', bd=5, font=('Arial', 13), fg='white',bg='red', command=clear)

"""функция работы кнопки забой"""
def make_backspace_button():
    return tk.Button(text='<', bd=5, font=('Arial', 13), fg='red', command=backspace)

"""функция работы кнопки проценты"""
def make_percent_button():
    return tk.Button(text='%', bd=5, font=('Arial', 13), fg='red', command=percent)

"""функция работы кнопок клавиатуры компьютера"""
def press_key(event):
    #print(repr(event.char))        # чтобы узнать кодировку кнопки
    if event.char.isdigit():        # если нажата цыфровая клавиша
        add_digit(event.char)       # выводим её значение на экран
    elif event.char in '/*-+':      # если нажата арифметическая клавиша
        add_operation(event.char)   # выводим её значение на экран
    elif event.char == '\r':        # если нажата клавиша Enter
        calculate()                 # вычисляем Backspace
    elif event.char == '\x08':      # если нажата клавиша
        backspace()                 # удаляем по символу

"""создание окна для калькулятора"""
win = tk.Tk()                           # создаём экземпляр(объект) класса.
win.geometry("240x330+100+200")
win.title("калькулятор")
win['bg'] = "#33ffe6"                   # задание цвета через RGB, можно словом.
win.bind('<Key>', press_key)            # связывает виджит, событие, действие.

"""определение работы экрана калькулятора"""
calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15) # вывод данных на экран калькулятора.
                    # прижимаем вправо , стиль и зазмер символа .
calc.insert(0, '0') # вывод нуля на экран
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5) # параметры экрана:строка,столбец,количество столбцов,
                                                             # растяжение влево и вправо,отступ от края.

"""задаём параметры цифровых кнопок"""
make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_digit_button('.').grid(row=4, column=1, stick='wens', padx=5, pady=5)

"""задаём параметры служебных кнопок"""
make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)
make_percent_button().grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_calc_button('=').grid(row=5, column=2, columnspan=2, stick='wens', padx=5, pady=5)
make_clear_button().grid(row=5, column=0, stick='wens', padx=5, pady=5)
make_backspace_button().grid(row=5, column=1, stick='wens', padx=5, pady=5)

"""задаём минимальный размер колонок"""
win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

"""задаём минимальный размер строк"""
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)
win.mainloop()                              # для фиксации окна калькулятора на мониторе
