# Eventex

Sistema de eventos encomendado pela morena 

##Como desenvolver
1. clone o repositório 
2. crie um virtual env com python 3.5
3. Ative o seu virtualenv
4. Instale as dependencias.
5. Configure a instancia com .env
6. Execute os testes
```console
git clone git@github.com:cordjr/eventex.com wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp conttrib/env-sample .env
python manage.py test
```


##Como fazer o deploy
1. Crie uma instancia para o heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para instancia
4. Defina DEBUG False
5. Configure o servió de email
6. Envie o codigo para o heroku
```console
heroku create minha instancia
heroku config:push
heroku config:set SECRET_KEY=´python conttrib/secret_gen.py`
heroku config:set DEBUG=False
#configura o email
git push heroku master --force
```


