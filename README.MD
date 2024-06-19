# Project Ticket Automation

This Python script automates the creation and linking of tickets in a project management system using the GitLab API. It reads ticket data from an Excel file and interacts with the GitLab API to create user stories and tasks, as well as link tasks to their respective user stories.

## Features

- **Ticket Creation**: Creates tasks for each user story and links them to the respective user story.
- **Avoids Duplicates**: Skips creating duplicate tasks and only creates new tasks if they do not already exist.

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/yourusername/project-ticket-automation.git
   ```

2. Navigate to the project directory:

   ```
   cd project-ticket-automation
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have Python installed on your machine.
2. Set up your GitLab API access token and configure it in the `config.py` file.
3. Prepare your ticket data in an Excel file named `Tasks.xlsx` with the following columns:

   - Ticket Name
   - Assignee
   - Milestone
   - Due Date
   - Labels

4. Run the script `main.py`:

   ```
   python main.py
   ```

## Configuration

- Update the `config.py` file with your GitLab API access token and project ID.

## Example Excel Data

The Excel file `Tasks.xlsx` should have the following structure:

| Ticket Name                                          | Assignee    | Milestone | Due Date  | Labels                            |
|------------------------------------------------------|-------------|-----------|-----------|-----------------------------------|
| User Story >> Authentication >> UAA001 >> Login     |             | Sprint 1  | 6/28/2024 | ["User_Story"]                    |
| Task >> Authentication >> Frontend >> Login          | Suman Rimal | Sprint 1  | 6/28/2024 | ["CAT_REGULAR", "PLAT_FRONTEND"] |
| Task >> Authentication >> Backend >> Login           | Suman Rimal | Sprint 1  | 6/29/2024 | ["CAT_REGULAR", "PLAT_BACKEND/CMS"]|
| Task >> Authentication >> API >> Login               | Suman Rimal | Sprint 1  | 6/30/2024 | ["CAT_REGULAR", "PLAT_API"]       |
| Task >> Authentication >> QA >> Login                | Suman Rimal | Sprint 1  | 7/1/2024  | ["CAT_REGULAR", "PLAT_QA"]        |

## Support

For any issues or questions, please open an issue in the GitHub repository or contact [Suman Rimal](mailto:sumanrimalconnect@gmail.com).



---

Feel free to customize this README.md file further based on your project's specific details and requirements.