<p align="center">
<img src='https://cdn.theforage.com/vinternships/companyassets/AKkAyEwWc8wjPxx9n/Gz8nAM5drF9tcbBa4/PREVIEW%20TILE%20(NEW).jpg' width=100%>
</p>

# About ANZ Virtual Experience Program

<p> <b>Data@ANZ</b> is about mining and linking datasets to develop stories that matter and challenge the status quo, to deliver on ANZ’s purpose “to shape a world where people and communities thrive”. This virtual internship seeks to equip young professionals with data analytics and predictive modeling skills that can be implemented in most organizations.

Further details about the program can be assessed [here](https://www.theforage.com/virtual-internships/prototype/ZLJCsrpkHo9pZBJNY/ANZ-Virtual-Internship?ref=tCfFoXSNJ4aLnBQye)</p> 
- The program consists of 2 modules.
- The files in this repository are only my submitted files.

<br>


# Project Details
<details>
	<summary>Problem Statement</summary>
	<br>
	<p style='text-align:justify;'>ANZ have a synthesised transaction dataset containing 3 months’ worth of transactions for 100 hypothetical customers. It contains 	         purchases, recurring transactions, and salary transactions. Based on this dataset, ANZ will want to understand the behaviours of their customers and how transactions are         undertaken by each hypothetical customer and finally, be able to predict the annual salary of their present and potential customers.
	</p>

</details>

<details>
	<summary>Project Goals</summary>
	<br>
	<p>In this project, I wanted to achieve 2 main goals and they are;</p>
	<ol>
		<li>Segment dataset and draw unique insights, including visualization of the transaction volume and assessing the effect of any outliers.</li>
		<li>Explore correlation between customer attributes and build a regression and a decision-tree prediction model based on your findings.</li>
	</ol>
</details>

<details>
	<summary>Information Needed</summary>
	<br>
	<p style='text-align:justify;'>I therefore needed the following data to help perform EDA and build my predictive model.</p>
	<ul>
		<li><b>Customer data</b> - which should include characteristics of each customer, for example, age, education, transaction mode of customer etc.</li>
		<li><b>Salary data</b> - which would indicate current salary of customers.</li>
		<li><b>Historical transaction data</b> – which should indicate every transaction the customer has performed.</li>
	</ul>
</details>

---

### Code and Resources Used
**Python Version:** 3.7\
**Packages:** Pandas, Numpy, Sklearn, Matplotlib, Datetime, Plotly, Seaborn, Wordcloud, XGBoost

<br>

### Installing Packages
<p style='text-align:justify;'>To run the jupyter notebook on your localhost, I recommend you install the packages I used for this project. You can do that by;</p>
<ul>
	<li>Downloading the <i>requirements.txt</i> file and save it into the directory you'll be working from.</li>
	<li>Open anaconda prompt and navigate into the directory containing the file.</li>
	<li>Type <i>conda create --name env-name --file requirements.txt</i> where env-name is the environment name of your choice.</li>
	<li>Once your environment is created type <i>conda activate env-name</i> and then open jupyter notebook.</li>
</ul>

---

<br>

# Summary of Steps Taken
<details>
	<summary>Data Quality Assessment</summary>
	<br>
	<p style='text-align:justify;'>The first task that I performed under the data preparation step was initial assessment of the quality of data which easily allowed me to           properly clean the data. The following were some of the issues discovered;</p>
	<ul>
		<li>Missing values in some of the columns with 2 of those columns having missing values above 40%.</li>
		<li>Discovered some columns will not be needed for the analysis.</li>
		<li>Some of the data types were not properly formatted including the date.</li>
		<li>Spatial coordinates needed to be split.</li>
	</ul>
</details>

<details>
	<summary>Data Cleaning and Preprocessing</summary>
	<br>
	<p style='text-align:justify;'>The preprocessing step (usually an iterative process) was carried out to clean the data based on data quality issues identified. Some of           the task performed in this step include;</p>
	<ul>
		<li>Handling missing values</li>
		<li>Dropping unneeded columns</li>
		<li>Proper date formatting</li>
		<li>Splitting of spatial data(longitude and latitude column)</li>
	</ul>
</details>

<details>
	<summary>Exploratory Data Analysis</summary>
	<br>
	<p style='text-align:justify;'>One of the goals for this project as mentioned earlier was to segment dataset and draw unique insights, including visualization of the             transaction volume and assessing the effect of any outliers. Based on this stated goal, I performed any set of anylysis on the cleaned data to obtain insights that               helped me to arrive at some plausible conclusions.
	</p>
	<p>To achieve the first goal, I answered a few questions using both quantitative and graphical methods. Some of the questions are listed below.</p>
	<ul>
		<li>What is the age distribution of the customers?</li>
		<li>What is the amount distribution of the customers?</li>
		<li>Are males performing more transactions as compared to females?</li>
		<li>Which transaction movement happens for most of the customers?</li>
		<li>How much do customers spend on the average?</li>
		<li>Are most of the transactions authorized?</li>
		<li>Between males and females, who spends a lot?</li>
		<li>Which suburb do most of the transactions take place?</li>
		<li>How does spending vary with state?</li>
		<li>How did the average amount spent by customers changed over time ( days, weeks)?</li>
	</ul>
	<br> 
	<h3>Sample Visualizations</h3>
	<p>
		<img src="https://i.ibb.co/Xyrq9ky/newplot-2.png" alt="newplot-2" border="0" height='300px' width='480px'>
		<img src="https://i.ibb.co/TT7zcgT/newplot-1.png" alt="newplot-1" border="2" height='300px' width='480px'>
	</p>
	<br>
	<p>
		<img src="https://i.ibb.co/7Wv830j/newplot-3.png" alt="newplot-3" border="0" height='300px' width='480px'>
		<img src="https://i.ibb.co/yB8SYsB/new.png" alt="new" border="0" height='300px' width='480px'>
	</p>
	
</details>


<details>
	<summary>Statistical Analysis</summary>
	<br>
	<p style='text-align:justify;'>For this task I further looked into the question that was asked about the spending habit of customers based on their gender. I found out 	that the number of male customers performed a lot of debit transactions than their female counterparts. I therefore needed to clearly conclude without any doubt that 	         males spend more than females and that the difference is not due to chance. To do this I performed hypothesis testing(Welch's t-Test) to draw conclusion on the result.           Here is the summray of the result;</p>
	<ul>
		<li>The hypothesis test I performed showed that there was no difference in their average spend. That is, average spend for males was the same as females</li>
		<li>Also, I concluded with 95% confidence that average spend for males will mostly fall between <i>28.35 AUD and 29.35 AUD</i> whereas that of females will fall                 between <i>26.38 AUD and 27.36 AUD</i></li>
	</ul>
</details>

<details>
	<summary>Feature Selection and Engineering</summary>
	<br>
	<p style='text-align:justify;'>The better I prapare the data for modeling, the better my model will perform. In this task, I properly prepared my data by transforming            columns, dropping irrelevant columns, handling missing and categorical values and finally merging if the need be. The following tasks were performed for this step;
	</p>
	<ul>
		<li>Creating and merging new features(annual salary, annual spending and spending ratio)</li>
		<li>Dropping unneeded columns</li>
		<li>One hot encodind of gender column</li>
		<li>Data Normalization</li>
	</ul>
	
</details>

<details>
	<summary>Predictive Modeling</summary>
	<br>
	<p style='text-align:justify;'> To complete this task I went through the various machine learning steps which includes;</p>
	<ul>
		<li><b>Data Loading</b> - In this task I loaded the cleaned data that contained all the engineered features as well as the selected ones.</li>
		<li><b>Data Understanding</b> - In this step, I used both graphical and quantitative methods to explore the distributions and correlations between customer                        attributes.</li>
		<li><b>Data Splitting</b> - I then went ahead and split the data into train and test data in readiness for modeling.</li>
		<li><b>Algorithm Evaluation</b> - In this step, I trained various algorithms on the train and standardized train data using default parameters and 10-fold cross                  validation. I then evaluated the performance of each model on the dataset and then selected the best model out of the rest. I also trained a couple of ensemble                  algorithms on the data.</li>
		<li><b>Parameter Tuning</b> - The best model turned out to be ExtraTreeRegressor which I later went ahead to tune its parameters for better performance using                     Grid Search.</li>
		<li><b>Final Model</b> - At this stage, the model was ready to make predictions. The model was able to predict the annual salaries of customers with RMSE of                      11130 and R-score of approximately 95%. I plotted the difference between the y-test and predictions and had a linear relationship which means my model did a                      good job at predicting the annual salaries.</li>
		<li><b>Model Understanding</b> -  I wanted to know which features were mostly affecting/impacting the predictions made by the model and it turned out customers                   annual spend was a major player in predicting the annual salaries of customers.</li>
	</ul>
	<h3>Sample Visualizations</h3>
	<p>
		<img src="https://i.ibb.co/yRCgS0t/download.png" alt="download" border="0" height='300px' width='480px'>
		<img src="https://i.ibb.co/PCs9mQY/download-1.png" alt="download-1" border="0" height='300px' width='480px'>
	</p>

</details>


<details>
	<summary>Summary of Results</summary>
	<br>
	<ul>
		<li>The accuracy of the final model is approximately 95% and the RMSE is approximately 11130</li>
		<li>Distribution of the difference between the expected values and the predicted values is almost normally distributed which indicates that the final model is                   suitable for predicting the annual salaries of customers.</li>
		<li>There is a strong correlation with value of about 0.95 between the actual salaries and the predicted salaries. Again, this indicates how close our model's                     prediction is to the actual values.</li>
		<li>Finally, the feature importance revealed that annual_spend and spending_ratio are the big influencers of the model's predictions</li>
	</ul>
</details>

---

### Credential 
[Earned Certificate](https://insidesherpa.s3.amazonaws.com/completion-certificates/ANZ/ZLJCsrpkHo9pZBJNY_ANZ_tCfFoXSNJ4aLnBQye_completion_certificate.pdf)

