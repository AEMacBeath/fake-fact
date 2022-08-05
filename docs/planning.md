# Project Planning

## Project Setup

1. Install Django and supporting libraries
0. Create Django project (fakefact) and app (blog)
0. Deploy App in Heroku - [fakefact2022](https://fakefact2022.herokuapp.com/)
0. Create wireframes _Note: add wiredrames in seperate md_
0. Start [Fake-Fact User Stories Project](https://github.com/users/AEMacBeath/projects/5/views/2) with user stories

## Manage posts
### User stories 
[Create draft posts](https://github.com/AEMacBeath/fake-fact/issues/4), 
[Publish posts](https://github.com/AEMacBeath/fake-fact/issues/5),
[Edit Posts](https://github.com/AEMacBeath/fake-fact/issues/6), 
[Delete posts](https://github.com/AEMacBeath/fake-fact/issues/7)

### Tasks
#### Post Model

        Model Diagram
        | Name            | Type            |
        |-----------------|-----------------|
        | featured_image  | CloudinaryField |
        | title           | CharField       |
        | content         | TextField       |
        | excerpt         | TextField       |
        | status          | IntegerField    |
        | author          | ForeignKey      |
        | created         | DateTimeField   |
        | fake            | ManyToManyField |
        | fact            | ManyToManyField |
        | published       | BooleanField    |
        | slug            | SlugField       |

#### Django Admin Panel
-   Create super user to access Django admin panel
-   Add Post model to admin.py
-   Install summernote for post content field

#### Publish posts
-   Define publish_post function in admin.py

## Homepage
### User stories
[View posts](https://github.com/AEMacBeath/fake-fact/issues/1)

#### PostList view
-   Import Django generic views and Post model to views.py
-   Create PostList view using generic.ListView

#### Templates
-   Install [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
-   Write base.html with
    -   [Bootstrap Navbar](https://getbootstrap.com/docs/5.2/components/navbar/)
    -   Background image
-   Write index.html with
    -   [Bootstrap Cards](https://getbootstrap.com/docs/5.2/components/card/) for all publised posts in post list
    -   Fake and Fact buttons on card for users to vote on post
-   Add urls to link PostList view with index.html template 

## Post detail page
### User stories
[Open a Post](https://github.com/AEMacBeath/fake-fact/issues/8),
[Site Pagination](https://github.com/AEMacBeath/fake-fact/issues/11),
[Interact with content](https://github.com/AEMacBeath/fake-fact/issues/2)

#### PostFakeVote & PostFactVote views
-   Create views to link Fake / Fact buttons on index.html to post_detial.html
-   Function to record users vore and return the value in post_detail.html

#### Template
-   Write post_detail.html with
    -   [Bootstrap Card](https://getbootstrap.com/docs/5.2/components/card/) for displaying post detail
    -   User vote displayed at the bottom of the card

#### Site Pagination
-   Add Django site pagination cose to index.html
-   Style next / prev buttons in styles.css

##  Authorisation
### User stories
[Create account](https://github.com/AEMacBeath/fake-fact/issues/3)

#### Sign up, Sign in, Sign out
-   Install Django allauth
-   Edit account signin, signup and signout html templates
    -   to extend base.html
    -   match site styling

## Messages
### User stories
[USER STORY: View Comments](https://github.com/AEMacBeath/fake-fact/issues/10),
[USER STORY: Add Comments](https://github.com/AEMacBeath/fake-fact/issues/9),
[USER STORY: Edit Comments](https://github.com/AEMacBeath/fake-fact/issues/15),
[USER STORY: Delete Comments](https://github.com/AEMacBeath/fake-fact/issues/16)

#### Message Model

        Model Diagram
        | Name     | Type          |
        |----------|---------------|
        | post     | ForeignKey    |
        | author   | ForeignKey    |
        | body     | TextField     |
        | received | DateTimeField |
        | accepted | BooleanField  |

#### Create Message
-   Create MessageForm
    -   Use Django Crispy forms
    -   Fields from Message model
        -   body


#### Update Message
-   Create MessageUpdateView using Django UpdateView
-   Write message_update.html
    -   extends base.html
    -   matches site styling
-   Add url to link view and template

#### Delete Message
-   Create MessageDeleteView using Django DeleteView
-   Write message_delete.html
    -   extends base.html
    -   matches site styling
-   Add url to link view and template

#### Post Detail template
-   Update post detail view to include messages
    -   Add new [cards](https://getbootstrap.com/docs/5.2/components/card/) to 
        -   display messages
        -   display MessageForm
    -   Add Update / Delete buttons to users own message cards
