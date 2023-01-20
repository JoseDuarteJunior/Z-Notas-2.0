# modulo z-mail para envio do e-mail de serviço
import smtplib

import PySimpleGUIQt as sg
import config
configuracoes_mail = open('config_mail.txt','r')
conteudo_configuracoes_mail = configuracoes_mail.read().splitlines()
configuracoes_mail.close()

cfg_email_srv = conteudo_configuracoes_mail[0]
cfg_senha_srv = conteudo_configuracoes_mail[1]
cfg_smtps_srv = conteudo_configuracoes_mail[2]
cfg_porta_srv = conteudo_configuracoes_mail[3]
cfg_email_dst = conteudo_configuracoes_mail[4]



#sent_from = config.email_sender

to = cfg_email_dst
subject = 'Aviso Z-Notas Falha'
body = 'O sistema apresentou uma falha grave ao tentar logar no e-mail das notas e foi incapaz de recuperar, por favor consulte a tela onde esta executando e volte a executar'
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (cfg_email_srv, to, subject, body)

def world():
    try:
        smtp_server = smtplib.SMTP_SSL(cfg_smtps_srv, cfg_porta_srv )
        smtp_server.ehlo()
        smtp_server.login(cfg_email_srv, cfg_senha_srv)
        smtp_server.sendmail(cfg_email_srv, to, email_text)
        smtp_server.close()
        print ("Email enviado com sucesso")
    except Exception as ex:
        print ("incapaz de enviar e-mail",ex)

def world_new():
    try:
        #print (config.email_sender)
        smtp_server = smtplib.SMTP_SSL(config.email_smtps, config.email_porta )
        smtp_server.ehlo()
        smtp_server.login(config.email_sender, config.email_senha)
        smtp_server.close()
        sg.popup('Tudo Certo', 'Informações corretas clique em salvar configurações')
    except:
        sg.popup('Atenção', 'Informações de e-mail inválidas, o e-mail não podera ser enviado, desmarque o envio ou ajuste as informações !')