Participa
=========

Citizens’ participation in the democratic life — either local or national — is one of the most urgent and challenging issues of today’s societies. Motivated by the efforts of the governments of [Iceland](http://en.wikipedia.org/wiki/Icelandic_constitutional_reform,_2010%E2%80%9313), [Finland](http://thegovlab.org/seven-lessons-from-the-crowdsourced-law-reform-in-finland/) and [United States](https://petitions.whitehouse.gov), an increasing number of elected authorities and political leaders have begun to take actions toward more inclusive, transparent and participatory administrations. Boosted by the World Wide Web, online civic-engagement practices have been appearing all over the world seeking to involve citizens in public consultations, deliberation, and decision-making processes oriented to address issues of public interest, such as law reforms, policy making and innovations in the public sector. 

In this context, innovative ideas and valuable opinions are more likely to appear when the group of participants is large and diverse. Understanding that the largest virtual communities today are to be found in popular social networking sites, such as Facebook, Twitter, or Google Plus, *Participa* is a concrete effort toward bringing internet-mediated civic participation tools closer to social network communities. Apart from reaching wider and larger sources of information, we aim at reducing as much as possible the participation barrier, enabling people to take part on modern civic engagement initiatives by using familiar technology, such as social networking services.
 
By providing a flexible and generic model, *Participa* enables public institutions, politicians, and elected authorities to efficiently organize, run, and harvest the information generated during civic participation initiatives. It also allows to enrich and complement already existing initiatives with opinions generated within social network communities.It is social network "agnostic" making possible to reach different social network communities simultaneously, favoring inclusiveness and broadness. It can be used as a stand-alone application or it can be integrated with existing tools. 

Model
-----
Participa exploits the power and advantages (user-friendliness, worldwide connectivity, real-time information sharing) of
general purpose **social network services** to reach and engage social network communities into online civic participation 
initiatives. Its operation is based mainly on social networks' native features: posts, comments, votes (likes, +1), hashtags. **Hashtags** are particularly important and because of this, it may work only on hashtag-supported social networking sites, such as Twitter, Facebook, Google Plus, and Instagram. Currently, *only Twitter is available*.

The remaining concepts of participa's model are the initiatives, campaigns, and challenges, which help to structure and
organize the consultants facilitating the analysis of the results. The **initiative** is the container of the consultant 
details. There the organizer, whoever public institution, elected authority, politician, civic organization, defines the name and description of the consultant, as well as, the hashtag that will be used to identify the consultant and the social network in which the consultant will be run. To avoid error collecting posts related to the consultant the initiative hashtag should be chosen carefully. 

In participa's model, each initiative is composed of one or more **campaigns**, which are the phases or stages in which 
the process of a consultant is divided in. Finally, campaigns contain **challenges**, which are the questions, topics, or 
issues to be discussed in the consultant. Further, it is included the explanation of real use case scenario to ground 
the concepts.
  

Workflow
--------

Participa's operation is divided in four simple steps, as it is outlined in the following picture. 

1. A public institution (politician, elected authority, civic organization) creates an initiative, its corresponding 
campaigns and challenges, and the hashtags to be used.
2. The initiative's organizer (a public institution in this case) "deploys" the initiative in one or multiple social networks.
3. Citizens, which are users of the social networks where the initiative was deployed, engage in the initiative by 
publishing posts containing the hashtags of the initiative and hashtag the challenge that are "solving".
4. As soon as participa finds posts containing the hashtags of the initiative and challenges, it collects and processes 
them. Through a tabular-based dashboard the answers are presented to the initiative's organizer. In addition, participa 
can be programed to sinchronize its content with a remote platform.

![model](https://dl.dropboxusercontent.com/u/55956367/participa_model.png "Participa Model")


Participa in action!
--------------------

[California Report Card (CRC)](http://www.californiareportcard.org) is a jointly coordinated effort between the 
[Data and Democracy Initiative](http://citris-uc.org/initiatives/democracy/) of the Center for Information Technology Research 
in the Interest of Society (CITRIS) of the University of California, Berkeley and the Lt. Governor of California Gavin Newsom. 

By employing a web-based application, it engages citizens in discussion about public concern issues. Specifically, 
CRC allows, in a first phase, to grade six timely topics and, in a second phase, to propose issues that merit the attention 
of the state government. The left side of the following picture illustrates the alphabetical pad used to grade the issues, 
while the right side illustrates the second phase.

<img alt="CRC Screenshots" src="https://dl.dropboxusercontent.com/u/55956367/crc_screenshots.png" height="70%" width="70%" />

Participa is currently being used to enable citizens of California to participate in CRC directly via Twitter. In this case, 
the following initiative, campaigns, challenges and hashtags were created. California Report Card and *#careportcard* were defined as the **initiative** and the initiative **hashtag**, respectively. The two phases of CRC, "grading issues" and "proposing new issues", were set as the **campaigns** of the initiative. The six CRC issues were configured as the **challenges** of the grading campaign, while the request for new issues was defined as the challenge of the proposing campaign. Each challenge was associated to a unique **hashtag**. Finally, Twitter was chosen as the **social network** to deploy the initiative.

On the left of the next picture, it is represented an example of grading a CRC issue via Twitter. Basically, it is
simply required to post a tweet with the grade -- C in this case --, the hashtag of the initiative, **#careportcard**, and the hashtag of associated to the issue, **#affordcolleges**. In a similar way, the right side of the picture illustrates how participants can propose new issues through tweets. Specifically, they send a suggestion together with the hashtag of the initiative, **#careportcard**, and the hashtag of the challenge, **#newissue**.

<img alt="CRC TW Screenshots" src="https://dl.dropboxusercontent.com/u/55956367/crc_tw_screenshots.png" height="70%" width="70%" />

Additional information on how to take part of CRC through Twitter can be found [here](https://dl.dropboxusercontent.com/u/55956367/Flyer_CRC_Twitter.pdf).

Installation
------------

1. Clone the repository `git clone https://github.com/joausaga/participa.git`

2. Go inside the repository folder and execute `pip install -r requirements.txt` to install dependencies 

3. Create a mysql database

4. Rename the file participa/settings.py.sample to participa/settings.py

5. Set the configuration parameters of the database in settings.py 

     ```
        DATABASES = {
            ...
                'NAME': '',
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
            ...
        }
      ```

6. Run `python manage.py migrate` to set up the database schema

7. Create a [Twitter application](https://apps.twitter.com) and give it read and write permissions

7. Rename the file cparte/config.sample to cparte/config

8. Set the parameters of your recently created Twitter application in cparte/config

    ```
        [twitter_api]
        consumer_key = YOUR_TWITTER_APP_CONSUMER_KEY
        consumer_secret = YOUR_TWITTER_APP_CONSUMER_SECRET
        token = YOUR_TWITTER_APP_TOKEN
        token_secret = YOUR_TWITTER_APP_TOKEN_SECRET
    ```

9. Load initial settings `python manage.py loaddata config_data.json`

10. Install Rabbit MQ broker. [Unix installation instructions](http://www.rabbitmq.com/install-generic-unix.html)

License
-------
MIT

Technologies
------------

1. [Django Framework 1.7](https://www.djangoproject.com/)
2. [MySQL](http://www.mysql.com) database and its corresponding python package
3. [Tweepy](http://www.tweepy.org) a python-based Twitter API client
4. [Django Admin Bootstrapped App](https://riccardo.forina.me/bootstrap-your-django-admin-in-3-minutes)
5. [Django Bootstrap3 App](https://github.com/dyve/django-bootstrap3)
6. [Google API Client](https://developers.google.com/api-client-library/python/)
7. [Celery](http://www.celeryproject.org)
8. [Celery for Django](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)
9. [Rabbit MQ](http://www.rabbitmq.com)

Let me know
-----------

If you use participa, please [write me](mailto:jorgesaldivar@gmail.com) a short message with a link to your project. 
It is not mandatory, but I will really appreciate it!
