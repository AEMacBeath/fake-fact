# Fake or Fact
Deployed app - [fakefact2022](https://fakefact2022.herokuapp.com/)

## Project Description
Fake | Fact is a blog web applcaition where users are presented with vaiours facts and myths. The user can select wether they think it is fake or fact. Once chosen they are presented with the full post details. If logged in the users can also create and view messages left by other users. 

## Table of Contents _Note: add links to ToC_
-   [Project Description](#project-description)
-   [Build process](docs/planning.md)
-   [Features](#features)
    -   [Common features](#common-features)
    -   [Homepage](#homepage)
    -   [Post detail](#post-detail)
    -   [Account screens](#account-screen)
-   [Testing]{#Testing}
    -   [Validator Testing](#validator-testing)
    -   [Bugs](#bugs)
-   [Technologies Used](#technologies-user)
-   [Credits](#credits)

## Features
### Common features
-   Background image
-   Navigation - [Bootstrap Navbar](https://getbootstrap.com/docs/5.2/components/navbar/)
-   Footer - includes Django pagination buttons

### Homepage
-   Post title cards with Fake and Fact buttons - [Bootrap Cards](https://getbootstrap.com/docs/5.2/components/card/)


### Post Detail
-   Post content cards - [Bootrap Cards](https://getbootstrap.com/docs/5.2/components/card/)
-   Number of fake or fact votes
-   Comments

### Account screen
-   Sign up, sign in, sigh out screens

## Testing
-   Bugs
    -   styles.css not loading in Heroku. Resolved by setting DEBUG to FALSE in settings.py

-   Validator testing
    -   [Python - PEP3](docs/pep8_screenshots.md)
    -   [HTML - w3]
    -   [CSS - Jigsaw]


## Credits
-   CI I think before i blog 
-   Bootstrap documentation
-   Wireframes created on [Lucid](https://lucid.app/)
-   Content
    -   Fact posts from [bestlifeonline](https://bestlifeonline.com/common-myths/)
    -   Fake posts from [Insider](https://www.insider.com/true-facts-that-sound-fake-2017-8#the-guinness-book-of-world-records-was-created-to-settle-bar-arguments-4)
-   Code from https://dontrepeatyourself.org/post/django-blog-tutorial-part-4-posts-and-comments/