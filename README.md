# Analytic Hierarchy Process Solver in Python
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()

## Theory
Saaty's AHP model for making decision
[AHP](https://ac.els-cdn.com/0270025587904738/1-s2.0-0270025587904738-main.pdf?_tid=dd2ff8f7-5309-49f1-86de-ba06bfb64173&acdnat=1522246227_0c33ef0d5df5ca8cd4b16ecf64633234)

also see [wiki of AHP](https://en.wikipedia.org/wiki/Analytic_hierarchy_process) and
[car example](https://en.wikipedia.org/wiki/Analytic_hierarchy_process_–_car_example)

## Download

```python
pip install pyahp
```

## Example

There are tow examples in doc folder.

### Example of television.json

```python
import json
from pyahp import *

model = json.load(open(pathto/television.json))  # or define it as a dict directly
ahp_model = parse(model)   # dict -> AHP Model Class
ahp_model.get_priorities() # get priorities
```


### Command Line in Shell

	python pathto/pyahp -f pathto/television.json

	[+] Television Model
		Method: eigenvalue
		Results:
			Samsung: 0.243
			Sony: 0.106
			Panasonic: 0.27
			Toshiba: 0.38
		Recommended is Toshiba

## Maintainer
- Abhinav Mishra [@mishrabhinav](https://github.com/mishrabhinav)
