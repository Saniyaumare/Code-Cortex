import requests

API = "http://localhost:5000/api"

# Gate Pass
def apply_gate_pass():
    name = input("Enter Name: ")
    reason = input("Enter Reason: ")

    data = {
        "name": name,
        "reason": reason
    }

    response = requests.post(f"{API}/gatepass", json=data)
    
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print("Error:", response.text)


# Complaint
def submit_complaint():
    student = input("Enter Student Name: ")
    issue = input("Enter Issue: ")

    data = {
        "student": student,
        "issue": issue
    }

    response = requests.post(f"{API}/complaint", json=data)
    
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print("Error:", response.text)


# Menu
print("1. Apply Gate Pass")
print("2. Submit Complaint")

choice = input("Enter choice: ")

if choice == "1":
    apply_gate_pass()
elif choice == "2":
    submit_complaint()
else:
    print("Invalid choice")