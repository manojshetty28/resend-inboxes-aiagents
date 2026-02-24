# =============================================================================
# resend_emails.py
# This script sends an email using the Resend email API.
# It demonstrates basic email sending functionality with HTML content.
# =============================================================================

# Import the os module to access environment variables
import os

# Import the resend SDK for interacting with the Resend email service
import resend

# Configure the Resend API key.
# The key is retrieved from the RESEND_API_KEY environment variable.
# If the environment variable is not set, an empty string is used.
# Note: Replace with your real Resend API key, or set RESEND_API_KEY env var.
# For production use, always store API keys securely in environment variables.
resend.api_key = os.environ.get("RESEND_API_KEY", "")

# Send an email using the Resend API
# Parameters:
#   - "from": The sender email address (using Resend's onboarding domain)
#   - "to": The recipient email address
#   - "subject": The subject line of the email
#   - "html": The HTML body content of the email
r = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": "manojshettyjava@gmail.com",
    "subject": "Hello World",
    "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})

# Print the response from the Resend API (contains the email ID and status)
print(r)
