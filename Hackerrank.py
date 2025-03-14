# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def calculate_fine(returned_date, due_date):
    ret_day, ret_month, ret_year = map(int, returned_date)
    due_day, due_month, due_year = map(int, due_date)
    
    if (ret_year, ret_month, ret_day) <= (due_year, due_month, due_day):
        return 0
    elif ret_year > due_year:
        return 10000
    elif ret_month > due_month and ret_year == due_year:
        return 500 * (ret_month - due_month)
    else:
        return 15 * (ret_day - due_day)

if __name__ == "__main__":
    lines = sys.stdin.read().strip().split("\n")
    
    returned_date = lines[0].split()
    due_date = lines[1].split()
    
    fine = calculate_fine(returned_date, due_date)
    print(fine)
