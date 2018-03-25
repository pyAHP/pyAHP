# Analytic Hierarchy Process Solver in Python
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()

## Theory
Saaty's AHP model for making decision
![AHP](https://en.wikipedia.org/wiki/Analytic_hierarchy_process)

## Example

### Scripts

	model = json.load(open(pathto/television.json))  # or define it as a dict directly
	ahp_model = parse(model)   # dict -> AHP Model Class
	ahp_model.get_priorities() # get priorities


### Command Line in Shell

	python pathto/pyahp -f pathto/television.json

	[+] Television Model
		Method: eigenvalue
		Results:
			Samsung: 0.243
			Sony: 0.106
			Panasonic: 0.27
			Toshiba: 0.38

## Maintainer
- Abhinav Mishra [@mishrabhinav](https://github.com/mishrabhinav)
