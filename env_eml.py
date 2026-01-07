import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def enviar_email(
        remetente,
        senha,
        destinatario,
        assunto,
        corpo,
        anexo_path=None
):
    # configuraçã da mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # corpo do email
    msg.attach(MIMEText(corpo, 'plain'))

    if anexo_path and os.path.isfile(anexo_path):
        with open(anexo_path, "rb") as anexo:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(anexo.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Dispostion',
                f'attachment; filename={os.path.basename(anexo_path)}'
            )
            msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        print("Email enviado com sucesso!") 
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

enn_mails.enviar_email(
                remetente= #email do envio,
                senha= #espaço pra senha de autenticação de dois fatores,
                destinatario= #destino do email,
                assunto= #assunto da mensagem,
                corpo= #escreva alguma coisa para o corpo do email,
                anexo_path=None #deixa mesmo assim como none
            )