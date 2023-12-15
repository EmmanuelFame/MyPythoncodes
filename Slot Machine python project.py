import random

MAX_LINES = 3
MAX_BET= 100
MIN_BET= 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}
def deposit():
    while True:
        ammount = input('How much will you like to deposit? $')
        if ammount.isdigit():
            ammount=int(ammount)
            if ammount>0:
                break
            else:
                print('ammount must be greater than 0.')
        else:
            print('Please enter a number.')

    return ammount

def get_number_of_lines():
    while True:
        lines = input('Enter the number of lines you will like to bet on(1-' +str(MAX_LINES)+')? ' )
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('enter a valid number of lines')
        else:
            print('Please enter a number.')

    return lines
def get_bet():
    while True:
        ammount = input('What would you like to bet on each line? $')
        if ammount.isdigit():
            ammount=int(ammount)
            if MIN_BET <= ammount <= MAX_BET:
                break
            else:
                print(f'ammount must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Please enter a number.')

    return ammount

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbols, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)
    columns= [[], [], []]
    for _ in range(cols):
        column= []
        current_symbols= all_symbols[:]
        for _ in range(rows):
            value=random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns)-1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        print()


def main():
    balance=deposit()
    lines=get_number_of_lines()
    while True:
        bet= get_bet()
        total_bet= bet * lines
        if total_bet > balance:
            print(f'you do not have sufficient balance to bet, your current balance is ${balance}')

        else:
            break
    print(f'you are betting ${bet} on {lines} lines). Total bet is = ${total_bet}') 
    slots= get_slot_machine_spin(ROWS, COLS, symbol_count)
main()

    
