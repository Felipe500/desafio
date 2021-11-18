

# SOBRE O PROJETO
15/11/21 19:40:
<br>
Para este projeto eu decide montar a seguinte estrutura.

Front-end: HTML, CSS E bootstrap v4.6.1. <br>
Back-end: Python com o framework Django.

Estrutura:
--> Django projeto: Portal_Scale_News
    <br>
        -->Apps: Home, Post_noticias, Post_Comentarios e User_perfil(Ainda falta implementar).
<br><br>Estrutura dos templates : <br>
-->Portal_Scale_News/templates/base.html - Inclui navbar.htm e footer.html. Pagina principal para carregamento de recursos vindo do bootstrap.<br>
-->Portal_Scale_News/templates/navbar.html - Contém link para rota inicial da aplicação e o link para todas categorias de noticias cadastradas no banco de dados.<br>
-->Portal_Scale_News/templates/footer.html - Contém informações de contato e o ano atual.<br>


16/11/21 07:39<br>
Criando teste otimizados e automatizando com pycharm para executar comandos no manage.py.<br>
comandos: runserver, migrate, makemigrations, createsuperuser(criar usuario admin).<br>

Buscando modelos de templates para facilitar o desenvolvimento do front-end:<br>
 - Layout: Bootstrap 4.6.1 link documentação - https://getbootstrap.com/docs/4.6/getting-started/introduction/ <br>

 - Icones: link - https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css <br>
 - Sesão de comentarios: link - https://bbbootstrap.com/snippets/bootstrap-nested-comment-section-reply-72244546 <br>
 - Resposta de envio de comentario: link - https://www.w3schools.com/bootstrap4/tryit.asp?filename=trybs_ref_js_alert&stacked=h <br>




17/11/21 09:12:


13/11/21 17:25:
Criando as primeiras otimizações:
 - Verficando código repetido.  
 - Primeiros testes em massa pelo arquivos input.txt

 - Criando mecanismo de remoção de usuários quando os mesmo atingem o limite de tarefas ou ttask permitida.