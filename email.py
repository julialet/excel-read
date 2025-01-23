import win32com.client as win32

#  Integração com o Outlook
outlook = win32.Dispatch("outlook.application")

# Criar um e-mail
email = outlook.CreateItem(0)

faturamento = 1500

# Configurar informações do e-mail
email.To = "destino"
email.Subject = "assunto"
email.HTMLBody = f"""

colocar assunto aqui dentro de <tags de paragrafo>

faturamento foi de {faturamento}

"""

# anexo = "caminho do anexo"
# email.Attachments.Add(anexo)

#email.Send()
