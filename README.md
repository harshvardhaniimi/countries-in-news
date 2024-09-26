# Countries in News: How are countries portrayed in popular international media?

## Objective
We want to understand and visualize how countries are portrayed in the popular media.
1. Get news reported on various countries (A) by publishers based in other countries (B).
2. Perform sentiment analysis to how positive/negative news sentiments have changed over time.
3. Do topic modelling to see what are common themes associated by countries.
4. Identify potential biases in portrayal of some countries by other countries. 

Although we would like to focus on selected countries right now, we should make the code modular enough to be used for any given set of countries.

- Countries A: USA, UK, India, China, Russia
- Countries B: USA, UK, India, China, Russia

The countries list might lengthen/shorten depending on how much effort it is.

## Data
The data will be sourced from [GDELT Project](https://analysis.gdeltproject.org/) ("Global Database of Events, Language, and Tone") which provides a global database of news articles.
They have a [Python API](https://github.com/alex9smith/gdelt-doc-api) as well as [Google BigQuery](https://cloudplatform.googleblog.com/2014/05/worlds-largest-event-dataset-now-publicly-available-in-google-bigquery.html) so we can directly download the data for free.

ChatGPT can write great SQL code for BigQuery, so we can use that to get the data.

## Team Members

1. Harshvardhan (Harsh)
2. Jeremiah Augustine
3. Faith Chernowski
4. Colin Canonaco
