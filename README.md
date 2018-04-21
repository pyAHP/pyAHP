# Analytic Hierarchy Process Solver
The analytic hierarchy process (AHP) is a structured technique for organizing
and analyzing complex decisions, based on mathematics and psychology. It was
developed by Thomas L. Saaty in the 1970s and has been extensively studied and
refined since then.[[1](https://www.sciencedirect.com/science/article/abs/pii/037722179090057I)]

The Wikipedia [[2](https://en.wikipedia.org/wiki/Analytic_hierarchy_process)] page
on AHP references two full examples of AHP and many more can be found on the
internet.

`pyAHP` provides a flexible interface to build AHP models and solve them using
a plethora of methods. Checkout the documentation [here](https://pyahp.gitbook.io/pyahp/).

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]() [![CircleCI](https://circleci.com/gh/pyAHP/pyAHP.svg?style=shield)](https://circleci.com/gh/pyAHP/pyAHP)

## Installation
To install `pyAHP`, simply:
```python
pip install pyahp
```

## Getting Started

### Using as a `python` module

```python
import json
from pyahp import parse

with open('model.json') as json_model:
    # model can also be a python dictionary
    model = json.load(json_model)

ahp_model = parse(model)
priorities = ahp_model.get_priorities()
```


### Using on the command line

```
$> python -m pyahp -f examples/television.json
    [+] Television Model
	    Method: eigenvalue
	    Results:
		    Samsung: 0.243
		    Sony: 0.106
		    Panasonic: 0.27
		    Toshiba: 0.38
	    Recommended is Toshiba
```

## Model Schema
The models supplied to the library are in JSON format. The model has to follow
a specific schema and a number of errors are raised in case the schema
validation  fails. A very simple model with three criteria and one criteria
with two subcriteria and three alternatives is as follows:

```javascript
{
  "name": "Sample Model",
  "method": "approximate",
  "criteria": ["critA", "critB", "critC"],
  "subCriteria": {
    "critA": ["subCritA", "subCritB"]
  },
  "alternatives": ["altA", "altB", "altC"],
  "preferenceMatrices": {
    "criteria": [
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]
    ],
    "subCriteria:critA": [
      [1, 1],
      [1, 1]
    ],
    "alternatives:subCritA": [
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]
    ],
    "alternatives:subCritB": [
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]
    ],
    "alternatives:critB": [
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]
    ],
    "alternatives:critC": [
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]
    ]
  }
}
```

### Supported Methods
There are a wide variety of methods available for calculating the priorities
from preference matrices. This library currently supports the following
methods:

- Approximate (`approximate`)
- Geometric (`geometric`)
- Eigenvalue (`eigenvalue`)

### Fields in the model

| Field                    | Type     | Description |
|--------------------------|----------|-------------|
| **`name`**               | `string` | Name of the model. It is used when the library is called from the command line and ignored when used as a python library. Defaults to the filename in the command line mode. |
| **`method`**             | `string` | The method/algorithm used to calculate the priority vectors from the preference matrices. It should be one of the supported methods. `required`  |
| **`criteria`**           | `array`  | An array of strings containing the names of all the top level criteria. All the names should be `unique`. `required`  |
| **`subCriteria`**        | `object` | It contains the sub-criteria definitions with criterion as the key and an array of strings as the sub-criteria. |
| **`alternatives`**       | `array`  | An array of strings containing the names of all the alternatives. All the strings should be `unique`. `required`  |
| **`preferenceMatrices`** | `object` | An object with key of the form `criteria` or `subCriteria:<criteriaName>` or `alternative:<criteriaName>` and the value is a 2D square matrix with integer elements. `required`|

In the sample model above, due to the design of the model and hierarchy,
`critA` has two sub-criteria. Hence, we need to provide a preference matrix for
the sub-criteria of `critA`, named `subCriteria:critA`, and two `alternative`
preferences matrices with the name `alternatives:subCritA` and
`alternatives:subCritB`. All the other criteria have corresponding preference
matrices.

## Maintainer
- Abhinav Mishra [@mishrabhinav](https://github.com/mishrabhinav)
