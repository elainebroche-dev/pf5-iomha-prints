<h1 align="center">Íomhá Prints - Order Prints Online</h1>

[View the live project here](https://pf5-iomha-prints.herokuapp.com/)

The Íomhá Prints project is a B2C e-commerce application which sells art prints directly to end users.  It is implemented as a retail store where users can view, search and filter the products on offer, then select items to add to their shopping cart and purchase through a simple single payment.

General users can view details of the prints available for purchase including bio information on the print artist, and can sign up to the company newletter. In addition, registered users can create a wishlist of prints they may be interested in and a profile to keep track of delivery details and order history.

Admin users can manage the lists of prints and artists, this includes being able to add new prints to the range, update pricing, link artists to prints, update artist bio information.  A full description of the available functionality is included in this document.

The Web Marketing strategies used by the project are :
- Organic Social - through facebook
- Email - through a newletter subscription managed via Mailchimp

The structure and purpose of the Íomhá Prints project is based on the Code Institute Boutique Ado walkthrough example application.

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

### Existing Features

Below are descriptions of the main features of the application.  Many of the features are based on the Boutique Ado walkthrough project and SEO and Web Marketing modules of the course.  

The Íomhá Prints application uses a B2C e-commerce model, selling directly to end customers with single online payments to cover purchases.

- UX Related Features

    -   __F01 - Consistent page look and feel__
        
        The page layout, navigation bar, header, footer, colours and fonts have a consistent look and feel on all pages of the website to give the user an intuitive easy to use experience.  The navigation bar is responsive on multiple screen sizes - on smaller screens it coverts to a 'burger' menu style. 
        
        ![F01 Large Screen](documentation/supp-images/f01-large-screen.png)

        ![F01 Small Screen](documentation/supp-images/f01-small-screen.png)

    -   __F02 - User logged in indicator__
        
        The user can easily see if they are logged in from the user icon at the top right of the screen.  If not logged in the user icon appears as an outline and has the text "Account" underneath, if logged in, the user icon is filled in and the user's username (max 12 chars) appears under the icon.  
        
        ![F02 Logged Out](documentation/supp-images/f02-logged-out.png)

        ![F02 Logged In](documentation/supp-images/f02-logged-in.png)


    -   __F03 - Home Page__
        
        The application home page includes an eye-catching carousel which displays a sample of the prints available for purchase on the site.  It also gives introductory content to clearly brief the user on the purpose of site and goal of of the company.  
        
        ![F03 Home Page](documentation/supp-images/f03-home-page.png)


    -   __F04 - View Prints__
        
        The user can easily scroll through the list of prints available for purchase on the site by using the All Prints option in the navigation bar at the top of the screen. The list presented will show an image of the print and some details including title, category, number of likes and rating. A back-to-top button allows the user to quickly navigate back to the top of the screen.
        
        ![F04](documentation/supp-images/f04-list-of-prints.png)


    -   __F05 - Filter and Search options__
        
        There are options available to the user on the navigation bar to filter the list of prints and allow them to restrict the results to items they are particularly interested in.  For example, the user can choose to just see prints for a particular category, or just new arrivals (added within the last 6 months) or just discounted prints.  The user can also restrict the list of results based on a search term which will attempt to find matches in the print titles and artist names.

        The number of matching results is shown on screen and results can be ordered by rating, category, or title.
        
        ![F05](documentation/supp-images/f05-list-of-prints.png)

    -   __F06 - View Print Details__
        
        By clicking on a print the user can access the Print Details page which will display the image, category, rating, number of likes, artist name, print options (size and price) and from here they can select the size and quantity of print they want and add them to their cart.  
        
        ![F06](documentation/supp-images/f06-print-detail.png)

    -   __F07 - View Artist Details__
        
        From the Print Detail page (F06 above) the user can click on the artist name and view a short bio of the artist associated with the print and learn a bit about their background and work.  
        
        ![F07](documentation/supp-images/f07-artist-detail.png)


    -   __F08 - Likes and Wishlist__
        
        If the user is logged in when they visit a Print Detail page (F06 above) they will have the opportunity to 'like' the print.  Clicking on the 'heart' icon will toggle the like/unlike setting for that user for that print.  Liking a print will add that print to the user's wishlist.  The wishlist option is available from the navigation bar - but is only visible when the user is logged in.  Adding items to their withlist enables the user to save items for purchase later.   
        
        ![F08](documentation/supp-images/f08-likes.png)

        ![F08](documentation/supp-images/f08-wishlist.png)

    -   __F09 - Custom HTTP 404 and 500 response pages__
        
        To help support a consistent user-experience and handle unexpected events in a user-friendly manner, custom pages are displayed for any unexpected 404 or 500 HTTP response codes.  
        
        ![F09 404 Response](documentation/supp-images/f09-404-response.png)

        ![F09 500 Response](documentation/supp-images/f09-500-response.png)

    -   __F10 - On-screen messages__
        
        Pop-up on-screen messages are used to let the user know the effects of their interactions with the application.  Events such as changing the contents of the shopping cart, submitting an order, logging in or out will result in a message appearing on screen to inform the user of what has happened, and if appropriate, give them an update on the contents of the shopping cart.
        
        ![F10](documentation/supp-images/f10-toast-example-1.png)

        ![F10](documentation/supp-images/f10-toast-example-2.png)
    
    
- Authentication and Role-based Authorisation Related Features

    -   __F11 - Registration, Login, Logout__
        
        Users can register (sign-up) with the site, login (sign-in) and logout (sign-out).  Some features such as the wishlist are only available to logged in users (see F12 below for information on role based interactions).  When registering, users are asked to confirm their email addresses in order to activate the account.
        
        ![F11 Register](documentation/supp-images/f11-register.png)
        
        ![F11 Login](documentation/supp-images/f11-login.png)
                      
        ![F11 Logout](documentation/supp-images/f11-logout.png)

    -   __F12 - Role based interactions__
        
        Certain functionality within the application is role based.  For example, in order to 'like' a print and add it to their wishlist or save profile information, a user needs to be logged in.

        In addition, data managment tasks such as adding prints or artist information to the website, or changing pricing, are actions which can only be performed by a logged in admin (superuser).  
        
        ![F12 Profile](documentation/supp-images/f12-profile.png)

        ![F12 Management](documentation/supp-images/f12-print-management.png)

    -   __F13 - User Profile__
        
        If logged/signed in a user can opt to save their delivery address and/or birthday in their profile.  The My Profile page can be accessed via clicking the user icon.   If delivery details have been stored for a user then their details are automatically pre-populated on the checkout page making it quicker and easier for them to checkout.  The profile information can easily be changed simply overwritting the pre-populated values and opting to save this new information on submission of the order, or they can be updated directly via the My Profile page. 

        By giving the user the option of storing their date of birth, this allows the company to track additional information about the user than could be used in marketing - for example offering a special discount on their birthday to encourage them to purchase.
        
        ![f13](documentation/supp-images/f13-profile-page.png)

- E-Commerce Related Features
    (???? mention B2C here)

    -   __F14 - Shopping Cart__
        
        To be written  
        
        ![?????](documentation/supp-images/)
    
    -   __F15 - Secure Payments__
        
        To be written  
        
        ![?????](documentation/supp-images/)

    -   __F16 - Order Confirmation and Order History__
        
        To be written  
        
        ![?????](documentation/supp-images/)
 

- Data Administration Related Features

    -   __F17 - Print Management__
        
        To be written  
        
        ![?????](documentation/supp-images/)
    
    -   __F18 - Print Option Management__
        
        To be written  
        
        ![?????](documentation/supp-images/)

    -   __F19 - Artist Management__
        
        To be written  
        
        ![?????](documentation/supp-images/)


- SEO, GDPR and Marketing Related Features
    - SEO (include sitemap and robotls mentions here) - talk about how keywords where determined and where they were used
    - Subscribe to Newsletter
    - Facebook
    - Privacy Policy

    -   __F20 - SEO__
        
        To be written  
        
        ![?????](documentation/supp-images/)
    
    -   __F21 - Subscribe to Newletter__
        
        To be written  
        
        ![?????](documentation/supp-images/)

    -   __F22 - Facebook__
        
        To be written  
        
        ![?????](documentation/supp-images/)

    -   __F23 - Privacy Policy__
        
        To be written  
        
        ![?????](documentation/supp-images/)

-   __How these features support the user stories__
    
    The User Stories in the [User Experience (UX)](#user-experience-ux) part of this document are numbered 1 to ?????.  The existing features are listed above as F01 to ?????.  Below is a traceability matrix cross-referencing the user stories with the features, illustrating which features support which stories :
        
    ![User Story Feature Matrix](documentation/supp-images/traceability-matrix.png)


### Features which could be implemented in the future

-   __to be written__
    
    DOB captured
    improve on the delete comfirmation message
    Improved datepicker for artist mgt and user dob
    reviews and testimonials - could feed into ratings

## Design

-   ### Wireframes

    The wireframe diagrams below describe the application web pages.  

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


-   ### Entity-Relationship diagram for DBMS
    
      Notes on the ER diagram : 

      - The ER diagram provided shows the logical data model.  The many-to-many relationship between prints and their 'likes' is represented as normalized tables to clarify the relationship.  In the products models file the 'likes' data item is declared as part of the Print class, with django handling how this relationship is represented in the physical database tables in the background.

      - The User table in the ER diagram is also a logical representation of the data captured during user registration and how it relates to the application data model.  The User table itself is handled by the django modules and this logical view does not reflect all columns and constraints etc. used by the physical data tables in the database.

      - Like the application itself, the data models rely heavily on the models used in the Code Institute Boutique Ado example application.  The Order and OrderLineItem tables are almost a direct match of the ones using in Boutique Ado, the only customizations being the foreign key of product is linked to the Print table instead of a Product table, and a column to store item_dimensions.

      - The UserProfile table/model is also largely based on the one used in the Boutique Ado application, it has been customized by adding a DOB column so that the Customer's date of birth can be optionally captured and potentially used for birthday offers and promotions.

      - The Print table replaces the Boutique Ado Product table and has been customized heavily to reflect the information stored for this application.  In addition to a relationship with the OrderLineItem table, the Print table links to a new table for Artist data and a Category table that is similar to the one used by Boutique Ado.

      - The PrintOption table is a new table that is used to store size and price options applicable to all print stock.  Like the PrintOption table, dimension data and price are also stored in the OrderLineItem table however there is no declared relationship between those data items and the dimesion and price data in the PrintOption table as the data in OrderLineItem records reflect a snapshot in time when a purchase was made whereas these items in the PrintOption table represent the current up-to-date values that are valid for new purchases.


    <details>
    <summary>ER Diagram</summary>

    ![ER Diagrams1](documentation/entity-relationship-diagrams/er-diagram.png)
    </details>

## Planning

A GitHub Project with linked Issues was used as the Agile tool for this project.  User Stories with acceptance criteria were defined using GitHub Issues and development of code for these stories was managed using a Kanban board.  All of the User Stories were linked to 'parent' Epic issues to show how they all supported the over-arching goals of the project.  The acceptance criteria were tested as each story moved to 'Done' and were also included in the final pre-submission manual testing documented in the Testing section of this README.

The Epic, User Stories and Kanban board can be accessed here : [Iomha Print Agile Tool](https://github.com/elainebroche-dev/pf5-iomha-prints/projects/1)


## Technologies Used

### Languages Used 

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://jquery.com/) 
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

 
### Manual Testing Test Cases and Results 

- The link below details the test cases that were used, the results, and a cross-reference to the Feature ID that each test case exercised (click link to open pdf).  The test cases are primarily based on the User Story acceptance criteria that were used to test iterations of the code during development.
  
  - <a href="?????" target="_blank">Manual Testing - Test Cases and Results</a>

### Known bugs

- To be written

## Deployment  - leaving this here for now but all needs to be rewritten

Detailed below are instructions on how to clone this project repository and the steps to configure and deploy the application.  Code Institute also provides a summary of similar process steps here : [CI Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

1. How to Clone the Repository
2. Create Application and Postgres DB on Heroku
3. Connect the Heroku app to the GitHub repository 

4. Configure Amazon Web Services S3 to store static files and images
5. Configure STRIPE config vars and webhooks

### How to Clone the Repository 

- Go to the https://github.com/elainebroche-dev/pf5-iomha-prints repository on GitHub 
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
- N.B. Be careful not to upload DEBUG=True in the settings.py file to GitHub - this setting should only be used locally.

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
- Set up and admin user in the postgres db using the command : python3 manage.py createsuperuser
- Set DEBUG flag to False in settings.py
- Commit and push any local changes to GitHub.
- In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py

### Connect the Heroku app to the GitHub repository
- Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
- Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is (https://github.com/elainebroche-dev/pf5-iomha-prints) and click on Connect to link up the Heroku app to the GitHub repository code.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
- The application can be run from the Application Configuration page by clicking on the Open App button.
- The live link for this project is (https://pf5-iomha-prints.herokuapp.com/)

### Configure Amazon Web Services S3 to store static files and images
- Log on to AWS account on aws.amazon.com - create an account if necessary
- From the dashboard access the S3 services
- Create a new 'bucket', it is recommended to give this a name similar to your application to make it easy to remember and use, choose a region close to you, uncheck "Block all public access" and acknowledge that the bucket will be public.  Next, click on the new bucket to configure it.
- Go to the properties tab and turn on static website hosting, fill in default values for index and error document settings - e.g. index.html and error.html and click on Save.
- Go to the permissions tab and make 3 changes to configure the bucket :

    - Step 1 Configure CORS : 
        - Paste the following CORS configuration string :
    	[
            {
                "AllowedHeaders": [
                    "Authorization"
                ],
                "AllowedMethods": [
                    "GET"
                ],
                "AllowedOrigins": [
                    "*"
                ],
                "ExposeHeaders": []
            }
        ]

    - Step 2 Generate Policy:
        - Go to the bucket policy area, click on Edit and click on policy generator.  
        - Choose S3 bucket policy from drop-down
	    - Put asterisk in Principal field
	    - Select get object from Actions drop-down
	    - Copy ARN and paste into ARN box on the policy generator page
	    - Click Add Statement
	    - Click Generate Policy then copy the policy into the policy editor window
        - Add /* to the end of the Resource key
	    - Click Save

    - Step 3 ACL :
        - Go to the Access Control List area
		- Set the list objects permission for everyone under the Public Access section and
		check the box to confirm you want this permission setting

- Create a user to access the bucket through IAM as follows :
    - Return to the services menu on the dashboard and access the IAM area
    - Create a group
    - On the same page click on Policies, then Create Policy, go to JSON table and select Import Managed Policy
    - Click on Import managed policy on rhs
	- Search for S3 and select AmazonS3FullAccess and click on Import
	- Go back and get the Bucket Policy ARN (generated when bucket was created)
	- Change the Resource value from * to ARN bucket and it's contents - e.g :
        "Resource": [
                    "arn:aws:s3:::pf5-iomha-prints",  (sensitive)
                    "arn:aws:s3:::pf5-iomha-prints/*"
                ]
	- Click Next and then Review Policy
	- Give the policy a name and click Create Policy
    - Attach the policy to the group you created as follows : Go to groups, click on your group, go to the Permissions tab, click Add permissions and select Attach policies, select the policy created on previous step and click Attach permissions
    - Create user to put into the group. Click Users on lhs, click Add User, assign name check the programmatic access checkbox, click on Next:Permissions.  Add user to group, click through to the end and click Create User.

- Download and save the generated csv which contains the users access and secret access keys
- Update the AWS section of the settings.py file - replace the bucket name and region with the values you set up in the previous steps :

			if 'USE_AWS' in os.environ:
				# Bucket Config
				AWS_STORAGE_BUCKET_NAME = 'pf5-iomha-prints'    <------ bucket name and region
				AWS_S3_REGION_NAME = 'eu-west-1'
				AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
				AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

- Add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY config vars to heroku using the values from the downloaded cvs
- Add USE_AWS = True to the Heroku config vars
- Remove the DISABLE_COLLECTSTATIC config var at this point from Heroku
- The custom_storages.py file that is part of this project will tell Django to use S3 to store static and media files when collectstatic is run
- The remaining AWS configuration settings needed are already configured in this projects settings.py file
- Go to the S3 dashboard and create a folder called media in the new bucket.  Specify grant public-read access on the folder and tick the checkbox to confirm.

### Configure STRIPE config vars and webhooks
- Log in to your Stripe account - create one if necessary
- Add STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY to the Heroku config vars, assign these variables values from your Stripe account dashboard
- Create a webhook endpoint for use with your applications.  On the stripe dashboard go to the Developers -> Webhooks area, click add endpoint, use the url of your Heroku application with '/checkout/wh/' tagged onto the end of the url string.  When configuring the endpoint, the events to register to listen to are payment_intent_succeeded and payment_intent_failed
- Once the endpoint is set up get the signing secret for the webhooks and save this value as a Heroku config var called STRIPE_WH_SECRET.

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