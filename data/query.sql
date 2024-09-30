-- LINK: https://console.cloud.google.com/bigquery?ws=!1m7!1m6!12m5!1m3!1sgdelt-437214!2sus-central1!3s7673c423-17ef-4f27-9689-b98031a0f5e1!2e1

EXPORT DATA OPTIONS(
  uri = 'gs://gdelt-storage/gdelt-2024-09-30-*.csv',
  format = 'CSV',
  overwrite = True,
  header = True,
  field_delimiter = ','
) AS

SELECT 
  SQLDATE,  -- Date of the event
  Actor1CountryCode,  -- Country code of the first actor
  GoldsteinScale,  -- The event impact score
  Actor1Geo_CountryCode,  -- Geographic location of the first actor
  AvgTone,  -- Average sentiment/tone of the media coverage
  SOURCEURL  -- URL of the news source
FROM 
  `gdelt-bq.full.events`
WHERE 
  -- Filter events where the first actor is from the USA, India, or China
  Actor1CountryCode IN ('USA', 'IND', 'CHN') 
  AND SQLDATE >= 20000101  -- Include events from January 1, 2000 onwards
  AND SQLDATE <= 20201231  -- Include events until December 31, 2020
  
  -- Filter events from specified reputable news sources
  AND (
    SOURCEURL LIKE '%nytimes.com%' OR  -- The New York Times (USA)
    SOURCEURL LIKE '%washingtonpost.com%' OR  -- Washington Post (USA)
    SOURCEURL LIKE '%bbc.com%' OR  -- BBC (UK)
    SOURCEURL LIKE '%thehindu.com%' OR  -- The Hindu (India)
    SOURCEURL LIKE '%timesofindia.indiatimes.com%' OR  -- The Times of India (India)
    SOURCEURL LIKE '%xinhuanet.com%' OR  -- Xinhua (China)
    SOURCEURL LIKE '%scmp.com%'  -- South China Morning Post (China)
  )
  
  -- Select a random 10% of the filtered data
  -- AND RAND() < 0.1
  
ORDER BY 
  SQLDATE DESC;  -- Order the results by the event date in descending order