# Log Analysis Project


this is the first project in Udacity's Connect Full Stack Web Developer
# project description 
 You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
 The program will run from the command line and connect to the database.
 
Questions to be answerd:
    (1) What are the most popular three articles of all time?
    (2) Who are the most popular article authors of all time?
    (3) On which days did more than 1% of requests lead to errors?
see OUTPUT.txt file for the results


# Set Up
## software 
- install vagrant 
- install virtual machine
- Download a FSND virtual machine: https://github.com/udacity/fullstack-nanodegree-vm
- download "newsdata.sql": https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdat
a.zip
- unzip the folder
- add "newadata.sql" to your project folder 

**Starting virtual machine:**
- from terminal line cd to project folder you set up above.
> cd vagrant
> vagrant up
> vagrant ssh
>  cd /vagrant
> cd log-analysis-project
- load database with this command : 
> psql -d news -f newsdata.sql
- connect to database 
>psql -d news



### to Run the Project
 - cd to project folder log-analysis-project
 - run this command
 > python3 log-analysis-project.py

#### Output 
```
MOST POPULAR THREE ARTICLES OF ALL TIME:
(1) Candidate is jerk, alleges rival -- 338647 views
(2) Bears love berries, alleges bear -- 253801 views
(3) Bad things gone, say good people -- 170098 views

MOST POPULAR THREE AUTHORS OF ALL TIME:
(1) Ursula La Multa -- 507594 views
(2) Rudolf von Treppenwitz -- 423457 views
(3) Anonymous Contributor -- 170098 views

 DAYS WITH MORE THAN ONE PERCENT ERROR REQUESTS:
(1) 2016-07-17 -- 2.26% errors
```
