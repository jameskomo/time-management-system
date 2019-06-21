# Time Management System Watch

![Image Gallery](https://www.noobpreneur.com/wp-content/uploads/2016/12/time-management-1.jpg)

This is a simple Python Django time management system that allows users create an account and log in, add (and edit and delete) a row what they have worked on, what date, for how long. This system has three roles with different permission levels: a regular user would only be able to CRUD on their owned records, a user manager would be able to CRUD users, and an admin would be able to CRUD all records and users. The system includes a REST API that makes it possible to perform all user actions via the API, including authentication and implements AJAX for better user experience.

You can see the live Application here [SoftSearch Time Management System](https://softsearch.herokuapp.com/).

Author Information
========
James Komo 

Features
========

- Built with Python 3.6, Djang0 2.0 Framework
- Styled using Bootstrap4
- Uses PostgreSQL DB and Deployed to Heroku
Allows users to:
- Sign in with the application to start using.
- add (and edit and delete) a row what he has worked on, what date, for how long.
- Set up a profile about me and be able to update profile as needed.
- Perform all user actions via the REST API, including authentication
- Search Postings based on Post title
- Create Posts that will be visible to everyone 
- Perform CRUD operations on posts they own


Behavior Driven Development (BDD)
================================
| Input                                                                             | Output                                                                                               |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| - Sign in with the application to start using.                                    | On signup, user is navigated to login page and on submitting correct credentials can visit home page |
| - add (and edit and delete) a row what he has worked on, what date, for how long. | User has CRUD control over their own postings                                                        |
| - Set up a profile about me and be able to update profile as needed.              | Users can update profile and create all profile details                                              |
| - Perform all user actions via the REST API, including authentication             | The REST API handles all POST, GET operations and includes tokens                                    |
| - Search Postings based on Post title                                             | Users can search by clicking the search  bar                                                         |
| - Create Posts that will be visible to everyone                                   | Based on authentication, users can create posts                                                      |

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to:

-   Have python installed
-   Have PostgreSQL DB installed
-   Have a terminal to interact with the app.
-   Any text editor
-   Browser to view
-  -Create a Virtual Environemnt, install Django >=2.0 and its dependencies


Installation
========

    $ git@github.com:jameskomo/time-management-system.git


Build & Deployment
========

**NOTE:** You need to have fully cloned it to run it locally.


    (virtual) $ python3.6 manage.py runserver

    # it will launch the web page from local server. You can also visit the livelink [here](https://softsearch.herokuapp.com/).
 to use the system

##Built With

- Built with Python 3.6
- Django2.0
- Styled using Bootstrap

Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!

Known Bugs
========
There are currently no known bugs for the app. However, I will be updating the README incase any bugs arise.

## License

MIT License

Copyright (c) 2019 James Komo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
