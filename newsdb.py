#!/user/bin/env python3
import psycopg2
import pycodestyle

"""Return all posts from the 'database', """


def get_query(sql):
    try:
        db = psycopg2.connect(dbname=news)
    except psycopg2.Error as e:
        print("unable to connect", e.args)
    else:
        c = db.cursor()
        c.execute(sql)
        result = c.fetchall()
        db.close()
        return result


#What are the most popular three articles of all time?


def q1():
    sql = "SELECT substring(path , 10) AS title , count(*) AS views \
    FROM log \
    GROUP BY path \
    HAVING substring(path , 10) <> '' \
    ORDER BY views DESC;"
    answer1 = get_query(sql)
    print ("What are the most popular three articles of all time?" )
    for article , views in answer1:
        print ( "{}, -- {} views".format(article, views))
    return


#Who are the most popular article authors of all time? 
def q2():
    sql = "SELECT name , SUM(views) as views  \
    FROM authors a , popular_article p , articles ar\
    WHERE ar.author = a.id AND p.title  = ar.slug\
    group by 1\
    order by 2 desc;"
    answer2 = get_query(sql)
    print ("Who are the most popular article authors of all time? ")
    for author, views in answer2:
        print("{}, -- {} views".format(author, views))
    return


# On which days did more than 1% of requests lead to errors?


def q3():
    sql = "SELECT Total_errors.date , ROUND( (1.0*errors_count/total )*100 ,2)as percentage\
    from Total_errors , Errors_count\
    where Total_errors.date = Errors_count.date AND ROUND( (1.0*errors_count/total )*100 ,2) >= 1;"
    answer3 = get_query(sql)
    print ("On which days did more than 1% of requests lead to errors? " )
    for date , percentage in answer3 :
        print ( "{} -- {:.2f} %  errors".format(date,percentage))
    return


if __name__ == '__main__':
    q1()
    q2()
    q3()

