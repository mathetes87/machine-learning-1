# Machine Learning Engineer Nanodegree
## Capstone Proposal
Juan  Roberto Honorato
__December 31st__, 2017

## Predicting EURUSD value in Forex Trading

### Domain Background
_(approx. 1-2 paragraphs)_

Forex or trading, or more formally the foreign exchange market, is a global and decentralized market for the trading of currencies. This market has a long history and can be traced back to [ancient times] (https://en.wikipedia.org/wiki/Foreign_exchange_market#Ancient). But modern Forex trading is said to have started in a free and open manner [since 1973] (https://en.wikipedia.org/wiki/Foreign_exchange_market#After_1973). Today, the foreign exchange market is the [most liquid financial market in the world] (https://en.wikipedia.org/wiki/Foreign_exchange_market#Market_size_and_liquidity) and accounted for [$5.09 trillion per day in April 2016] (https://en.wikipedia.org/wiki/Foreign_exchange_market#Foreign_exchange_market).

Autotrading, on the other hand, originates at the emergence of online retail trading [since about 1999] (https://en.wikipedia.org/wiki/Foreign_exchange_autotrading#History). As its name suggests, autotrading refers to algorithms that either operate the market on their own or signal for a human to manually take action. The possibility of entirely autonomous systems operating with real money, and (hopefully) _making_ real money is a fascinating prospect for me, and this is why I have chosen this idea to be my capstone project.

### Problem Statement
_(approx. 1 paragraph)_

In this section, clearly describe the problem that is to be solved. The problem described should be well defined and should have at least one relevant potential solution. Additionally, describe the problem thoroughly such that it is clear that the problem is quantifiable (the problem can be expressed in mathematical or logical terms) , measurable (the problem can be measured by some metric and clearly observed), and replicable (the problem can be reproduced and occurs more than once).

### Datasets and Inputs
_(approx. 2-3 paragraphs)_

The data used for the project was personally collected and is included in the `data` folder in this repository. It consists of historical data for the EURUSD Forex pair ranging from 2012 to 2017, where every row of the dataset is registered every 5 minutes, the total number of rows (or _candles_) being 438K+. This data was gathered using the [Metatrader 4] (https://www.metatrader4.com/) software, which is freely available for download.

The features gathered are the following:


* _time_: when the candle opened. The format used is `Year_Month_Day_Hour_Minute_Second`.
* _close_: price when the candle closed. In this case, since the candles follow an M5 (5 minutes) window, this is the price 5 minutes after the candle opened.
* _open_: price when the candle opened.
* _high_: highest price during the 5 minute window of the candle.
* _low_: lowest price during the 5 minute window of the candle.
* _sebas_stoch1_: first stochastic indicator gathered from proprietary indicators.
* _sebas_stoch2_: second stochastic indicator gathered with certain parameters.
* _negrita1_: first MACD indicator gathered with certain parameters.
* _negrita2_: second MACD indicator gathered with certain parameters.
* _ladrillo_: third MACD indicator gathered with certain parameters.

A sneak peek into the data throws the following table:

| **time**        | **close** | **open** | **high** | **low** | **sebas_stoch1** | **sebas_stoch2** | **negrita1**       | **negrita2**       | **ladrillo**       |
|-----------------|-----------|----------|----------|---------|------------------|------------------|--------------------|--------------------|--------------------|
| 2012_1_2_3_0_0  | 1.29377   | 1.29387  | 1.29391  | 1.29372 | 43.0             | 44.3484853625    | -0.000103977921316 | -5.60416684946e-05 | -4.79362528215e-05 |
| 2012_1_2_3_5_0  | 1.29377   | 1.29373  | 1.2938   | 1.2937  | 41.1160058737    | 43.0131702472    | -0.000124136299998 | -6.97383679821e-05 | -5.43979320163e-05 |
| 2012_1_2_3_10_0 | 1.29357   | 1.29376  | 1.29382  | 1.29357 | 35.843373494     | 39.9864597892    | -0.000154469658795 | -9.01779849445e-05 | -6.42916738504e-05 |
| 2012_1_2_3_15_0 | 1.29351   | 1.29355  | 1.29357  | 1.29348 | 29.1729323308    | 35.3774372328    | -0.000181261097638 | -0.000115268723952 | -6.59923736861e-05 |

In this section, the dataset(s) and/or input(s) being considered for the project should be thoroughly described, such as how they relate to the problem and why they should be used. Information such as how the dataset or input is (was) obtained, and the characteristics of the dataset or input, should be included with relevant references and citations as necessary It should be clear how the dataset(s) or input(s) will be used in the project and whether their use is appropriate given the context of the problem.

### Solution Statement
_(approx. 1 paragraph)_

In this section, clearly describe a solution to the problem. The solution should be applicable to the project domain and appropriate for the dataset(s) or input(s) given. Additionally, describe the solution thoroughly such that it is clear that the solution is quantifiable (the solution can be expressed in mathematical or logical terms) , measurable (the solution can be measured by some metric and clearly observed), and replicable (the solution can be reproduced and occurs more than once).

### Benchmark Model
_(approximately 1-2 paragraphs)_

In this section, provide the details for a benchmark model or result that relates to the domain, problem statement, and intended solution. Ideally, the benchmark model or result contextualizes existing methods or known information in the domain and problem given, which could then be objectively compared to the solution. Describe how the benchmark model or result is measurable (can be measured by some metric and clearly observed) with thorough detail.

### Evaluation Metrics
_(approx. 1-2 paragraphs)_

In this section, propose at least one evaluation metric that can be used to quantify the performance of both the benchmark model and the solution model. The evaluation metric(s) you propose should be appropriate given the context of the data, the problem statement, and the intended solution. Describe how the evaluation metric(s) are derived and provide an example of their mathematical representations (if applicable). Complex evaluation metrics should be clearly defined and quantifiable (can be expressed in mathematical or logical terms).

### Project Design
_(approx. 1 page)_

In this final section, summarize a theoretical workflow for approaching a solution given the problem. Provide thorough discussion for what strategies you may consider employing, what analysis of the data might be required before being used, or which algorithms will be considered for your implementation. The workflow and discussion that you provide should align with the qualities of the previous sections. Additionally, you are encouraged to include small visualizations, pseudocode, or diagrams to aid in describing the project design, but it is not required. The discussion should clearly outline your intended workflow of the capstone project.

-----------

**Before submitting your proposal, ask yourself. . .**

- Does the proposal you have written follow a well-organized structure similar to that of the project template?
- Is each section (particularly **Solution Statement** and **Project Design**) written in a clear, concise and specific fashion? Are there any ambiguous terms or phrases that need clarification?
- Would the intended audience of your project be able to understand your proposal?
- Have you properly proofread your proposal to assure there are minimal grammatical and spelling mistakes?
- Are all the resources used for this project correctly cited and referenced?
