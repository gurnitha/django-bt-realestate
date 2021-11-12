## BUILDING LISTING OF REAL ESTATE APP USING DJANGO V3.2


### 1. COMPLETE SETUP

#### 1.1 Create project, app, .env db, static, media

        new file:   .gitignore
        new file:   README.md
        new file:   apps/pages/__init__.py
        new file:   apps/pages/admin.py
        new file:   apps/pages/apps.py
        new file:   apps/pages/migrations/__init__.py
        new file:   apps/pages/models.py
        new file:   apps/pages/tests.py
        new file:   apps/pages/views.py
        new file:   manage.py
        new file:   realestate/__init__.py
        new file:   realestate/asgi.py
        new file:   realestate/settings.py
        new file:   realestate/urls.py
        new file:   realestate/wsgi.py


#### 1.2 Create home page VTU

        modified:   README.md
        new file:   apps/pages/templates/pages/index.html
        new file:   apps/pages/urls.py
        modified:   apps/pages/views.py
        modified:   realestate/urls.py


#### 1.3 Create about page VTU

        modified:   README.md
        new file:   apps/pages/templates/pages/about.html
        modified:   apps/pages/urls.py
        modified:   apps/pages/views.py


### 2. BASE TEMPLATES AND TEMPLATES INHERITANCE

#### 2.1 Create base template

        modified:   README.md
        modified:   apps/pages/templates/pages/about.html
        modified:   apps/pages/templates/pages/index.html
        modified:   realestate/settings.py
        new file:   templates/base.html

#### 2.2 Template inheritance

        modified:   README.md
        modified:   apps/pages/templates/pages/about.html
        modified:   apps/pages/templates/pages/index.html
        modified:   templates/base.html
        new file:   templates/inc/head.html
        new file:   templates/inc/navbar.html


### 3. Adding Theme

#### 3.1 Adding static assets, index and about template themes

        modified:   README.md
        modified:   apps/pages/templates/pages/about.html
        modified:   apps/pages/templates/pages/index.html
        modified:   realestate/settings.py
        ...
        new file:   realestate/static/assets/webfonts/fa-solid-900.woff2
        modified:   templates/base.html
        new file:   templates/inc/footer.html
        modified:   templates/inc/head.html
        modified:   templates/inc/navbar.html
        new file:   templates/inc/scripts.html
        new file:   templates/inc/topbar.html

















































































































































































