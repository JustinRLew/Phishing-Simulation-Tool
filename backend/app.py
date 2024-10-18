import os
import re  # For regular expression to validate email
from flask import Flask, request, jsonify, render_template
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, TrackingSettings, ClickTracking, OpenTracking

app = Flask(__name__)

# Set your SendGrid API key (use environment variable for production)
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY', 'your-api-key')

# Regular expression to validate email format
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

@app.route('/')
def index():
    # Render the HTML form
    return render_template('index.html')

# Route to send phishing emails
@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        # Extract the email details from the request body (JSON)
        data = request.json
        recipient_email = data.get('to')
        subject = data.get('subject')
        body = data.get('body')

        # Validate the email format
        if not EMAIL_REGEX.match(recipient_email):
            return jsonify({"error": "Invalid email address"}), 400

        # Construct the HTML content including a phishing link
        html_content = f'''
            <p>Hello,</p>
            <p>This is a test phishing email. Do not click the link below:</p>
            <a href="https://github.com/JustinRLew/Phishing-Simulation-Tool">Click here</a>
            <p>{body}</p>
        '''

        # Create the email message
        message = Mail(
            from_email='your-verified-email@example.com',
            to_emails=recipient_email,
            subject=subject,
            html_content=html_content  # Using HTML content for proper tracking
        )

        # Enable tracking settings for clicks and opens
        tracking_settings = TrackingSettings()
        tracking_settings.click_tracking = ClickTracking(enable=True, enable_text=True)
        tracking_settings.open_tracking = OpenTracking(enable=True)
        message.tracking_settings = tracking_settings

        # Send the email via SendGrid
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)

        # Return success message
        return jsonify({"message": "Email sent successfully", "status": response.status_code}), 200

    except Exception as e:
        # Return any errors that occur during the process
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
