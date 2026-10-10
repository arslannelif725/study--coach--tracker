# Study Coach & Tracker

#### Video Demo: <https://youtu.be/518jdaaHSOc>

#### Description:
Study Coach & Tracker is a comprehensive Command Line Interface (CLI) application built in Python to assist students and learners in managing, logging, and analyzing their study sessions effectively. Keeping track of study habits, subject choices, time allocation, and the volume of practice questions solved is crucial for academic progress. This project aims to simplify that process through a clear and structured interactive workflow.

The core motivation behind Study Coach & Tracker is to provide immediate analytical feedback on daily learning sessions. When students engage in self-study, they often lose track of how efficiently they are working. By recording the duration spent on each subject alongside the total number of questions answered, the application calculates key performance metrics such as average time spent per question. This allows users to identify subjects where they need to build speed or adjust their study pacing.

#### Key Features:
- **Interactive Session Logging:** Prompts the user to continuously enter study data including the subject name, total duration in minutes, and total questions solved. The loop seamlessly terminates when the user presses Enter without typing a course name.
- **Robust Input Validation:** Implements exception handling to guard against common input errors. Negative durations, negative question counts, and empty course names trigger descriptive value errors, ensuring data integrity.
- **Formatted Table Output:** Converts raw session dictionaries into a visually appealing ASCII table using the `tabulate` library, providing a clean summary of the entire study log.
- **Performance Analytics:** Computes overall metrics across all recorded sessions, including aggregate study time, total solved questions, and the precise average time required per question.

#### File Structure & Implementation Details:
- `project.py`: Serves as the primary executable file containing the core program logic. It defines `main()` alongside three mandatory custom functions required by the project specifications:
  - `add_session(subject, duration, questions)`: Validates individual session inputs and constructs a dictionary representation of the study log.
  - `calculate_summary(sessions)`: Accepts a list of study session dictionaries to compute total time, total questions, and average metrics.
  - `format_table(sessions)`: Formats the collected session logs into a structured grid using `tabulate`.
- `test_project.py`: Contains thorough unit test suites utilizing `pytest`. It tests valid and invalid inputs for `add_session`, mathematical calculations in `calculate_summary`, and output contents from `format_table`.
- `requirements.txt`: Specifies external package dependencies needed for running the application, specifically `tabulate` and `pytest`.
- `README.md`: Provides exhaustive project description, architectural documentation, and usage guidelines.
