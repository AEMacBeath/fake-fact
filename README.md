# Fake or Fact
_Note: add responsive screenshot_

## Project Description
_Note: add description_

## Table of Contents _Note: add links to ToC_
-   Project Description
-   Features
-   Build Process
-   Testing
    -   Validator Testing
    -   Bugs
-   Technologies Used
-   Credits 

## Features _Note: add screenshots for all features_
### All views
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


## Build Process
1. Inital user stories <!--Complete-->
    -   [USER STORY: View posts](https://github.com/AEMacBeath/fake-fact/issues/1)
    -   [USER STORY: Interact with Content](https://github.com/AEMacBeath/fake-fact/issues/2)
    -   [USER STORY: Create Account](https://github.com/AEMacBeath/fake-fact/issues/3)
    -   [USER STORY: Create draft posts](https://github.com/AEMacBeath/fake-fact/issues/4)
    -   [USER STORY: Publish posts](https://github.com/AEMacBeath/fake-fact/issues/5)
    -   [USER STORY: Edit posts](https://github.com/AEMacBeath/fake-fact/issues/6)
    -   [USER STORY: Delete posts](https://github.com/AEMacBeath/fake-fact/issues/7)
    -   [USER STORY: Open a Post](https://github.com/AEMacBeath/fake-fact/issues/8)
2. Initial homepage design wireframe
![initial_design_wireframes](readme_images/initial_design_wireframe.png)
3. Django <!--Complete-->
    -   Project (fakefact)
    -   App (blog)
5. Deploy App in Heroku - [fakefact2022](https://dashboard.heroku.com/apps/fakefact2022)<!--Complete-->
6. Post Model <!--Complete-->
    -   featured_image
    -   title
    -   status
    -   author
    -   created
    -   fake
    -   fact
    -   content
7. Django Admin Panel <!--Compelete-->
    -   User Stories completed
        -   [USER STORY: Create draft posts](https://github.com/AEMacBeath/fake-fact/issues/4)
        -   [USER STORY: Publish posts](https://github.com/AEMacBeath/fake-fact/issues/5)
        -   [USER STORY: Edit posts](https://github.com/AEMacBeath/fake-fact/issues/6)
        -   [USER STORY: Delete posts](https://github.com/AEMacBeath/fake-fact/issues/7)
8. Templates to render view <!--Compelete-->
    -   Install [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
    -   Add html files
    -   Link up urls
9. Homepage view <!--Compelete-->
    -   Navbar
    -   Background image
    -   Cards for posts using [Bootstrap](https://getbootstrap.com/docs/5.2/components/card/)
    -   User Stories completed
        -   [USER STORY: View posts](https://github.com/AEMacBeath/fake-fact/issues/1)
    -   _Note: Add responsive screenshot_
10. Authorisation <!--complete-->
    -   Django allauth _Note: add link to CI lesson used_
        -   [USER STORY: Create Account](https://github.com/AEMacBeath/fake-fact/issues/3)
11. Sign in, Sign up, Sign out views
    -   _Note: Add wireframe_
    -   _Note: Add Responsive Screenshot_
12. Messages <!--todo-->
    -   Message model
    -   Add to post_detail
    -   User ability to
        -   Create <!--Done-->
        -   Read <!--Done-->
        -   Update
        -   Detele
13. Post deatil view (including comments) <!--todo-->
    -   [USER STORY: Open a Post](https://github.com/AEMacBeath/fake-fact/issues/8)
    -   [USER STORY: Add Comments](https://github.com/AEMacBeath/fake-fact/issues/9)
    -   [USER STORY: View Comments](https://github.com/AEMacBeath/fake-fact/issues/10)
14. Site Pagination Buttons
    -   [USER STORY: Site Pagination](https://github.com/AEMacBeath/fake-fact/issues/11)
15. Responsive design
00. Testing
00. Tidy up
00. Finish README


## Testing
-   Bugs
    -   Heroku
        -   Main background image missing
        -   Fake Fact buttons missing from post cards
        -   Nav moved back to the left




## Credits
-   CI I think before i blog 
-   Bootstrap documentation
-   Wireframes created on [Lucid](https://lucid.app/)
-   Content
    -   Fact posts from [bestlifeonline](https://bestlifeonline.com/common-myths/)
    -   Fake posts from [Insider](https://www.insider.com/true-facts-that-sound-fake-2017-8#the-guinness-book-of-world-records-was-created-to-settle-bar-arguments-4)