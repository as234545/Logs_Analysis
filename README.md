Logs Analysis Project
==========
___
 this is an internal  reporting tool that is used to view information from the database to discover what kind of 
 articles the site's readers like.
 
## Purpose 
 ___
 the Purpose of this project is to answer three questions 
 1-What are the most popular three articles of all time? 
 2-Who are the most popular article authors of all time? 
 3-On which days did more than 1% of requests lead to errors?
 
## What is inside the database ?
 ___
 the news database contains information  about the authors, articles and web  server log for the site
 which has a time reader for each time a user load the web  page.
 
## Installation
 ___
you should have already intalled a virtualbox and vagrant then you run `vagrant up` and `vagrant ssh` 

* after you unzip the compressed folder and put is you'r local directory  cd into the file `cd Log_Analysis`
* in the command lind write `psql -d news -f newsdata.sql`
* create the views down blow 
* run the python file `python3 newsdb.py`

## Views
____
`CREATE VIEW popular_article AS
SELECT substring(path , 10) AS title , count(*) AS views 
FROM log 
GROUP BY path 
HAVING  substring(path , 10) <> '' 
ORDER BY views desc;`

`CREATE VIEW Errors_count AS
select TO_CHAR(date_trunc('day' , time ),'MON dd , yyyy') as date , count(status)  as errors_count
from log
where LEFT(status ,1) = '4'
group by 1
order by 1;`

`CREATE VIEW Total_errors AS
select TO_CHAR(date_trunc('day' , time ),'MON dd , yyyy') as date , count(status)  as total 
from log 
group by 1
order by 1;`

## output 
___
after you run the news.py successfully the output should be like this 
`What are the most popular three articles of all time? 
Candidate is jerk, alleges rival -- 338647 views
Bears love berries, alleges bear -- 253801 views
Bad things gone, say good people -- 170098 views`

`Who are the most popular article authors of all time? 
Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views`

`On which days did more than 1% of requests lead to errors?
 July 17, 2016 -- 2.26 % errors`

