# TransBorder Freight Data Analysis
This project analyzes transportation data from the Bureau of Transportation Statistics (BTS) to uncover insights into the **efficiency**, **safety**, and **environmental impact** of freight movement across U.S. borders.

# Tools Used
• Python (Pandas): For data cleaning, merging, wrangling, and analysis.
• Power BI: For visualizing trends, comparisons, and building an interactive dashboard.

# Process
This project follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology which is a set of processes for solving data science problems. 

# Step 1- Business Problem Understanding
# Project Goal
To analyze freight transportation data to uncover inefficiencies, identify environmental impacts, and suggest ways to improve logistics performance.

# Business questions; 
1.What is the total trade value and freight cost for the selected country (Canada/Mexico)?
2.What is the average cost and value per kilogram of traded goods?
3.How has the trade value changed over time (2020–2024)?
4.What is the distribution of containerized vs non-containerized goods?
5.What proportion of trade is domestic vs foreign
6.How does trade value differ between imports and exports?
7.Which transportation modes are the most and least cost-efficient (in terms of cost per kg)?
8.How does trade value compare between Canada and Mexico, across imports and exports?

# Step 2 - Data Understanding 
• Loaded the dataset from the Bureau of Transportation Statistics.
• Combined Excel files per month, then merged all monthly files into one dataset per year.
• Combine yearly datasets into one final dataset for analysis.
• Reviewed the dataset documentation to understand column definitions and codes.
• Performed exploratory data analysis to:
•	Check number of rows and columns
•	Understand data types
•	Identify missing or duplicate values

# Step 3 - Data Preparation
• Loaded the dataset into Power BI.
•	Renamed ambiguous column headers  for better clarity.
•	Replaced coded values using the provided data dictionary.
•	Created new metrics: Cost per Kg and Value per Kg 


# Step 4 - Analysis
Visualizations were developed in Power BI to answer the business questions using:
- Bar charts for comparison of import/export values across countries
- Line charts showing time trends (2020–2024)
- Pie charts for containerization and domestic vs. foreign trade proportions
- Calculated measures for cost/value efficiency

# Step 5 - Evaluation 
Insights were interpreted to support strategic decision-making, including:
- Identification of the most cost-efficient transport modes
- Analysis of trade value growth trends
- Understanding of import/export balance with Canada an

# Step 6 - Deployment 
Interactive dashboard built in Power BI, exported as PDF for offline sharing
- Presentation slide deck created to summarize business questions, methodology, and final insights
- All code, datasets, and documentation uploaded to GitHub
