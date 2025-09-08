# Introduction
This document is for further explanations regarding to [Basics of parameter estimation](https://bilby-dev.github.io/bilby/basics-of-parameter-estimation.html) document.

## Problem Statement
In this document we have some data that is measured at specific times (i.e. a discrete data). This data is beleived to come from a process that is a linear function, namely:

$$
y(t) = m t + c
$$

where $m$ is slope na d $c$ is the intercept. 

## Linear Regression

To solve this problem, a very clean and standard approach is linear regression. This is becuase we assumed that the real process is a linear function. But for more complex systems this would not be the case. 

Here this linear model is just an example to demonstrate the Bayesian Approach.

## Bayesian Approach
In the Bayesian approach, we're trying to estimate the posterior distribution of the parameters $m$ and $c4, which tells us how likely different values of these parameters are (I think this is a probabilistic view to the problem) given the data. 

The posterior distribution is proportional to:

$$
P(m,c | \{ y_i, t_i\}, H) \prop P(\{y_i,t_i\} | m,c,H) \times P(m,c|H)
$$

The first function in the right hand side is the Likelihood function, which tells us how likely our data is, given specific values for $m$, $c$.

The last function is the Prior, which, expresses what we know about $m$, and $c$ before looking at the data. For example, we might assume $m$ and $c$ to be within a range.

> This is clearly investigated in the `core.ipynb` notebook as we went through the prior package.

## The Likelihood Function
The likelihood describes how well your model explains the observed data points. The assumption here is that the data follows a Gaussian distribution. Which can be written as:

$$
P(y_i,t_i|m,c,H) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(\frac{-(y_i-(t_i m + c))^2}{2\sigma^2}\right)
$$

This is for a single data point, for more the whole likelihood function (i.e. $P(\{y_i,t_i\}|m,c,H)$ each single-data likelihood multiplied together (because we are assuming the data are independent from one another).

### Log-Likelihood

Instead of working with the likelihood directly, it's often easier to work with the logarithm, since the products would turn into sums.

## Prior Distribution
The prior represents our assumptions and beliefs about $m$ and $c$ before seeing the data. In this case, the prior is uniform over certain ranges for $m$ and $c$:

$$
P(m,c|H) = P(m|H) \times P(c|H) = \text{Unif}(0,5) \times \text{Unif}(-2,2)
$$

This means that before looking at the data, we assume that $m$ is between $0,5$ and $c$ is between $-2,2$.

## Posterior distribution
Finally, after combining the likelihood and the prior, we get the posterior distribution. This basically is the updated beliefs about $m$ and $c$ after taking the data into account.


