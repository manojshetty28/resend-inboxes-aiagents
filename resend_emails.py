import os
import resend

# Replace re_xxxxxxxxx with your real Resend API key, or set RESEND_API_KEY env var
resend.api_key = os.environ.get("RESEND_API_KEY", "")

r = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": "manojshettyjava@gmail.com",
    "subject": "Hello World",
    "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})

print(r)
