# Data Store Documentation

Authors: Hunter Chun, Justin Taylor, Jiho Seo, Jason Hong, Joseph Bain

{hunterch,jdtaylor,jihoseo,jason810,jbain359} @ bu.edu

## Description
1. Cache: We cache the results of each new photo, and fingerprint it with an MD5 hash so it is searchable within the SQLite DB. For example, if a user uploads a photo of a sunset, the songs returned are saved with the MD5 hash. Before another photo is processed, its MD5 hash is searched for within the db to make sure it hasn't already been done.

This significantly improves the latency of duplicate requests, as no API calls are necessary in these cases.

2. Data Models
We are using a SQLite relational database to store user profiles (user ID, name, email, and profile picture), as well as image data (photo iD, hash, songs, author ID, time created, title). The photo and user tables are correlated by the author ID.

![](https://github.com/jihoseo852/CS411-Team3/tree/master/docs/notes/erd.png)

3. Sequence Diagram: 

![](https://github.com/jihoseo852/CS411-Team3/tree/master/docs/notes/seqdiagram.png)
