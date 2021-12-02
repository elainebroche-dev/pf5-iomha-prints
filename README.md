<h1 align="center">Íomhá Prints - Order Prints Online</h1>

[View the live project here](https://pf5-iomha-prints.herokuapp.com/)

The Íomhá Prints project is a B2C e-commerce application which sells art prints directly to end users.  It is implemented as a retail store where users can view, search and filter the products on offer, then select items to add to their shopping cart and purchase through a simple single payment.

General users can view details of the prints available for purchase including bio information on the print artist, and can sign up to the company newletter. In addition, registered users can create a wishlist of prints they may be interested in and a profile to keep track of delivery details and order history.

Admin users can manage the lists of prints and artists, this includes being able to add new prints to the range, update pricing, link artists to prints, update artist bio information.  A full description of the available functionality is included in this document.


![Mockup](documentation/supp-images/amiresponsive.png)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Planning](#planning)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### User stories :

* EPIC 01 : Registration and Account Management
  <details>
      <summary>User Stories for EPIC 01: </summary>

  - US101 : Register for an account
      - As a **site user** I can **register for an account** so that **I can view my profile and purchasing history**
  - US102 : login and logout
      - As a **site user** I can **easily login or logout** so that **I can access my personal account information**
  - US103 : reset password
      - As a **site user** I can **easily reset my password in case I forget** so that **I can recover access to my account**
  - US104 : confirm registration via email
      - As a **site user** I can **receive an email confirmation after registering** so that **I can verify that my account registration was successful**
  - US105 : access user profile
      - As a **site user** I can **access my personalized user profile** so that **I can view my personal order history and order confirmations and my payment information**

  </details>

* EPIC 02 : Viewing and Navigation
  <details>
      <summary>User Stories for EPIC01: </summary>

  - US201 : View a list of products/prints
      - As a **site user** I can **view a list of prints** so that **I can select some to purchase**
  - US202 : View individual print details
      - As a **site user** I can **view details for a specific print** so that **I can see the description, rating, print image, available sizes and pricing**
  - US203 : View discounted items
      - As a **site user** I can **easily identify discounted items** so that **I can take advantage of savings on prints I want to purchase**
  - US204 : View shopping cart total
      - As a **site user** I can **easily view the total of my purchases at any time** so that **I can avoid over-spending**
  - US205 : Like a print
      - As a **site user** I can **'like' a print** so that **it is added to my  wishlist in my personal profile**
  - US206 : Easily understand purpose of website and how to navigate
      - As a **site user** I can **quickly identify what the website is selling and easily navigate the pages** so that **I can quickly find the information and functionality I am looking for**
  - US207 : View wishlist / liked items
      - As a **site user** I can **view my wishlist** so that **I can see prints I have 'liked'**
  - US208 : View prints by category
      - As a **site user** I can **view a specific category of prints** so that **I can quickly narrow down the range of prints I am interested in**
  - US209 : View artist bio
      - As a **site user** I can **view bio details of the artist of a specific print** so that **I can easily find out more about the artist**
  - US210 : Handle 404 and 500 errors 
      - As a **site user** I can **return to Home after http 404 or 500 response** so that **I feel I am still working within the website and can navigate easily**

  </details>

* EPIC 03 : Sorting and Searching
  <details>
      <summary>User Stories for EPIC01: </summary>

  - US301 : Sort list of available prints
      - As a **site user** I can **sort the list of available prints** so that **I can easily identify the best rated and categorically sorted products**
  - US302 : Sort a specific category of print
      - As a **site user** I can **sort a specific category of print** so that **I can find the best-rated print in a specific category or sort the prints in the category or sort the prints in that category by title**
  - US303 : Sort multiple categories of prints simultaneously
      - As a **site user** I can **sort multiple categories of prints simultaneously** so that **I can find the best-rated print in a specific category, or sort the prints across broad categories, such as "nature" or "architecture"**
  - US304 : search for a print by title or artist
      - As a **site user** I can **search for a print by title or artist** so that **I can find a specific print to purchase**
  - US305 : view search results and the number of items found
      - As a **site user** I can **easily view what I've searched for and the number of results** so that **I can quickly decide whether the print I want is available**

  </details>

* EPIC 04 : Purchasing and Checkout
  <details>
      <summary>User Stories for EPIC01: </summary>

  - US401 : Add items to shopping cart
      - As a **site user** I can **add items to my shopping cart** so that **I can choose multiple items to purchase**
  - US402 : Modify cart contents and remove items from the cart
      - As a **site user** I can **modify cart quantities and remove items from the shopping cart** so that **manage the contents of my shopping cart and rectify any mistakes in selecting purchases**
  - US403 : View notifications of user interactions
      - As a **site user** I can **get notifications on screen of my actions** so that **I can easily understand my interactions with the website and their consequences**
  - US404 : Finalize order through the checkout page
      - As a **site user** I can **complete my order by going through the checkout page** so that **I can see a final total, a summary of my order and I can specify a delivery address and payment details**
  - US405 : Implement a secure payment process
      - As a **site user** I can **enter my payment details** so that **my payment is secure**
  - US406 : View an order confirmation after checkout
      - As a **site user** I can **view an order confirmation after checkout** so that **I can see what was ordered and total costs**
  - US407 : Receive an email confirmation after checking out
      - As a **site user** I can **receive an email confirmation after checking out** so that **I have a record of my purchases**

  </details>

* EPIC 05 : Admin and Store Management
  <details>
      <summary>User Stories for EPIC01: </summary>

  - US501 : Add a print
      - As a **site admin** I can **add a print** so that **I can sell new items in my store**
  - US502 : Edit / update details for a print
      - As a **site admin** I can **edit / update details for a print** so that **I can change or amend it's title, image, discount setting and other attributes**
  - US503 : Delete a print
      - As a **site admin** I can **delete a print** so that **I can remove the print for sale**
  - US504 : Edit / update details for a print size option
      - As a **site admin** I can **edit / update details for a print size option** so that **I can change or amend it's price or dimensions**
  - US505 : Add an artist bio
      - As a **site admin** I can **add an artist bio** so that **I can give the site users background information on the artist**
  - US506 : Edit / update details for an artist bio
      - As a **site admin** I can **edit / update details for an artist bio** so that **I can change or amend biographical details for the artist**
  - US507 : Delete artist bio
      - As a **site admin** I can **delete an artist** so that **I can remove the artist from the database**


  </details>

* EPIC 06 : SEO and Web Marketing
  <details>
      <summary>User Stories for EPIC01: </summary>

  - US601 : Subscribe to newsletter
      - As a **site user** I can **subscribe to the company newsletter** so that **I can keep up with company news and offers**
  - US602 : View company facebook page
      - As a **site user** I can **find the company on facebook** so that **I can keep up to date with company posts**
  - US603 : SEO
      - As a **site user** I can **find the site through web searches** so that **I can easily access the site**
  - US604 : View privacy policy
      - As a **site user** I can **view the company privacy policy** so that **I can see the company is GDPR compliant**

  </details>


## Features

make notes here to say that many of the features are based on the walkthrough and some such as profile, and allauth are largely unchanged.  Others have been added to or customized for this project and ?? should the features list focus on the differences ?  or highlight them in some way ????
bag.html needs work to make it responsive
need to check out the pass reqs re business type
the confirm on the delete of print and artist is very basic
talk about filled in user icon when logged in, my home link on mobile menu, carousel, new arrivals, discounts
search checks for artist name and title
artist bio
admin for artist, print and printoption
summernote
dateselect widget
username shown on screen - limited to 12 chars
likes (login required - this code is already there)
subscribe list and facebook page
privacy policy
fb

### Existing Features

- include SEO stuff and privacy policy info here.
- discounts to be handled with boolean
- new arrivals to be handled using added on date within a 3 month range

-   __F01 to be written__
    
    To be written  
    
    ![?????](documentation/supp-images/)
    

-   __How these features support the user stories__
    
    The User Stories in the [User Experience (UX)](#user-experience-ux) part of this document are numbered 1 to ?????.  The existing features are listed above as F01 to ?????.  Below is a traceability matrix cross-referencing the user stories with the features, illustrating which features support which stories :
        
    ![User Story Feature Matrix](documentation/supp-images/traceability-matrix.png)


### Features which could be implemented in the future

-   __to be written__
    
    to be written

## Design

-   ### Wireframes

    The wireframe diagrams below describe the ??????? pages.  

    <details>
    <summary>Desktop Wireframes</summary>

    ![Desktop Wireframes](documentation/wireframes/desktop.png)
    </details>
    <details>
    <summary>Tablet Wireframes</summary>

    ![Tablet Wireframes](documentation/wireframes/ipad.png)
    </details>
    <details>
    <summary>Smartphone Wireframes</summary>

    ![Smartphone Wireframes](documentation/wireframes/smartphone.png)
    </details>

-   ### Entity-Relationship diagrams for DBMS
    
      Notes on the ER diagrams :  - to be written ?????  leave this here as it may be useful

      - The ER diagrams provided show the logical data model.  The many-to-many relationship between hikes and their 'likes' is represented as normalized tables to clarify the relationship.  In the models.py file the 'likes' data item is declared as part of the Hike class, with django handling how this relationship is represented in the physical database tables in the background.

      - The Users table in the ER diagrams is also a logical representation of the data captured during user registration and how it relates to the application data model.  The Users table itself is not declared in the models.py file, but is handled by the django modules and this logical view does not reflect all columns and constraints etc. used by the physical data tables in the database.

      - The data model tables are split into two diagrams so that the relationships between the tables can be easily read.

      - A booking is a many-to-many relationship between Schedule and Users but because it also has its own data - places_reserved, it is declared in its own separate class in models.py

      - Because there could be multiple guided hikes on the same hike trail in a single day, the schedule table needs a composite primary key of the hike_id and 'starts' column.  This is handled using a constraint in models.py.

    <details>
    <summary>ER Diagrams - ??????</summary>

    ![ER Diagrams1](documentation/entity-relationship-diagrams/??????)
    </details>

## Planning

A GitHub Project with linked Issues was used as the Agile tool for this project.  User Stories with acceptance criteria were defined using GitHub Issues and development of code for these stories was managed using a Kanban board.  All of the User Stories were linked to 'parent' Epic issues to show how they all supported the over-arching goals of the project.  The acceptance criteria were tested as each story moved to 'Done' and were also included in the final pre-submission manual testing documented in the Testing section of this README.

The Epic, User Stories and Kanban board can be accessed here : [Iomha Print Agile Tool](https://github.com/elainebroche-dev/pf5-iomha-prints/projects/1)


## Technologies Used

### Languages Used 

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://jquery.com/) ??????????????????????
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used  

-   [Google Fonts:](https://fonts.google.com/) used for the Lato and Old Standard TT fonts.
-   [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the project code after being pushed from Git. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking them on a Kanban board.
-   [Django](https://www.djangoproject.com/) was used as the framework to support rapid and secure development of the application.
-   [Bootstrap](https://getbootstrap.com/) was used to build responsive web pages
-   [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) used for account registration and authentication (version 0.41.0 installed because of project dependencies).
-   [Pillow](https://pillow.readthedocs.io/en/stable/index.html) - Python Imaging Library used for image handling
-   [jquery library](https://code.jquery.com/jquery-3.4.1.min.js) - for various pieces of functionality including adding and removing items from the shopping cart and handling the increment and decrement of the quantity control.
-   [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to simplify form rendering.
-   [Stripe](https://js.stripe.com/v3/) used for secure payments (referenced in base.html).
-   [Stripe install library](https://pypi.org/project/stripe/) used for secure payments.
-   [Django Countries](https://pypi.org/project/django-countries/) used on checkout page to pass valid country code to Stripe.
-   [Summernote](https://pypi.org/project/django-summernote/) used to provide WYSIWYG editing on the Artist Bio editing screen.
-   [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku.
-   [dj_database_url](https://pypi.org/project/dj-database-url/) library used to allow database urls to connect to the postgres db.
-   [psycopg2](https://pypi.org/project/psycopg2/) database adapter used to support the connection to the postgres db.
-   [Amazon S3](https://aws.amazon.com/s3/) used to store static files and images.
-   [Boto3](https://pypi.org/project/boto3/) the Amazon Web Services (AWS) Software Development Kit (SDK) for Python.
-   [django_storages](https://django-storages.readthedocs.io/en/latest/) used to connect django to S3.
-   [Heroku](https://www.heroku.com) - used to host the deployed application.
-   [Heroku Postgres](https://www.heroku.com/postgres) - SQL database service provided by Heroku used to store models and data.
-   [dbdiagram.io](https://dbdiagram.io/home) was used to create the Entity Relationship diagrams for the application data model
-   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes during the design process.


## Testing

### Validator Testing 

- python warning : Unused variable field_name in artists/forms.py - code is formatted this way so that the field variable
binds the actual field and not just a string representing it's name.

- [HTML Validator](https://validator.w3.org/)

    - As this project uses Django templates the html has been validated by manually clicking through the application pages, copying the source of the rendered pages and then validating this version of the html using the W3C Validator (link shown above). 

    - results for index.html
      - <details>
        <summary>Index Page - Summary</summary>

        ![Index Page - Summary](documentation/testing/validation/???????)
      </details>

      - <a href="?????" target="_blank">Index Page - Full HTML Validation Results</a>


- [CSS Validator](https://jigsaw.w3.org/css-validator/)

    - <details>
      <summary>?????? validation results</summary>

      ![style.css](documentation/testing/validation/?)
      </details>

    - <a href="???" target="_blank">CSS Validation - Full Results</a> 


- [Javascript Validator](https://jshint.com/)

  <details>
    <summary>??????.js validation results</summary>

    ![Script JS](documentation/testing/validation/??????)
  </details>

- [Python Validator](http://pep8online.com/)

  <details>
    <summary>?????? validation results</summary>

    ![Project urls.py](documentation/testing/validation/??????????)
  </details>

### Automated Testing - to be written - may not need this

### Browser Compatibility

- Chrome DevTools was used to test the responsiveness of the application on different screen sizes.  In addition, testing has been carried out on the following browsers :
    - to be written
 
### Manual Testing Test Cases and Results - to be written

- The link below details the test cases that were used, the results, and a cross-reference to the Feature ID that each test case exercised (click link to open pdf).  The test cases are primarily based on the User Story acceptance criteria that were used to test iterations of the code during development.
  
  - <a href="?????" target="_blank">Manual Testing - Test Cases and Results</a>

### Known bugs

- To be written

## Deployment  - leaving this here for now but all needs to be rewritten

Detailed below are instructions on how to clone this project repository and the steps to configure and deploy the application.  Code Institute also provides a summary of similar process steps here : [CI Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

1. How to Clone the Repository
2. Create Application and Postgres DB on Heroku
3. Configure Cloudinary to host images used by the application
4. Connect the Heroku app to the GitHub repository
5. Executing automated tests
6. Final Deployment steps

### How to Clone the Repository 

- Go to the https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes repository on GitHub 
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there
- Open a GitBash terminal and navigate to the directory where you want to locate the clone
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process
- To install the packages required by the application use the command : pip install -r requirements.txt
- When developing and running the application locally set DEBUG=True in the settings.py file
- Changes made to the local clone can be pushed back to the repository using the following commands :

  - git add *filenames*  (or "." to add all changed files)
  - git commit -m *"text message describing changes"*
  - git push

- N.B. Any changes pushed to the master branch will take effect on the live project once the application is re-deployed from Heroku

### Create Application and Postgres DB on Heroku
- Log in to Heroku at https://heroku.com - create an account if needed.
- From the Heroku dashboard, click the Create new app button.  For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
- On the Create New App page, enter a unique name for the application and select region.  Then click Create app.
- On the Application Configuration page for the new app, click on the Resources tab.
- In the Add-ons search bar enter "Postgres" and select "Heroku Postgres" from the list - click the "Submit Order Form" button on the pop-up dialog.
- Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - check the DATABASE_URL has been automatically set up. 
- Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.
- Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
- The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

  - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

  - SECRET_KEY = os.environ.get('SECRET_KEY')

- In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate 
- Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command : pip3 freeze --local > requirements.txt
- Commit and push any local changes to GitHub.
- In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py

### Configure Cloudinary to host images used by the application
- Log in to Cloudinary - create an account if needed.  To create the account provide your name, email and set up a password.  For "primary interest" you can choose "Programmable Media for image and video API".  Click "Create Account" and you will be sent an email to verify your account and bring you to the dashboard.
- From the dashboard, copy the "API Environment variable" value by clicking on the "Copy to clipboard" link.
- Log in to Heroku and go to the Application Configuration page for the application.  Click on Settings and click on the "Reveal Config Vars" button.
- Add a new Config Var called CLOUDINARY_URL and assign it the value copied from the Cloudinary dashboard, but remove the "CLOUDINARY_URL=" at the beginning of the string. 
- In order to be able to run the application on localhost, also add the CLOUDINARY_URL environment variable and value to env.py

### Connect the Heroku app to the GitHub repository
- Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
- Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is (https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes) and click on Connect to link up the Heroku app to the GitHub repository code.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
- The application can be run from the Application Configuration page by clicking on the Open App button.
- The live link for this project is (https://pf4-wayfarers.herokuapp.com/)

### Executing automated tests
- The existing automated jquery/javascript test can be executed using jest as follows :
  - If jest is not installed then run the command : npm install --save-dev jest
  - Run the js test file using the command : npm test

- The existing automated django/python tests are executed using unittest as follows :
  - Run the python tests using the command : python3 manage.py test
  - To run just a subset of the tests, then append the application and test file name to the command, e.g. : python3 manage.py test hikebooker.test_models

- Test coverage for the django/python tests can be reviewed using the coverage tool :
  - If coverage is not installed then run the command : pip3 install coverage
  - Execute the following series of commands to determine test coverage :
    - coverage run --source=hikebooker manage.py test
    - coverage report
    - coverage html
    - python3 -m http.server  (detailed results can be viewed via the browser in the htmlcov directory)


### Final Deployment steps
Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows :
- Set DEBUG flag to False in settings.py
- Ensure this line exists in settings.py to make summernote work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'
- Ensure requirements.txt is up to date using the command : pip3 freeze --local > requirements.txt
- Push files to GitHub
- In the Heroku Config Vars for the application delete this environment variable :  DISABLE_COLLECTSTATIC
- On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch

#### The live link to the application can be found here - [P5 Iomha Prints](https://pf5-iomha-prints.herokuapp.com/) 


## Credits 

### Code 
- Much of the coding and testing relies heavily on information in the "Boutique Ado" walkthrough in the Code Institue Building an E-Commerce Platform module. 
- Some elements of the coding, such as the "like" functionality to add items to a wishlist are based on the "I Think Therefore I Blog" walkthrough in the Code Institute Full Stack Frameworks module.
- Code to implement a bootstrap carousel was based on information found here : [W3 Schools Bootstrap Carousel](https://www.w3schools.com/bootstrap4/bootstrap_carousel.asp)
- Code to make the carousel responsive was based on information found here : [Responsive Carousel](https://stackoverflow.com/questions/19582340/make-bootstraps-carousel-both-center-and-responsive)
- Code to handle images and avoid distortion was based on information found here : [Image Scaling](https://stackoverflow.com/questions/5369301/css-image-scaling-to-fit-within-area-not-distort)
- Code to set max-width for website was based on information found here : [Max Width Screen](https://stackoverflow.com/questions/9730263/setting-max-width-for-body-using-bootstrap)
- Code on to use calc() in css was based on information found here : [CSS Tricks](https://css-tricks.com/a-complete-guide-to-calc-in-css/)
- Information on how to use command line sql to deduct 6 months from automatic date was based on an example found here : [SQL Date](https://stackoverflow.com/questions/21309204/how-to-add-time-to-a-datetime-in-sqlite)
- Code to filter new arrivals was based on information found here : [Date Filter](https://stackoverflow.com/questions/1984047/django-filter-older-than-days)
- CSS to centre the back-to-top button was based on information found here : [CSS Center](https://stackoverflow.com/questions/2005954/center-a-positionfixed-element)
- Code to extract the first word from a string was based on information found here : [Python split](https://www.kite.com/python/answers/how-to-get-the-first-word-in-a-string-in-python)
- Code to take the first 2 chars of the print dimensions in django template was based on information found here : [Django Template Slice](https://stackoverflow.com/questions/17596141/django-slice-string-in-template)
- Code to create foreign key to model in another app was based on information found here : [Reference Model in another app](https://www.py4u.net/discuss/160247)
- Code to use summernote in a django form was based on information found here : [Integrating Summernote](https://djangocentral.com/integrating-summernote-in-django/)
- Code to place the widgets.py in the project folder so it can be shared : [Import Widget](https://stackoverflow.com/questions/60095510/how-do-i-include-a-built-in-django-widget-template-in-my-custom-widget-template)
- Code to set year range in SelectDateWidget was found here : [SelectDateWidget Years](https://stackoverflow.com/questions/12187671/how-to-change-year-options-of-djangos-selectdatewidget)
- Code to list the years range in SelectDateWidget from highest to lowest was found here : [Desc Year](https://www.generacodice.com/en/articolo/1166815/django-selectdatewidget-years-in-reverse)
- Code to use SummernoteInPlaceWidget was found here : [InplaceWidget](https://github.com/summernote/django-summernote/issues/303)
- Code to manipulate django querysets was based on information found here : [Django Querysets](https://docs.djangoproject.com/en/3.2/ref/models/querysets/)
- Code to invoke template on select control change was based on information found here : [Location href](https://stackoverflow.com/questions/15341285/how-do-i-call-a-django-function-on-button-click) and here : [Build URL](https://stackoverflow.com/questions/37311042/call-django-urls-inside-javascript-on-click-event)

### Content 
- The website page layout look and feel were influenced by [Dunnes Stores Website](https://www.dunnesstores.com/), [Desenio](https://desenio.ie/) and [Art Prints](https://artprints.ie/)
- The artist names are fictional and were generated using this website [Name Generator](https://www.random-name-generator.com/)
- The artist bios are ficitonal and images for them were generated using this website [This Person Does Not Exist](https://thispersondoesnotexist.com/)

### Media 
- The Old Standard TT and Lato fonts used were imported from [Google Fonts](https://fonts.google.com/)
- Fontawesome was used for all icons, including icons for wishlist, user, print category, social media etc. - [Font Awesome](https://fontawesome.com/)
- The application favicon was created from the images icon on [Font Awesome](https://fontawesome.com/) and created using information found here : [Icon as Favicon](https://stackoverflow.com/questions/18156240/use-font-awesome-icon-as-favicon) and [Favicon Generator](https://gauger.io/fonticon/)
- The images used for the art prints were taken from [Negative Space](https://negativespace.co/) and [Unsplash](https://unsplash.com/). 

    <details>
      <summary>Links to the images and original artist names can be found here :</summary>
     
  - Artist : Alex Wong - [Image](https://unsplash.com/photos/l5Tzv1alcps)
  - Artist : Bernard Spragg - [Image](https://negativespace.co/snowy-mountain-highway/)
  - Artist : Bernard Spragg - [Image](https://negativespace.co/colorful-buildings-abstract/)
  - Artist : Birch Landing - [Image](https://negativespace.co/shimmering-red-glitter/)
  - Artist : Bob Richards - [Image](https://negativespace.co/rusted-metal-texture-background/)
  - Artist : Bob Richards - [Image](https://negativespace.co/leaf-dew-rain/)
  - Artist : Bonnie Moreland - [Image](https://negativespace.co/waterfall-forest-stream-park/)
  - Artist : Bonnie Moreland - [Image](https://negativespace.co/snow-winter-landscape-trees/)
  - Artist : Bonnie Moreland - [Image](https://negativespace.co/lone-tree-fog/)
  - Artist : Bonnie Moreland - [Image](https://negativespace.co/old-barn-farm-stormy/)
  - Artist : Bonnie Moreland - [Image](https://negativespace.co/trees-winter/)
  - Artist : Burst - [Image](https://negativespace.co/soap-bubbles-macro/)
  - Artist : Burst - [Image](https://negativespace.co/abstract-lights-on-a-frozen-surface/)
  - Artist : Burst - [Image](https://negativespace.co/geometric-glass-building/)
  - Artist : Candace McDaniel - [Image](https://negativespace.co/bridge-abstract-city-monochrome/)
  - Artist : Candace McDaniel - [Image](https://negativespace.co/brooklyn-bridge-landmark/)
  - Artist : Claudio Testa - [Image](https://unsplash.com/photos/iqeG5xA96M4)
  - Artist : Dan Freeman - [Image](https://unsplash.com/photos/WHPsxhB4mWQ)
  - Artist : Free Nature - [Image](https://negativespace.co/blue-night-sky-clouds/)
  - Artist : Javier Diaz - [Image](https://negativespace.co/purple-white-dandellion-flower/)
  - Artist : JJ Skys the Limit - [Image](https://negativespace.co/autumn-mountain-valley/)
  - Artist : Joe deSousa - [Image](https://negativespace.co/eiffel-tower-closeup/)
  - Artist : Joe deSousa - [Image](https://negativespace.co/white-flower-background/)
  - Artist : Juskteez Vu - [Image](https://negativespace.co/stars-trail-sky-night-universe/)
  - Artist : Kelly Ishmael - [Image](https://negativespace.co/water-leaf-macro/)
  - Artist : Kumiko Shimizu - [Image](https://unsplash.com/photos/Pxa0yJ2Elxc)
  - Artist : Lukasz Szmigiel - [Image](https://unsplash.com/photos/jFCViYFYcus)
  - Artist : Matt Bango - [Image](https://negativespace.co/tree-stump-background/)
  - Artist : Matt Bango - [Image](https://negativespace.co/moon-surface/)
  - Artist : Matthew Henry - [Image](https://negativespace.co/ink-trail-water-pink/)
  - Artist : Mike Moloney - [Image](https://negativespace.co/beach-sand-waves-day/)
  - Artist : Nathalie E. Julien - [Image](https://negativespace.co/water-lotus-pond-bloom/)
  - Artist : Natures Buddy - [Image](https://negativespace.co/macro-flower-blossom/)
  - Artist : Pawel Czerwinski - [Image](https://unsplash.com/photos/ruJm3dBXCqw)
  - Artist : Robert V. Ruggiero - [Image](https://unsplash.com/photos/hLvK16XVUqs)
  - Artist : Silvestri Matteo - [Image](https://unsplash.com/photos/6-C0VRsagUw)
  - Artist : Stephen Rahn - [Image](https://negativespace.co/night-starry-sky-galaxy/)
  - Artist : Stephen Rahn - [Image](https://negativespace.co/nebula-with-stars/)
  - Artist : Stephen Rahn - [Image](https://negativespace.co/moon-night-sky-dark/)
  - Artist : Stephen Rahn - [Image](https://negativespace.co/night-stars/)
  - Artist : Stephen Rahn - [Image](https://negativespace.co/moon-surface-craters-background/)
  - Artist : Stephen Rahn - [Image](https://negativespace.co/star-trails/)
  - Artist : Travel Photographer - [Image](https://negativespace.co/bokeh-lights-background/)
  - Artist : Travel Photographer - [Image](https://negativespace.co/spiral-staircase-architecture/)
  - Artist : Travel Photographer - [Image](https://negativespace.co/flower-rain-drops/)
  - Artist : Vidsplay - [Image](https://negativespace.co/abstract-design-background/)
  - Artist : Vidsplay - [Image](https://negativespace.co/colorful-abstract-design/)
  - Artist : Vidsplay - [Image](https://negativespace.co/abstract-flowing-laser-light/)
  - Artist : Vidsplay - [Image](https://negativespace.co/abstract-geometric-background/)
  - Artist : Viktor Jakovlev - [Image](https://unsplash.com/photos/H0vuplqoX0c)
  - Artist : Wyncliffe - [Image](https://negativespace.co/ocean-sunset-water/)
  - Artist : Wyncliffe - [Image](https://negativespace.co/ocean-beach-rocks/)
    </details>

  
### Acknowledgments

- Thank you to my mentor Brian Macharia for all of his guidance, help and feedback throughout each project on this course. 