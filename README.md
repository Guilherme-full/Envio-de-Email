# Envio-de-Email (Guilherme Xavier Souza)

## Clonar Repositório
```
git clone https://github.com/Guilherme-full/Envio-de-Email.git
```

|          | Linux | macOS | Windows |
|   :---   | :---: | :---: | :---:   |
| Chromium <!-- GEN:chromium-version -->93.0.4543.0<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| WebKit <!-- GEN:webkit-version -->14.2<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Firefox <!-- GEN:firefox-version -->89.0<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |

## Descrição
Código realizado em Python para teste, no qual consiste no envio de email, utilizando a biblioteca smtplib

## Biblioteca
```
import smtplib
```

## Função

```
def enviar_email(email, senhaApp, email_Envio, destinatario, mensagem):
    try:
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
```

## Mensagem 
```
print('''Olá Usuario, este programa tem a finalidade de enviar e-mail, para que seja enviado com sucesso,
faça login em seu e-mail, vá em gerenciar conta, na parte de segurança, ative a verificação em duas etapas,
após concluido, gere uma senha de APP, e quando estiver utilizando este programa, basta apenas inserir seu e-mail,
e sua senha de APP para fazer login, para fazer o envio, informe novamente seu email, o destinatario e por fim a
mensagem.''')
```

## Corpo do Programa
```
login = input('Informe seu e-mail para login: ')
senha = input('Informe sua senha de APP: ')
envio_ = input('Informe novamente seu e-mail para envio: ')
dest = input('Qual o Destinatario: ')
men = input('Digite sua Mensagem: ')
enviar_email(login, senha, envio_, dest, men)
```

## Linguagem e Ferramenta
<img align="center"  alt="Python" heigth= "40" width ="60" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"></img>
<img align="center"  alt="Pycharm" heigth= "40" width ="60" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pycharm/pycharm-original.svg"></img>

