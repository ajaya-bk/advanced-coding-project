from controllers.problem_controller import ProblemController

def main():
    controller = ProblemController()

    while True:
        print("\nCommunity Problem Reporter")
        print("1. Report a Problem")
        print("2. View All Problems")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the problem: ")
            description = input("Enter a description of the problem: ")
            location = input("Enter the location of the problem: ")
            reporter = input("Enter your name (reporter): ")
            controller.report_problem(title, description, location, reporter)

        elif choice == "2":
            controller.view_problems()

        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
