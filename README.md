# vuejs-django-luisfred

Tutorial de VueJS com Django segundo o tutorial de Luis Fred.

Nesse tutorial Luis Fred ensina a usar [VueJS e Django](https://www.youtube.com/watch?v=rxLZg4PqC8M) sem DRF. Mas ensina também a usar `vue-cli` e componentes.

"VueJS com Django: Aprenda a usar o poderoso VueJS junto com o Django Framework, e criar componentes single file, com a extensão .vue." _Luis Fred_

Blog: http://blog.luisfred.com.br

Código: https://bitbucket.org/luisfredgs/django-vuejs


## Como desenvolver?

```
git clone https://github.com/rg3915/vuejs-django-luisfred.git
cd vuejs-django-luisfred
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
```

## Tutorial

### Backend

```
python3 -m venv .venv
source .venv/bin/activate
pip install django dj-database-url dj-static django-extensions python-decouple
pip freeze > requirements.txt
django-admin.py startproject myproject .
cd myproject
python ../manage.py startapp core
cd ..
echo "node_modules/" >> .gitignore
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
```



### Frontend

Iniciando com vue-cli

`vue init`


```
touch .babelrc
touch package.json
touch webpack.config.js
mkdir -p myproject/templates/core
touch myproject/templates/{base,nav}.html
touch myproject/templates/core/index.html
mkdir -p myproject/static/{css,js,public}
mkdir -p myproject/static/js/components
touch myproject/static/css/starter-template.css
touch myproject/static/js/app.js
touch myproject/static/js/components/exemplo.vue
```

Instalando tudo

`npm install`


Compilando tudo

`$ webpack`




Fiz com [vue-resource](https://github.com/pagekit/vue-resource) `$http` e com [axios](https://github.com/axios/axios).

