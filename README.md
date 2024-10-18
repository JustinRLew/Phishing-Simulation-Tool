# Phishing-Simulation-Tool

Phishing Simulation Tool
This is a phishing simulation tool that allows users to send phishing emails using the SendGrid API and tracks email interactions such as opens and clicks. The tool demonstrates full-stack development by integrating a simple front-end form with a back-end Flask application.

Features
Send Phishing Emails: Users can enter a recipient's email, subject, and message body, and the system will send a phishing email with a test link.
Email Tracking: The SendGrid API handles tracking for when recipients open the email or click the phishing link.
Full-Stack Application: The tool uses an HTML front-end, JavaScript for form submission, and a Python Flask back-end to process and send the emails.

Tech Stack
Back-End: Python, Flask
Front-End: HTML, JavaScript (Fetch API)
Email Service: SendGrid API

Project Structure
bash

.
├── backend
│   ├── app.py                # Flask back-end logic
│   ├── templates/
│   │   └── index.html         # Front-end form for sending emails
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies

Requirements
To run this project locally, you need:

Python 3.8+
SendGrid API Key (You can sign up for an account at sendgrid.com)
Flask and SQLAlchemy for Python
JavaScript for handling the front-end form

Installation
Follow these steps to get the project up and running:

1. Clone the repository
bash

git clone https://github.com/your-username/phishing-simulation-tool.git
cd phishing-simulation-tool

2. Set up a virtual environment (optional, but recommended)
bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
Install the required Python packages:

bash

pip install -r requirements.txt

4. Set up SendGrid API Key
You'll need to export your SendGrid API key as an environment variable:

bash

export SENDGRID_API_KEY='your-sendgrid-api-key'
On Windows:

bash

set SENDGRID_API_KEY='your-sendgrid-api-key'

5. Run the Flask app
Start the Flask server:

bash

python backend/app.py

6. Open the Application
Visit the following URL in your web browser:

arduino

http://127.0.0.1:5000/
Usage
Open the tool in your browser.
Fill in the recipient's email, subject, and message body.
Click Send Phishing Email.
The tool will use SendGrid to send the email and display a success or error message.

Screenshots
Phishing Email Form

SendGrid Dashboard (Email Tracking)

Future Improvements
Campaign Management: Add a system to track multiple phishing campaigns.
Recipient Statistics: Show detailed reports for recipients, including who opened the email or clicked the link.
Authentication: Add user authentication to restrict access to the tool.

License
This project is licensed under the MIT License - see the LICENSE file for details.
