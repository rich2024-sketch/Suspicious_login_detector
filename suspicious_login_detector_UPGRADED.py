# admin_failed = 0
# guest_failed = 0

failed_login_dict = {}
with open('login_data.log', 'r', encoding = "utf-8") as file:
    for line in file:
        login_ip = line.strip().split()
        if login_ip[2] == "FAILED":
            failed_login_dict[login_ip[4]] = failed_login_dict.get(login_ip[4], 0) + 1

print("Failed Login Report")
print("-----------------------")
for failed_login, count in failed_login_dict.items():
    print(f"{failed_login}: {count} failures")
print("\n")
for failed_login, count in failed_login_dict.items():
    if count >= 3:
        print(f"ALERT: {failed_login} exceeded failed login threshold")

