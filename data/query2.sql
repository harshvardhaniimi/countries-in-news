-- LINK: https://console.cloud.google.com/bigquery?ws=!1m7!1m6!12m5!1m3!1sgdelt-437214!2sus-central1!3s7673c423-17ef-4f27-9689-b98031a0f5e1!2e1

EXPORT DATA OPTIONS(
  uri = 'gs://gdelt1/gdelt-2024-11-20-*.csv',
  format = 'CSV',
  overwrite = True,
  header = True,
  field_delimiter = ','
) AS

SELECT 
  SQLDATE,  -- Date of the event
  Actor1CountryCode,  -- Country code of the first actor
  Actor2CountryCode,  -- Country code of the first actor
  GoldsteinScale,  -- The event impact score
  AvgTone,  -- Average sentiment/tone of the media coverage
  NumArticles, -- Number of articles that mention this event
  SOURCEURL  -- URL of the article
FROM 
  `gdelt-bq.full.events`
WHERE 
  -- Filter events where both actors are in this list
  Actor1CountryCode IN ('USA', 'IRN', 'IRQ', 'GBR', 'CHN', 'JPN', 'AUS', 'RUS', 'CAN', 'FRA', 'IND', 'UKR', 'NGA', 'PAK', 'TUR', 'ISR')
  AND Actor2CountryCode IN ('USA', 'IRN', 'IRQ', 'GBR', 'CHN', 'JPN', 'AUS', 'RUS', 'CAN', 'FRA', 'IND', 'UKR', 'NGA', 'PAK', 'TUR', 'ISR')
  
  -- Filter by date
  AND SQLDATE >= 20130401
  AND SQLDATE <= 20241120
  
  -- Select a random 2.5% of the filtered data
  AND RAND() < 0.025
  
  -- Filter events from specified reputable news sources
  -- AND (
  --   SOURCEURL LIKE '%nytimes.com%' OR  -- The New York Times (USA)
  --   SOURCEURL LIKE '%washingtonpost.com%' OR  -- Washington Post (USA)
  --   SOURCEURL LIKE '%bbc.com%' OR  -- BBC (UK)
  --   SOURCEURL LIKE '%thehindu.com%' OR  -- The Hindu (India)
  --   SOURCEURL LIKE '%timesofindia.indiatimes.com%' OR  -- The Times of India (India)
  --   SOURCEURL LIKE '%xinhuanet.com%' OR  -- Xinhua (China)
  --   SOURCEURL LIKE '%scmp.com%'  -- South China Morning Post (China)
  -- )
  
  
ORDER BY 
  SQLDATE DESC;  -- Order the results by the event date in descending order