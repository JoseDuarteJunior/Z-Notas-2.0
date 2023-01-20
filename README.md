<p style="text-align:center;"><strong>Z-Notas-XML V.2</strong></p>
<hr>
<p>Este software foi desenvolvido para auxiliar no processo de captação de notas fiscais recebidas por e-mail de forma a automatizar as rotinas de captação e adequeção do nome dos arquivos.<br>Ele faz o download das notas XML recebidas em anexo nos e-mails, renomeia os arquivos de acordo com a chave da nota e depois salva as mesmas em uma pasta de saída.</p>
<hr>
<ul>
    <li><strong>Instalação</strong>
        <ul>
            <li><strong>​</strong>1 - ​Execute o instalador :<img class="image_resized" style="width:190px;" src="https://github.com/JoseDuarteJunior/Z-Notas-XML/raw/main/manual1.png"><strong>&nbsp;</strong></li>
            <li>2 - Coloque na pasta raiz :&nbsp;</li>
        </ul>
    </li>
</ul>
<p><img class="image_resized" style="width:585px;" src="https://github.com/JoseDuarteJunior/Z-Notas-XML/raw/main/manual2.png"></p>
<p>3 - O software vai se instalar.</p>
<hr>
<ul>
   <li><strong>Execução</strong>
        <ul>
            <li>1 - &nbsp;Execute o software que esta na pasta de instalação :&nbsp; <img class="image_resized" style="width:138px;" src="https://github.com/JoseDuarteJunior/Z-Notas-2.0/blob/main/inst1.jpg"></li>
            <li>2 - O programa irá mostrar a tela de configuração.</li>
        </ul>
    </li>
</ul>
<hr>
<ul>
   <li><strong>Tela Inicial</strong><br><br><img class="image_resized" style="width:648px;" src="https://github.com/JoseDuarteJunior/Z-Notas-2.0/blob/main/tela1.jpg">
        <ul>
            <li><strong>Rodar:</strong> Executa o software na configuração atual<br><br>&nbsp;</li>
            <li><strong>Configurar:</strong> Abre a tela para configuração do sistema<br><br>&nbsp;</li>
</ul>
    </li>
</ul>
<hr>
<p><br><br>&nbsp;</p>
<ul>

   <li><strong>Configurações</strong><br><br><img class="image_resized" style="width:648px;" src="https://github.com/JoseDuarteJunior/Z-Notas-2.0/blob/main/tela2.jpg">
        <ul>
        <li><strong>Somente processar pasta de arquivos:</strong> Se esta opção estiver marcada o software vai apenas varrer a pasta temp renomear os arquivos xml com sua chave de nota e mover para Pasta, com esta opção o software não conecta nos e-mails<br><br>&nbsp;</li>
            <li><strong>Email:</strong> Deve ser inserido o e-mail onde as notas são recebidas, caso seja em mais de um endereço use a virgula para separar os endereços ex email1@mail.com,email2@mail.com<br><br>&nbsp;</li>
            <li><strong>Senha:</strong> Deve ser inserido a(s) senha(s) do(s) e-mail(s) colocados no item anterior, usando a mesma regra de virgula caso seja mais de um e-mail<br><br>&nbsp;</li>
            <li><strong>Porta:</strong> Deve ser inserido a porta de conexão usada no e-mail no formato IMAP, a versão atual suporta somente IMAP.<br><br>&nbsp;</li>
            <li><strong>Dias Antes:</strong>&nbsp;Deve ser inserido a quantidade de dias anteriores a data presente em que o software deve verificar ,valor de exemplo: 5, o software iria baixar as notas recebidas de até 5&nbsp;dias antes a data da execução.<br><br>&nbsp;</li>
            <li><strong>Tempo Min.: </strong>Tempo de repetição da verificação de entrada dos e-mails, o formato do valor é&nbsp;minutos, &nbsp;recomendado não deixar este valor abaixo de 5 pois dependendo do servidor de e-mail pode pensar que é algum ataque e bloquear.<br><br>&nbsp;</li>
            <li><strong>Tamanho XML: </strong>Tamanho da chave XM contida na nota, por padrão este valor é de 44 caracteres numéricos.<br><br>&nbsp;</li>
            <li><strong>Pasta Temp.: </strong>Pasta temporária de trabalho, nesta pasta fica o arquivo log.txt que não deve ser apagado ou removido podendo gerar erros ao software. *Pode ser modificada pelo usuário.<br><br>&nbsp;</li>
            <li><strong>Pasta: </strong>Pasta local ou remota aonde ficarão armazenadas as notas fiscais já processadas pela software.&nbsp; *Pode ser modificada pelo usuário.<br><br>&nbsp;</li>
            <li><strong>Limpeza Log:</strong> Tempo em dias para limpeza do arquivo de log, lembrando que este tempo deve ser sempre maior que o valor do campo Dias Antes, dessa forma o software não irá baixar novamente as mesmas notas.<br><br>&nbsp;</li>
            <li><strong>Pasta Erro:</strong> Pasta onde as notas que não puderam ser processadas pelo software são mantidas. *Pode ser modificada pelo usuario.</li>
        </ul>
    </li>
</ul>
<hr>
<ul>
    <li><strong>Extras</strong><br><br><img class="image_resized" style="width:648px;" src="https://github.com/JoseDuarteJunior/Z-Notas-2.0/blob/main/tela3.jpg">
        <ul>
            <li><strong>Mandar e-mail reportando erros:</strong> Se esta opção estiver marcada o software vai enviar e-mails para o endereço configurado quando algo der errado e sua execução for interrompida<br><br>&nbsp;</li>
            <li><strong>Email de serviço:</strong> Endereço de e-mail que va enviar a mensagem de erro<br><br>&nbsp;</li>
            <li><strong>Senha do Email de serviço:</strong> Senha deste e-mail<br><br>&nbsp;</li>
            <li><strong>Servidor SMTPS do Email de serviço:</strong> Endereço do servidor SMTPS do e-mail de serviço<br><br>&nbsp;</li>
            <li><strong>Porta do Email de serviço:</strong>Porta do servidor de serviços<br><br>&nbsp;</li>
            <li><strong>E-mail de destino:</strong>Endereço de e-mail para o qual vai ser enviado a mensagem de erro<br><br>&nbsp;</li>
            <li><strong>Testar E-mail:</strong>Este botão testa os dados inseridos e se o serviço estiver funcionando ele confirma<br><br>&nbsp;</li>
            <li><strong>Salvar dados:</strong>Este botão salva os dados do envio do e-mail de relatorio de erro<br><br>&nbsp;</li>
        </ul>
    </li>
</ul>
<hr>
<ul>
    <li><strong>Utilização</strong>
        <ul>
            <li>Após validar as configurações caso tenha alterado alguma precione salvar, o software irá encerrar na próxima execução as configurações alteradas terão efeito, rode novamente e clique em rodar o software vai para a tray do computador.</li>
        </ul>
    </li>
</ul>
<hr>
<ul>
    <li><strong>Interface</strong>
        <ul>
            <li><strong>Configurações - </strong>Abre a tela anterior</li>
            <li><strong>Zerar Contador - </strong>Limpa o contador de notas baixadas desde a execução</li>
            <li><strong>Sobre - </strong>Informações sobre versão e updates</li>
            <li><strong>Ajuda - </strong>Este documento</li>
            <li><strong>Exit - </strong>Encerra o software</li>
        </ul>
    </li>
</ul>
<p><img class="image_resized" style="width:162px;" src="https://github.com/JoseDuarteJunior/Z-Notas-XML/raw/main/manual4.png"></p>
<hr>
<ul>
    <li><strong>Informações​​​​​​​</strong>
        <ul>
            <li><strong>​​​​​​​</strong>Este software está em fase de desenvolvimento, logo seu funcionamento pode apresentar instabilidades e variar conforme a plataforma onde sera instalado, favor reportar problemas, duvidas ou sugestões para o e-mail : duarte936@gmail.com.</li>
        </ul>
    </li>
</ul>
<p>&nbsp;</p>
<p><br>&nbsp;</p>
