#! /usr/bin/env python3
import psycopg2
DBNAME = "news"


def main():
    try:
        db = psycopg2.connect(database=DBNAME)  # connect to database
    except (psycopg2.DatabaseError, e):
        print("<error message>")
    # open cursor
    c = db.cursor()
    # Queries
    # First Question
    most_popular_articles = """SELECT title, count(*) as num
  FROM articles, log
  WHERE log.path = CONCAT('/article/',articles.slug)
  GROUP BY title
  ORDER BY num
  desc limit 3;"""
    # excute querie
    c.execute(most_popular_articles)
    # Fetch and print
    print("\nMOST POPULAR THREE ARTICLES OF ALL TIME:")
    count = 1
    for i in c.fetchall():
        print('(' + str(count) + ') ' + str(i[0]) + " -- " +
              str(i[1]) + " views \n")
        count += 1

    # Second Question
    most_popular_authors = """SELECT authors.name, count(*) as num
  FROM articles, log,authors
  WHERE log.path = CONCAT('/article/',articles.slug)
  AND articles.author = authors.id
  GROUP BY authors.id
  ORDER BY num desc
  LIMIT 3;
  """
    # excute querie
    c.execute(most_popular_authors)
    # Fetch and print
    print("\nMOST POPULAR THREE AUTHORS OF ALL TIME:")
    count = 1
    for i in c.fetchall():
        print('(' + str(count) + ') ' + str(i[0]) + " -- " + str(i[1]) +
              " views \n")
        count += 1

    # Third Question
    more_than_one_error = """  SELECT *
  FROM err_rate
  WHERE err_rate.percent >1
  ORDER BY err_rate.date;"""
    # excute querie
    c.execute(more_than_one_error)
    # Fetch and print
    print("\nDAYS WITH MORE THAN ONE PERCENT ERROR REQUESTS:")
    count = 1
    for i in c.fetchall():
        print('(' + str(count) + ') ' + str(i[0]) + " -- " +
              str(round(i[1], 2)) + "% errors \n")
        count += 1
    c.close()
    db.close()


if __name__ == '__main__':
    main()
