from models.problem import Problem

class ProblemController:
    """
    This class acts as a controller to handle the operations related to problems, 
    such as reporting and viewing problems.
    """

    def report_problem(self, title, description, location, reporter):
        """
        Creates a new Problem object and saves it to the database.
        :param title: Title of the problem
        :param description: Description of the problem
        :param location: Location of the problem
        :param reporter: Name of the reporter
        """
        # Create a new Problem instance with the provided details
        problem = Problem(title=title, description=description, location=location, reporter=reporter)
        # Save the problem to the database
        problem.save()
        # Notify the user
        print("\nProblem reported successfully.")

    def view_problems(self):
        """
        Fetches and displays all problems from the database.
        """
        # Fetch all problems from the database
        problems = Problem.fetch_all()

        if problems:
            # Display each problem if there are any
            print("List of Reported Problems:")
            for problem in problems:
                print(f"ID: {problem[0]}, Title: {problem[1]}, Description: {problem[2]}, "
                      f"Location: {problem[3]}, Reporter: {problem[4]}")
        else:
            # Notify the user if there are no problems
            print("No problems have been reported yet.")
