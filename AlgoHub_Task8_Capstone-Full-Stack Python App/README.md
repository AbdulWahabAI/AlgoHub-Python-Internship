# Capstone: Full-Stack Python Application
## Internship Week 8 Project - AlgoHub Software House

### Project Overview
This project serves as the final capstone application for the AlgoHub Python Programming Internship. The primary objective was to design and deploy an end-to-end Python application that bridges backend data processing with an interactive frontend. This application demonstrates a decoupled system architecture, where a RESTful API handles data logic and a dynamic dashboard manages user interaction.

### Tech Stack
To achieve professional-grade performance and maintainability, the following technologies were utilized:
*   **Backend**: FastAPI (High-performance API development with automatic Swagger documentation).
*   **Frontend**: Streamlit (Data-driven UI for real-time visualization).
*   **Database ORM**: SQLAlchemy (Object-Relational Mapping for database management).
*   **Database**: SQLite (Lightweight, serverless relational database).
*   **Testing**: pytest (Ensuring code reliability and robustness).
*   **Version Control**: Git & GitHub.

### Project Functionality
The application allows users to perform CRUD operations through a clean interface:
1.  **Data Entry**: Users can add items via the sidebar form, which are processed by the FastAPI backend and stored in the SQLite database.
2.  **Data Retrieval**: The application fetches and displays all stored items in an organized, expandable format.
3.  **Scalability**: The modular structure ensures that additional endpoints or features can be integrated easily.

### How to Run Locally
1. **Clone the Repository**:
   ```bash
   git clone <your-repository-url>
   cd AlgoHub_Task8_Capstone

 ## Setup Virtual Environment:
 python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

##  Install Dependencies:
pip install -r requirements.txt

##  Launch the Application:
##  ​Backend: Run 
uvicorn backend.main:app --reload
##  ​Frontend: Open a new terminal and run
 streamlit run frontend/app.py

 ## Project Submission Links
* **LinkedIn Project Post:** [Click Here to View Post](https://www.linkedin.com/posts/abdul-wahab-1077a3291_python-fastapi-streamlit-ugcPost-7496619399047618560-tgCk/?utm_source=share&utm_medium=member_android&rcm=ACoAAEbGitcBzdgikeoEnOEahLBrZMgjtI0ItY)
* **Demo Video:** [Click Here to Watch Video](https://drive.google.com/file/d/1dQagaf1Uk9Dw5t7_uPTONMpOEAH2ZxK1/view?usp=drivesdk)

​Developed by Abdul Wahab | AlgoHub Python Programming Intern