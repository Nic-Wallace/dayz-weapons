# [DAYZ WEAPONS](https://dayz-weapons-f7806c760857.herokuapp.com)

DayZ Weapons is a tool for players of the game DayZ. It displays every weapon available in-game along with it's statistics. 
The goal for this site is to make a comprehensive and up-to-date list available to its users.

![screenshot](documentation/mockup.png)

## UX

The design of the DayZ Weapons application has been kept clean and simple, with the focus of the site being the weapon listings.
The simple design of the site makes it user friendly, with a clear menu and each page having a crisp layout that is the same for the entire application.
This makes DayZ Weapons an intuitive tool that is accessible to all.

### Colour Scheme

The colours for DayZ Weapons were chosen to keep the application on a relevant theme to the game itself.
DayZ is known for the dark nights and grey infrastructure, as well as the green fields and forests.

![screenshot](documentation/colours.png)

I used [coolors.co](https://coolors.co/204b29-494949-5a5a5a-f8f9fa-ffffff) to generate my colour palette.

### Typography

- [Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono) was used for the site.

## User Stories

### Site Users

- As a site user, I can view a list of weapons pages, so that I can choose one to view.
- As a site user, I can see an image for each listing, so that I know what each weapon will look like in game.
- As a site user, I can view the weapon statistics in an organised order, so that I can see the information in an easy to read manner.
- As a site user, I can click on a weapon listing, so that I can view the statistics.
- As a site user, I can view a list of weapons, so that I can select one to view.
- As a site user, I can view a list of weapons pages, so that I can choose one to view.

### Site Admin

- As a site admin, I can log in and complete authentication, so that I can access the admin tools and keep the site secure.
- As a site admin, I can have category dropdown menus to use during weapon creation, so that I can choose from a list and complete the listing faster.
- As a site admin, I can create a weapon listing without using the admin panel, so that I can easily make new listings in an uncomplicated way.
- As a site admin, I can create draft listings, so that I can finish inputting the statistics later.
- As a site admin, I can create, read, update and delete weapons listings, so that I can manage the site content.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

<details>
<summary>Click to expand and view the Wireframes</summary>

**Desktop**
- ![screenshot](documentation/wireframe-laptop.png)

**Tablet**
- ![screenshot](documentation/wireframe-tablet.png)

**Mobile**
- ![screenshot](documentation/wireframe-phone.png)

</details>

## Features

### Existing Features

- **Page Heading**

    - The navigation bar and welcome message for the main page are easily seen by the user when they enter the site. This is beneficial as the user can see the option to log in or sign up, and if they are admin logged in, they can see the option to add a weapon or logout.

![screenshot](documentation/feature01.png)

- **Weapons List**

    - The list of weapons is laid out in a grid on the home page which adjusts row size depending on screen size. This makes the main site content easy to see for the user.

![screenshot](documentation/feature02.png)

- **Weapon Page**

    - Once a weapon is selected, the weapon page displays with the name and image of the weapon at the top of the page. This makes it clear to the user which item they are looking at.

![screenshot](documentation/feature03.png)

- **Weapon Details and Statistics**

    - Under the name and image, the rest of the weapon details are listed, which include the description from in-game. These are laid out in clear sections to make the information easy for the reader to see.

![screenshot](documentation/feature04.png)

- **Edit/ Delete**

    - This feature displays at the end of the weapon statistics, and allows a logged in admin to either edit or delete this listing. This is useful as the admin doesn't have to go to the admin panel to make changes to the listings.

![screenshot](documentation/feature05.png)

- **Edit Page**

    - The edit page displays the pre-populated form for the weapon that the admin is editing. This makes it very easy for the user to make changes.

![screenshot](documentation/feature06.png)

- **Edit Fields**

    - The rest of the edit/ add weapon pages show easy to use dropdown or text fields, which make inputting data easy for the user. There is also a clear button to save the changes that were made, or to cancel the process.

![screenshot](documentation/feature07.png)

- **User Action Confirmation**

    - When the user makes a change like editing a weapon or logging in, they will be redirected to the home page and see a banner at the top, which will confirm the action they just performed.

![screenshot](documentation/feature08.png)

- **Add Weapon**

    - This feature allows the admin to add a new weapon with the use of text fields, dropdowns and an image uploader.

![screenshot](documentation/feature09.png)

- **Sign-up Page**

    - This feature allows a user to sign in to the site. If they have admin status, they will now be able to see the edit and delete options for items, and they will be able to view drafts on the home page. This is useful as it allows the site to have security. Further functionality can be added so the regular site-user can like weapons etc.

![screenshot](documentation/feature10.png)

- **Sign-in Page**

    - This feature is useful for users that already have an account. They will be able to log in without having to sign up every time, which saves time and allows security.

![screenshot](documentation/feature11.png)

- **Pagination**

    - Once 12 weapons are displayed on the home page, a button saying "Next" will appear under the listings, when clicked it will bring the user to the next 12 weapons, where they will see "Prev" as well as the next button. This allows the user to navigate the weapon listings.

![screenshot](documentation/feature12.png)

- **Confirmation Modal**

    - When the admin attempts to delete a weapon listing, they will see a modal pop-up to warn them of the action they are about to make. This is beneficial as it warns the user that this data will be permanently deleted and will not be able to be retrieved.

![screenshot](documentation/feature13.png)

### Future Features

- Comparison tool
    - Allow the user to select multiple weapons to compare statistics.
- Category filter
    - Add ability to filter the weapon listing page.
- Favourites
    - Signed in users can favourite weapons and view their list for easy access to statistics.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.

## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.

I have 4 custom models for this application:
- `Ammunition`
- `Attachment`
- `Category`
- `Weapon`

```python
class Ammunition(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)


class Attachment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)


class Weapon(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    ammunition = models.ForeignKey(Ammunition, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, null=False, blank=False)
    weight = models.CharField(max_length=20, null=False, blank=False)
    damage = models.PositiveIntegerField(
        default=10, validators=[MinValueValidator(10), MaxValueValidator(150)],
        null=False, blank=False)
    image = CloudinaryField("image", default="placeholder")
    is_public = models.BooleanField(default=False)
```

![screenshot](documentation/erd.png)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/Nic-Wallace/dayz-weapons/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://github.com/Nic-Wallace/dayz-weapons/issues) served as an another Agile tool.

It also helped with milestone iterations on a weekly basis.

- [Open Issues](https://github.com/Nic-Wallace/dayz-weapons/issues)

- [Closed Issues](https://github.com/Nic-Wallace/dayz-weapons/issues?q=is%3Aissue+is%3Aclosed)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://dayz-weapons-f7806c760857.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: dayz-weapons).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

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

1. Go to the [GitHub repository](https://github.com/Nic-Wallace/dayz-weapons) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/Nic-Wallace/dayz-weapons.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Nic-Wallace/dayz-weapons)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Nic-Wallace/dayz-weapons)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [DjangoProject](https://forum.djangoproject.com/t/form-is-not-accepting-image-uploads/12033) | form image | how to get form to accept image uploads |
| [DjangoProject](https://docs.djangoproject.com/en/1.11/ref/clickjacking/) | settings | set x frame-options to allow amiresponsive mockup creation |
| [GitHub](https://forum.djangoproject.com/t/form-is-not-accepting-image-uploads/12033) | settings | set up local development |
| [StackOverflow](https://stackoverflow.com/questions/15998140/how-to-limit-a-view-to-superuser-only) | accounts | how to limit a view to superuser only |
| [StackOverflow](https://stackoverflow.com/questions/4884584/django-generate-default-slug) | weapon details | how to generate a default slug |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | delete weapon page | interactive pop-up (modal) |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [DayZ](https://dayz.com) | entire site | image | favicon on all pages, placeholder image for weapon listings |
| [DayZ Wiki](https://dayz.fandom.com/wiki/Weapons) | weapon listings | image | images of weapons |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank Roman from the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
