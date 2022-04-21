## The task

One of the main ways to deliver data intensive applications to the customers, while maintaining
the reasonable simplicity of integration, is to write a web API which would allow access to the
data scientific output (oftentimes statistical models) or analyzed data. This time we got off easy
and all we need to deliver is a simple web API which serves static content received through
classic ETL (extract-transform-load) pipeline.

# Subtasks
    1. Pick your favorite data source and fetch data from it.
        Ideas: scrape subreddit (e.g. https://www.reddit.com/r/Bunnies/) or real estate portal (e.g.
        Estonian https://www.kv.ee/), query existing web APIs (e.g. from
        https://rapidapi.com/collection/list-of-free-apis), use kaggle data set such as
        https://www.kaggle.com/c/dogs-vs-cats/data
    2. If fetched data has to be transformed, fields casted to specific data types, or minor
    corrections applied to the data, feel free to.
        Ideas: use Python libraries/tools such as pandas, luigi, Airflow, whatnot. Shell and other
        tools are cool as well.
    3. Store the possibly transformed data persistently.
        Ideas: txt, csv, parquet, sqlite, postgres, elasticsearch, mongodb, redis, neo4j, S3, …
    4. Write a (RESTful?) web API in Python 3.9+ to serve at least some parts of the stored
    data. Extra credits, if API call allows to also sync/get new data.
        Ideas: Swagger, Openapi, flask, django, falcon, 

## What will be assessed?
The overall solution and how it is done. There are innumerous things that make up a good
solution, some of which are listed below. Wow effect can be made with even the smallest efforts
and not everything needs to be there.
    1. Overall code quality, structure, readability, and maintainability (including conformance
    with pep8 through IDE, pylint; bandit for security? )
    2. Code readability and maintainability (e.g docstrings, decoupling, variable naming)
    3. The structure of the codebase.
    4. Tests. No need to go crazy, but even some will go a long way (e.g pytest)
    5. Error handling and system logging.
    6. Usage of version control (e.g. git).
    7. Delivering the solution and handling the environment. Instructions to set up or
    dockerized or setup.py or static environment configuration files or alike