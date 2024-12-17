from models.problem import Problem

class ProblemController:
    def report_problem(self, title, description, location, reporter):
       
        problem = Problem(title=title, description=description, location=location, reporter=reporter)
        problem.save()
        print("Problem reported successfully.")

    def view_problems(self):
        
        problems = Problem.fetch_all()
        if problems:
            print("List of Reported Problems:")
            for problem in problems:
                print(f"ID: {problem[0]}, Title: {problem[1]}, Description: {problem[2]}, "
                      f"Location: {problem[3]}, Reporter: {problem[4]}")
        else:
            print("No problems have been reported yet.")
