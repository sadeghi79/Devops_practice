from agent.analyzer import analyze_logs
from agent.generator import generate_file
from agent.monitor import health_check

def menu():
    print("\n🤖 DevOps AI Agent – Choose an option:")
    print("1. Analyze Logs")
    print("2. Generate DevOps File")
    print("3. Health Check")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter option: ")

    if choice == "1":
        path = input("Enter log file path: ")
        print(analyze_logs(path))
    elif choice == "2":
        file_type = input("What file to generate? (docker/nginx/github-actions): ")
        print(generate_file(file_type))
    elif choice == "3":
        print(health_check())
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
