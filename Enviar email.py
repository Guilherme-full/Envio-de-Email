def enviar_email(email, senhaApp, email_Envio, destinatario, mensagem):
    try:
        import smtplib
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email, senhaApp)
        server.sendmail(email_Envio, destinatario, mensagem)
        server.quit()
    except:
        print('----------------------------------------')
        print('\033[1;31Não Foi Possivel Enviar o E-mail')
        print('----------------------------------------')
    else:
        print('----------------------------------------')
        print('\033[1;31mE-mail Enviado com Sucesso')
        print('----------------------------------------')

print('''Olá Usuario, este programa tem a finalidade de enviar e-mail, para que seja enviado com sucesso,
faça login em seu e-mail, vá em gerenciar conta, na parte de segurança, ative a verificação em duas etapas,
após concluido, gere uma senha de APP, e quando estiver utilizando este programa, basta apenas inserir seu e-mail,
e sua senha de APP para fazer login, para fazer o envio, informe novamente seu email, o destinatario e por fim a
mensagem.''')


login = input('Informe seu e-mail para login: ')
senha = input('Informe sua senha de APP: ')
envio_ = input('Informe novamente seu e-mail para envio: ')
dest = input('Qual o Destinatario: ')
men = input('Digite sua Mensagem: ')
enviar_email(login, senha, envio_, dest, men)





