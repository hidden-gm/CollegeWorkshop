# CollegeWorkshop
This repository contains a simple FastAPI backend and a frontend HTML file to demonstrate fetching data from an API and displaying it on a webpage.

Setup Instructions
1. Clone the Repository

git clone https://github.com/Syed-maaz13/CollegeWorkshop.git


2. Create a Virtual Environment
To keep dependencies organized, create a virtual environment.


# For Windows
python -m venv venv
# For macOS/Linux
python3 -m venv venv


3. Activate the Virtual Environment

# For Windows
.\venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate

4. Install Dependencies

pip install fastapi
pip install fastapi uvicorn

5. Run the FastAPI Server
Start the FastAPI server to make the API available locally.

uvicorn main:app --reload

The server will start, and you can access the API at http://127.0.0.1:8000/hello.

6. Open the HTML File
Open index.html in a web browser. Click the button to see the message from the API displayed on the webpage.