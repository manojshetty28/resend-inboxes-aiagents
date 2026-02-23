import os
import resend

# Replace re_xxxxxxxxx with your real Resend API key, or set RESEND_API_KEY env var
resend.api_key = os.environ.get("RESEND_API_KEY", "re_TTdCPzzY_4sgXBU8K6sPyBCyVKpo5vgt6")

r = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": "manojshettyjava@gmail.com",
    "subject": "Hello World",
    "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})

print(r)
