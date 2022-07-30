# Project Planning

## Steps to complete project
1. Install Django and supporting libraries
0. Create Django project (fakefact) and app (blog)
0. Deploy App in Heroku - [fakefact2022](https://fakefact2022.herokuapp.com/)
0. Create wireframes _Note: add wiredrames in seperate md_
0. Start [Fake-Fact User Stories Project](https://github.com/users/AEMacBeath/projects/5/views/2) with user stories
0. Complete user stories

## User stories and tasks
_Note: add links to user stories_

| Epic            | User Story                         | Tasks                                                        |
| --------------- | ---------------------------------- | ------------------------------------------------------------ |
| Admin           | USER STORY: Create draft posts     | Build Post model                                             |
|                 | USER STORY: Edit posts             | Create Django super user                                     |
|                 | USER STORY: Delete posts           | Link Post model to Admin Panel in admin.py                   |
|                 | USER STORY: Publish posts          | Define publish_post function in admin.py for Post model      |
|                 | USER STORY: Accept Messages        |                                                              |
|                 |                                    |                                                              |
| Authorisation   | USER STORY: Create Account         | Install Django allauth                                       |
|                 |                                    | Edit Account signup.html template                            |
|                 | USER STORY: Sign in / out          | Edit Account login.html template                             |
|                 |                                    | Edit Account logout.html template                            |
|                 |                                    |                                                              |
| User Interface  | USER STORY: View posts             | Create base.html and index.html view code                    |
|                 | USER STORY: Site Pagination        | Set up Django pagination                                     |
|                 |                                    | Edit base.html footer to include Next / Prev buttons         |
|                 | USER STORY: View Messages          | Create Boostrap cards on post_detial.html to display Messages |
|                 |                                    | Inject Message model conent to cards                         |
|                 |                                    |                                                              |
| User Interaction | USER STORY: Open a post           |                                                              |
|                 | USER STORY: Add Messages           |                                                              |
|                 | USER STORY: Vote Fake Fact on posts |                                                             |
|                 |                                    |                                                              |


0.  _Notes: to be re-written for final README_
0. Post Model
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
12. Messages <!--Done-->
    -   Message model
    -   Add to post_detail
    -   User ability to <!--Done-->
        -   Create
        -   Read
        -   Update
        -   Detele
13. Post deatil view (including comments) <!--Done-->
    -   [USER STORY: Open a Post](https://github.com/AEMacBeath/fake-fact/issues/8)
    -   [USER STORY: Add Comments](https://github.com/AEMacBeath/fake-fact/issues/9)
    -   [USER STORY: View Comments](https://github.com/AEMacBeath/fake-fact/issues/10)
14. Site Pagination Buttons <!--done-->
    -   [USER STORY: Site Pagination](https://github.com/AEMacBeath/fake-fact/issues/11)
15. Responsive design <!--done-->
00. Testing
00. Tidy up
00. Finish README

