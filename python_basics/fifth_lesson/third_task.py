print("employee with salary < 20000:",)
total_salary = 0
workers = 0
with open("workers.txt") as f:
    for line in f.readlines():
        tmp_line = line.split()
        workers += 1
        total_salary += float(tmp_line[1])
        if float(tmp_line[1]) < 20000:
            print(f"{tmp_line[0]}")
print(f"average salary is: {total_salary / workers:.2f}")
