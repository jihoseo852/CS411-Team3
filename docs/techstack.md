# Our Tech Stack

Authors: Hunter Chun, Justin Taylor, Jiho Seo, Jason Hong, Joseph Bain

{hunterch,jdtaylor,jihoseo,jason810,jbain359} @ bu.edu

## Description
Our technology stack will include CSS/HTML, JS, MySQL, and Python, as well as a web server deployment, most likely with Apache. 

CSS/HTML we feel are pretty standard choices for web apps.

MySQL was chosen because we would need a robust database to cache past API calls, especially considering the fact that if similar photos are uploaded, we can essentially use the same inputs to our Spotify query. (i.e. two photos of similar sunsets should return similar song results). To minimize response time, we will only make API calls for search queries not found in the MySQL database.

We chose Python for the backend as we noticed that it had the most support across all of the API's that we wanted to use, and a vast code library that makes scripting with pre-existing tools incredibly easy. We initially considered Golang as an option, as we thought that multithreading the separate API calls would make it more efficient(we noticed that the Google Vision AI API had the potential to be particularly slow), however Python could also do similar concurrent tasks.

