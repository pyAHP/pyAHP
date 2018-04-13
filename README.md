# Analytic Hierarchy Process Solver
The analytic hierarchy process (AHP) is a structured technique for organizing
and analyzing complex decisions, based on mathematics and psychology. It was
developed by Thomas L. Saaty in the 1970s and has been extensively studied and
refined since then.[1](https://www.sciencedirect.com/science/article/abs/pii/037722179090057I)

The Wikipedia [2](https://en.wikipedia.org/wiki/Analytic_hierarchy_process) page
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

There are two examples in doc folder.

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
$> python pathto/pyahp -f pathto/television.json
    [+] Television Model
	    Method: eigenvalue
	    Results:
		    Samsung: 0.243
		    Sony: 0.106
		    Panasonic: 0.27
		    Toshiba: 0.38
	    Recommended is Toshiba
```

## Maintainer
- Abhinav Mishra [@mishrabhinav](https://github.com/mishrabhinav)
