
# [GLAMhack2021-DataDiver](https://hack.glam.opendata.ch/project/116)
_Automatically generate an overview of open source datasets_

Project for [GLAMhack 2021](https://hack.glam.opendata.ch/) ( [#GLAMhack2021](https://twitter.com/search?q=GLAMhack2021) ) Fri 16th April - Sat 17th April

![](./assets/Data-Diver.jpg)

# About

Finding and viewing open datasets can be time consuming. Datasets can take a long time to download, and after exploring them you realise it is not in the form you needed.

The idea is to create a tool that could run on open data providers' servers, but also on a local computer, which automatically generates an overview of the files, images and along with summary statistics.


# Implementation

Aim to create a containerised process that takes a locally available filepath and returns a html page or json with:
* collage of example images
* numbers of each file types
* if csv's are present create summary statistics with data quality 

# To Do 

[ ] get list of file in a zip (without unzipping it)
[ ] return numbers of files in a zip (without unzipping it)
[ ] make photo collage ( could unzip specific files )



