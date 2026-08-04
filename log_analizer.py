num_errors = 0
num_warnings = 0
num_lines = 0
with open('server.log', 'r', encoding = "utf-8") as file:
    for line in file:
        num_lines += 1
        if "ERROR" in line:
            num_errors += 1
        elif "WARNING" in line:
            num_warnings += 1
print("---------- log summary ----------")
print(f"Total lines: {num_lines}")
print(f"ERROR: {num_errors}")
print(f"WARNING: {num_warnings}")