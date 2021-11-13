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


### 4. LISTINGS

#### 4.1 Create a new app 'apps/listings' and register it to the project

        modified:   README.md
        new file:   apps/listings/__init__.py
        new file:   apps/listings/admin.py
        new file:   apps/listings/apps.py
        new file:   apps/listings/migrations/__init__.py
        new file:   apps/listings/models.py
        new file:   apps/listings/tests.py
        new file:   apps/listings/views.py
        modified:   realestate/settings.py
        new file:   realestate/static/assets/img/favicon.png
        modified:   templates/inc/head.html

#### 4.2 Create Listing model, run migration and register Listing to admin

        modified:   README.md
        modified:   apps/listings/admin.py
        new file:   apps/listings/migrations/0001_initial.py
        modified:   apps/listings/models.py


### 5. REALTORS

#### 5.1 Create a new app 'apps/realtors' and register it to the project

        modified:   README.md
        new file:   apps/realtors/__init__.py
        new file:   apps/realtors/admin.py
        new file:   apps/realtors/apps.py
        new file:   apps/realtors/migrations/__init__.py
        new file:   apps/realtors/models.py
        new file:   apps/realtors/tests.py
        new file:   apps/realtors/views.py
        modified:   realestate/settings.py

#### 5.2 Create Realtor model, run migration and register Realtor to admin

        new file:   apps/listings/migrations/0002_listing_realtor.py
        modified:   apps/listings/models.py
        modified:   apps/realtors/admin.py
        new file:   apps/realtors/migrations/0001_initial.py
        modified:   apps/realtors/models.py


#### 5.3 Inserting dumy data of Listing and Realtor to db

        modified:   README.md
        modified:   apps/realtors/models.py
        new file:   media/photos/2021/11/12/home-1.jpg
        ...
        new file:   media/photos/2021/11/12/home-2.jpg
        new file:   media/photos/2021/11/12/home-3.jpg


### 6. CUSTOMIZING ADMIN DISPLAY

#### 6.1 Customizing colors of the admin panel

        modified:   README.md
        new file:   realestate/static/assets/css/admin.css
        new file:   templates/admin/base_site.html

#### 6.2 Customizing list_display etc of the Listing in the admin panel

        modified:   README.md
        modified:   apps/listings/admin.py

#### 6.3 Customizing list_display etc of the Realtor in the admin panel

        modified:   README.md
        modified:   apps/realtors/admin.py
































































































































































