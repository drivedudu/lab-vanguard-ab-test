# Vanguard: Customer Experience Optimization



## Group Members

- Eduardo Silva

- Raynard Flores

- Luis Millet

  

## Project Overview

In this project, we aimed to evaluate the effectiveness of a new, modernized user interface (UI) for Vanguard’s online process. The goal was to determine whether this new design, would improve the user experience and increase the completion rates of the online process. The project utilized data analysis techniques, performance metrics evaluation, and hypothesis testing to provide actionable insights.



An A/B test was conducted from 3/15/2017 to 6/20/2017:



- **Control Group:** Clients interacted with Vanguard’s traditional online process.

- **Test Group:** Clients experienced the new, enhanced digital interface.



## The Critical Question

Does the new, more intuitive user interface (UI) with in-context prompts encourage more clients to complete the online process compared to the traditional interface?



### Specific Goals:

1. Evaluate the Effectiveness of the New UI: 

Determine if the new, more intuitive user interface (UI) with in-context prompts leads to higher process completion rates compared to the traditional UI.



2. Analyze Client Behavior:

Examine client demographics and behavior to identify patterns and trends among users interacting with the online process.



3. Define and Measure Performance Metrics:

Establish key performance indicators (KPIs) such as completion rate, time spent on each step, and error rates to assess the impact of the new UI.



4. Conduct Hypothesis Testing:

Perform statistical tests to validate whether the differences observed between the control and test groups are statistically significant.



5. Visualize Data Using Tableau:

Create interactive dashboards and visualizations to present the experiment’s findings clearly and effectively.



## Hypotheses



*Here, we will outline our initial hypotheses based on our problem statement. These hypotheses will guide our analysis and help us focus on specific relationships within the data.*



- **Hypothesis 1:** The difference in completion rates between the new design and the old design is statistically significant.

- **Hypothesis 2:** The observed increase in completion rate from the A/B test meets or exceeds the 5% threshold.

- **Hypothesis 3:** The average age of clients engaging with the new process is the same as those engaging with the old process.



## Technologies & Dependencies

1. Python

2. Tableau



You will need to import the following:

1. Pandas --> import pandas as pd

2. Scipy.Stats --> import chi2_contigency

3. Numpy --> import numpy as np

4. Statsmodels --> import statsmodels.api as sm

5. Scipy.Stats --> import scipy.stats as st



## Getting Started



To perform a similar analisis follow these simple steps:



1.  Download the datasets from the repository. 

2.  Install dependencies into your coding notebook

3.  Run various codes to explore and analyze the data

4.  Come up with a conclusion with your findings



## Metadata



The datasets contains the following columns:



* **client_id:** Every client’s unique ID.



* **variation:** Indicates if a client was part of the experiment.



* **visitor_id:** A unique ID for each client-device combination.



* **visit_id:** A unique ID for each web visit/session.



* **process_step:** Marks each step in the digital process.



* **date_time:** Timestamp of each web activity.



* **clnt_tenure_yr:** Represents how long the client has been with Vanguard, measured in years.



* **clnt_tenure_mnth:** Further breaks down the client’s tenure with Vanguard in months.



* **clnt_age:** Indicates the age of the client.



* **gendr:** Specifies the client’s gender.



* **num_accts: **Denotes the number of accounts the client holds with Vanguard.



* **bal:** Gives the total balance spread across all accounts for a particular client.



* **calls_6_mnth:** Records the number of times the client reached out over a call in the past six months.



* **logons_6_mnth:** Reflects the frequency with which the client logged onto Vanguard’s platform over the last six months.



## Challenges



1. Hypothesis Testing and P-Values: 



Difficulty in accurately calculating p-values and applying statistical methods, which we overcame through knowledge-sharing sessions and consulting our mentor for guidance.



2. Incorporating Different Statistical Methods:



Choosing and applying the right statistical tests (chi-square, t-tests, ANOVA), which we resolved by reviewing lessons and engaging in discussions to select appropriate methods and ensure reliable results.



3. Creating Visualizations in Tableau:



Initial challenges with advanced visualizations, we addressed it by going through the lessons, and watching online tutorials. 





## Conclusions & Insights



Note: The p-value is a statistical measure indicating the probability of obtaining results as extreme as those observed, assuming the null hypothesis is true. A low p-value (usually less than 0.05) suggests the observed results are unlikely under the null hypothesis, leading to its rejection in favor of the alternative hypothesis.



- **Hypothesis 1:** "The difference in completion rates between the new design and the old design is statistically significant".



The obtained p-value is 1.10, indicating an extremely significant difference. Therefore, we can reject the null hypothesis and conclude that the sample mean is significantly different from the specific value tested.



- **Hypothesis 2:** "The observed increase in completion rate from the A/B test meets or exceeds the 5% threshold".



The observed percentage increase is 10.17%, which is greater than the 5% threshold.



Therefore, we can reject the null hypothesis and conclude that the increase in the test group's completion rate meets or exceeds the 5% threshold.



- **Hypothesis 3:** "The average age of clients engaging with the new process is the same as those engaging with the old process".



The p-value obtained is 0.0073, which is less than the typical significance level (0.05).



Therefore, we can reject the null hypothesis and conclude that the average age of clients using the new process is significantly different from those using the old process. This difference is statistically significant.

## Presentation 

Link - https://docs.google.com/presentation/d/1lsHi3wuV4JeLIkMPU02p2D5VV8Us2yOCM9hWuUI4mec/edit?usp=sharing
