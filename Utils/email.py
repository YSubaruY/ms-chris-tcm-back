import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

class EmailService:
    @staticmethod
    def send_credential_email(email, username, password, first_name):
        host = os.getenv('SMTP_HOST')
        port = int(os.getenv('SMTP_PORT'))
        smtp_user = os.getenv('SMTP_USER')
        smtp_password = os.getenv('SMTP_PASSWORD')
        sender_email = os.getenv('SMTP_SENDER_EMAIL')

        subject = "Bienvenido - Tus credenciales de acceso"
        body = f"""
            Buenos días {first_name},

            Aquí están tus credenciales de acceso:

            Usuario: {username}
            Contraseña: {password}

            Por favor, no compartas esta información con nadie.

            Saludos,
            El equipo de soporte
            """
        receiver_emails = [email]
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ", ".join(receiver_emails)
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP(host, port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            text = message.as_string()
            server.sendmail(sender_email, receiver_emails, text)
            print("Correo con credenciales enviado exitosamente!")
            return True
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            return False
        finally:
            server.quit()