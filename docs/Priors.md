# Prior
## What are Priors
In Baysian statistics, a prior represents your belief about a model parameter before you have any data. It's a way of encoding what you know about the parameters in your model.


## How to Define them in Bilby

We can define priors in `bilby` using either a simple python dictionary, or the special `PriorDict` class which will give us more functionalities.

1. Sample Example Using Python Dictionary
```python
priors = {}
priors['a'] = bilby.prior.Uniform(minimum=0, maximum=10, name='a')
prioir['b'] = 5
```

Here `b` is considered a delta function prior. Meaning that the value of it is fixed at $5$. If you define priors using `PriorDict` you can have a sample method that would give random values of `a` and `b` based on the defined priors (gaussian, uniform, etc).

Available Prior classes are:
- Uniform Prior
- Gaussian Prior
- Multivariate Gaussian Prior

## Adding Constraints
Sometimes, we may want to impose constraints on the prior. For example, you might want to enforce that one parameter must always be greater than or equal to another. This can be done using constraint priors.

Here's an example

```python
def convertXYToZ(parameters):
    convertedparam = parameters.copy()
    convertedparam['z'] = parameters['x'] - parameters['y']
    return convertedparam
```

