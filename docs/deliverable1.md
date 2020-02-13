# Proposal: Photo-based Music Recommendations

Author(s): Hunter Chun, Justin Taylor, Jiho Seo, Jason Hong, Joseph Bain

{hunterch,jdtaylor,jihoseo,jason810,jbain359}@bu.edu

Last Updated: 2/12/2020

## Abstract

A music recommendation application that takes a photo as input, and gives Spotify recommendations.

## Proposal
Our idea is to make an application where users can upload a photo (a landscape, a person, a selfie, etc) and gives music recommendations from the photo. Google has their VisionAPI that allows us to identify what is inside of the users photo, as well as if the faces in the photo is happy, sad, joyful, laughing, etc. There is also color data and location data that we can pull from the photo. Using those key words we can use the Spotify+Genius API to give best-matching music recommendations.:

- Use the google vision api + genius lyrics api + spotify api

- Use google oauth to create a profile in database that stores the photos you take

- Could give you your most popular keywords
