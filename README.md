# Starbucks Customer Reviews

## Sentiment and Text Analysis Using R

This project analyzes customer reviews of Starbucks businesses using the Yelp Open Dataset. The analysis examines star ratings, review characteristics, word usage, TF-IDF, and sentiment patterns in customer reviews.

The project was developed as an applied text analysis project using **R**, with **Python** used for the initial extraction and preparation of Starbucks-related data from the Yelp dataset.

## Research Questions

The analysis addresses the following questions:

* How are Starbucks reviews distributed across star ratings?
* How does review length vary across rating levels?
* Which words are most characteristic of negative, neutral, and positive reviews?
* Which words occur most frequently across the review corpus?
* What sentiment and emotion patterns emerge from the review texts?
* How do star ratings and sentiment scores vary together?

## Data Source

The data comes from the **Yelp Open Dataset**, which provides business information and customer reviews.

For this project:

* **730 Starbucks businesses** were identified.
* **21,739 Starbucks reviews** were extracted.
* The reviews cover the period from **March 12, 2005 to January 19, 2022**.
* The analysis dataset contains review ratings, review text, dates, and review engagement variables.

The original Yelp JSON files are not included in this repository because of their large size. They are excluded through `.gitignore`.

## Tools and Methods

### Programming Languages

* **R** — data preparation, text preprocessing, statistical analysis, sentiment analysis, and visualization
* **Python** — initial extraction of Starbucks businesses and reviews

### Main R Packages

* `tidyverse`
* `tidytext`
* `readr`
* `dplyr`
* `tidyr`
* `ggplot2`

### Analytical Methods

* Data cleaning and preparation
* Text preprocessing and tokenization
* Exploratory data analysis
* Review length analysis
* Word frequency analysis
* TF-IDF analysis
* AFINN sentiment analysis
* NRC sentiment and emotion analysis
* Spearman rank correlation
* Data visualization with `ggplot2`

## Key Findings

### Rating Distribution

The dataset contains reviews across all five star-rating categories:

| Rating    |    Reviews |
| --------- | ---------: |
| 1 star    |      5,771 |
| 2 stars   |      2,925 |
| 3 stars   |      2,839 |
| 4 stars   |      4,275 |
| 5 stars   |      5,929 |
| **Total** | **21,739** |

The mean star rating is **3.077**.

### Review Length

Average review length varies across rating levels:

| Rating  | Mean Review Length |
| ------- | -----------------: |
| 1 star  |        88.48 words |
| 2 stars |        93.11 words |
| 3 stars |        86.05 words |
| 4 stars |        79.09 words |
| 5 stars |        66.24 words |

In this dataset, lower-rated reviews tend to be longer on average than higher-rated reviews.

### TF-IDF Analysis

TF-IDF was used to identify terms that are particularly characteristic of different rating groups.

Reviews were grouped into:

* **Negative:** 1–2 stars
* **Neutral:** 3 stars
* **Positive:** 4–5 stars

The analysis identified distinctive terms within each rating group. For example, terms associated with service problems, such as *slow*, *understaffed*, and *unfriendly*, appeared among the characteristic terms of negative reviews, while terms such as *speedy*, *nicest*, *friendliest*, and *cheerful* appeared among characteristic terms of positive reviews.

### Sentiment Analysis

AFINN sentiment scores were calculated for individual reviews and summarized by star rating.

| Rating  | Mean AFINN Sentiment |
| ------- | -------------------: |
| 1 star  |                -3.22 |
| 2 stars |                -0.84 |
| 3 stars |                 1.89 |
| 4 stars |                 4.58 |
| 5 stars |                 6.31 |

The Spearman rank correlation between star ratings and AFINN sentiment scores is **0.639**.

NRC analysis was additionally used to examine sentiment and emotion categories across the review corpus. The most frequent categories were **positive (24.50%)**, **anticipation (14.42%)**, **trust (13.25%)**, **negative (11.74%)**, and **joy (11.58%)**.

## Project Structure

```text
starbucks-customer-review-analysis/
│
├── data/
│   ├── starbucks_businesses.csv
│   └── starbucks_reviews.csv
│
├── python/
│   └── extract_starbucks.py
│
├── .gitignore
├── starbucks-customer-review-analysis.Rmd
└── starbucks-customer-review-analysis.Rproj
```

## How to Run the Project

1. Clone or download this repository.
2. Open `starbucks-customer-review-analysis.Rproj` in RStudio.
3. Open `starbucks-customer-review-analysis.Rmd`.
4. Install the required R packages if necessary.
5. Run the R Markdown document from top to bottom.

The processed CSV files required for the analysis are included in the `data/` folder. The original Yelp JSON files are not included because of their size.

## Limitations

* The analysis is based on the Yelp Open Dataset and therefore reflects businesses and users represented in that dataset.
* Yelp reviews may not represent all Starbucks customers.
* Dictionary-based sentiment methods may not fully capture context, sarcasm, negation, or other linguistic nuances.
* The observed relationship between star ratings and sentiment scores should not be interpreted as evidence of causality.
* The original Yelp JSON files are excluded from the repository because of their size.

## Conclusion

This project demonstrates an applied workflow for analyzing customer review data using R. It combines structured data analysis, text mining, TF-IDF, and sentiment analysis to examine patterns in Starbucks customer reviews.

The project also demonstrates a workflow combining **R, Python, Git, and GitHub** for an applied data analysis project.

