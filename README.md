## BUILDING LISTING OF REAL ESTATE APP USING DJANGO V3.2
https://github.com/gurnitha/django-bt-realestate


### 1. COMPLETE SETUP
### ------------------


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
### -------------------------------------------


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



### 3. ADDING THEME
### ---------------


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
### ---------------


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
### -----------


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
### ----------------------------


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



### 7. LISTINGS CRUD (READ)
### -----------------------


#### 7.1 Create listing_list page TVU and add template thame to it

        modified:   README.md
        new file:   apps/listings/templates/listings/listing_list.html
        new file:   apps/listings/urls.py
        modified:   apps/listings/views.py
        modified:   realestate/urls.py
        modified:   templates/inc/navbar.html


#### 7.2 Read and render listings from db to listing_list page

        modified:   README.md
        modified:   apps/listings/templates/listings/listing_list.html
        modified:   apps/listings/views.py
        new file:   media/photos/2021/11/13/home-6.jpg
        ...
        modified:   realestate/settings.py


#### 7.3 Create listing_detail page TVU and add template thame to it


        modified:   README.md
        new file:   apps/listings/templates/listings/listing_detail.html
        modified:   apps/listings/templates/listings/listing_list.html
        modified:   apps/listings/urls.py
        modified:   apps/listings/views.py
        new file:   realestate/static/assets/img/homes/home-1.jpg
        ...
        new file:   realestate/static/assets/img/homes/home-inside-6.jpg


#### 7.4 Read and render listing single from db to listing_detail page

        modified:   README.md
        modified:   apps/listings/templates/listings/listing_detail.html
        modified:   apps/listings/views.py



### 8. PAGINATION
### -------------


#### 8.1 PART 1: Workin on listing_list view - Get the pages from the db

        modified:   README.md
        modified:   apps/listings/views.py


#### 8.2 PART 2: Workin on listing_list page - Showing the pagination (showing no-previous mark)

        modified:   README.md
        modified:   apps/listings/templates/listings/listing_list.html


#### 8.3 PART 3: Workin on listing_list page - Showing the pagination (showing the: previous, active and not active link)

        modified:   README.md
        modified:   apps/listings/templates/listings/listing_list.html


#### 8.4 PART 4: Workin on listing_list page - Showing the pagination (showing the NEXT)

        modified:   README.md
        modified:   apps/listings/templates/listings/listing_list.html



### 9. LISTINGS CRUD (READ)
### -----------------------


#### 9.1 Display listings ORDER BY the most recent and filter by is_published

        modified:   README.md
        modified:   apps/listings/views.py



### 10. MAKING THE HOME AND ABOUT PAGE DYNAMIC
### ------------------------------------------


#### 10.1 Displaying listings (with limit 3) to home page

        modified:   README.md
        modified:   apps/pages/templates/pages/index.html
        modified:   apps/pages/views.py


#### 10.2 Displaying Team of Realtors to the about page

        modified:   README.md
        modified:   apps/pages/templates/pages/about.html
        modified:   apps/pages/views.py


#### 10.3 Displaying SELLER OF THE MONTH Realtor to the about page

        modified:   README.md
        modified:   apps/pages/templates/pages/about.html


#### 10.4 Modified README.md file

        modified:   README.md



### 11. DEPLOY TO GITHUB
### --------------------


#### 11.1 Create a new repository and deploy the project to Github

        https://github.com/gurnitha/django-bt-realestate

        modified:   README.md





























































































































