# Ribble Valley Soap Co.

![home-page](documentation/image-0.png)

## Table of Contents

- [Introduction](#introduction)
- [Design](#design)
- [Features](#features)
- [User Stories](#user-stories)
- [Languages](#languages)
- [Database](#database)
- [Agile Design Principles](#agile-design-principles)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Introduction



## Design



### Color Scheme

I found I color scheme that fitted my theme from [coolors.com](https://coolors.co/dcd6d1-b38656-3e5965-f5f5f5-9b4e46). 

### Font

My font was chosen from [googlefonts](https://fonts.google.com/specimen/Modern+Antiqua) - I chose Modern Antiqua as it fell under the medieval filter on google fonts and this links suitably with the historic feel I initially desired.

### Wireframes

I used the [Balsamiq](https://balsamiq.com/) wireframing tool to design simple mock-ups of my site to give me an initial idea of how the site layout should be.


## Features

### Site Pages

The following examples are screenshots of the various pages on my site.

### Home page

This is where the user first sees the site. All pages on the site consist of a navbar, the main content and a footer. On the home page the title of the company is displayed in the navbar along with a search bar function, a mission page, my account details and a bag icon.

Underneath the navbar is an offer banner that displays on some but not all pages of the site. It informs the user of an offer that they could be eligible for.

In the main section, there is a hero image of a river and over the top is the company name and a tagline informing the user of what the company sells. Underneath this tagline is a link straight to the products page.

At the bottom of the page is a footer, which includes information on the company address, my github details and a link to Facebook and Instagram.

![Landing page](documentation/image-01.png)

### Products Page

This page is accessed by following the link on the landing page. It can also be accessed by logged in users straight from the navbar. This products page displays all products that the site sells, along with searching by name and cost and also by filtering through different categories.

![Products page](documentation/image-02.png)
![Soap Page](documentation/image-03.png)
![Shampoo Bars](documentation/image-04.png)
![Bundles](documentation/image-05.png)
![Back to top](documentation/image-06.png)

This page also includes a 'back to top' button to allow the user to return to the filtering and searching options quickly and effectively.

### Product Page

#### Soaps & Shampoo Bars

The individual product page is dynamic and will change dependent on which product was chosen. I have three categories of products, soaps, shampoo bars and bundles. For the soap and shampoo bars the same product detail page is used. Each product has an image, price, weight, the displayed category, a description, dynamic ingredients and the ability to add these to the bag. Also there is a product gallery feature that the business owner could utilise with more images of the product, where a user clicks on an image and it becomes the main image.

![soap](image.png)
![Shampoo Bar](image-1.png)

#### Bundles
For the bundle the product detail page a different as the bundles consist of a soap and a shampoo bar. The bundles still have a price, weight, description but they also include links to the included items. As the bundles contains multiple items, there is no ingredients section.

![Bundles](image-2.png)

#### Add to bag button
The add to bag button at the bottom of the product page allows users to choose an item and place it it their bag. A user may use the add and minus buttons to increase the number of product they want to purchase. The user is not allowed to manually input a number so they cannot choose a negative number. The max items allowed is 99. When successful at placing an item in the bag a success message is displayed underneath the navbar in the top right hand corner. This toast button includes a link to view the bag. This message disappears after 5 seconds.

![Add to bag](image-3.png)

#### Logic for offer

The offer stated on numerous places informs the user that if they buy 5 products, they will receive a free 'Pendle Moor' soap.

![Banner offer](image-5.png)

The logic for this is handled on the bag page. If there is a total of 5 items in the bag then a Pendle Moor soap will be added along with a success message.
![Free soap](image-6.png)
The free product appears in the bag table and a user is not able to interact with it, they cannot add more items in or input a number in the quantity selector. They can remove it if they so wish though. If the total number of items falls below 5 then the free soap is taken out of the bag and a message informing the user of this is displayed. CHANGE THIS TO A WARNING MESSAGE!


### Bag

This page allows the user to look at, update and delete any product that they have previously selected and put in their bag. The bag is in the form of a clear table, the quantity of the item can be increased or decreased and updated and is reflected in the price.

![Bag](image-4.png)

### Future features

#### Game review 

A page on the site where a user can post their own experience of a board game. This would be akin to Trip Advisor, with a rating system, the ability to post a photo and a text area where the user can offer their opinion.

#### Comprehensive message to business owners function

This would be an area of the site where a user can make board game recommendations, ideas for events/theme nights etc directly to the owner. 

Neither of these features will be included in this deployed version due to time restraints but could be in any future deployments.

## User Stories

All of user stories can be located in the liked GitHub project [here](https://github.com/users/smithphil88/projects/3).

## Languages

Technologies used:

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [Heroku](https://www.heroku.com) used for hosting the deployed site.
- [Gunicorn](https://gunicorn.org/) used for WSGI server.
- [Balsamiq](https://balsamiq.com/) used to design mock-up pages.

## Database

I designed my database using [Lucidchart](https://www.lucidchart.com/pages). I created my Entity Relationship Diagram (ERD) to visualise the relationship between my database models.

![screenshot](documentation/lucidchart.png)

## Agile design principles

### Github Projects

[Github Projects](https://github.com/smithphil88/the_lucky_roll_cafe/projects?query=is%3Aopen) was utilised as an Agile design tool throughout this project. Using the right tags, issues and assignments, it served to promote efficient and effective Agile design principles.

User issues were created and issues and tasks were planned and referred back to over the course of the project using this Kanban Board.

The [MoSCoW](https://en.wikipedia.org/wiki/MoSCoW_method) method was used to assist with the organisation of the project. It helped prioritise certain tasks and leave tasks until the end that were not needed for the scope of this assessement.

![screenshot](documentation/github-project.png)

### Github Issues

[Github Issues](https://github.com/smithphil88/the_lucky_roll_cafe/issues) was used alongside Github Projects. This was how I created my user stories, using a custom template that served my purposes.

[Closed Issues](https://github.com/smithphil88/the_lucky_roll_cafe/issues?q=is%3Aissue%20state%3Aclosed)

![screenshot](documentation/gh-issues-closed.png)

[Open Issues](https://github.com/smithphil88/the_lucky_roll_cafe/issues)

![screenshot](documentation/gh-issues-open.png)

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://the-lucky-roll-b5e404f4335f.herokuapp.com/).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the drop-down menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA) and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars** and set your environment variables.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs to be updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
    - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/smithphil88/the_lucky_roll_cafe) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
    - `git clone https://github.com/smithphil88/the_lucky_roll_cafe`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://github.com/smithphil88/the_lucky_roll_cafe)

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/smithphil88/the_lucky_roll_cafe)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

### Content

| Source | Comments |
| --- | --- |
| [Flexbox Froggy](https://flexboxfroggy.com/) | modern responsive layouts |

### Media & Images

| Source | Location | Type |
| --- | --- | --- |
| [Unsplash](https://unsplash.com/photos/selective-focus-photography-of-chess-pieces-G1yhU1Ej-9A) | see our games modal - chess | image |

### Acknowledgements

- I would like to thank the tutors at Code Institute for helping me throughout the project on various debugging assistance.
- I would like to thank my tutor Julia for her support.
- Thank you to my cohort facilitator Lewis for his guidance.
- And thank you to my partner, Emma, for her complete support and bringing me cups of coffee when they were really needed.