# Log Parser
CLI tool to parse logs following the format below. Returns a list of hostnames connected to a given host during a given period.
The .txt file has no header and the columns are: UNIX timestamps in milliseconds, host where the connection starts and host that receives the connection.

|                	|          	|       	|
|---------------	|----------	|--------	|
| 1565647205599 	| Keimy    	| Dmetri 	|
| 1565647212986 	| Tyreonna 	| Rehgan 	|
| 1565647228897 	| Heera    	| Eron   	|
| 1565647246869 	| Jeremyah 	| Matina 	|
| 1565647247170 	| Khiem    	| Tailee 	|

# Installation
You can clone the repository:
```commandline
git clone https://github.com/annaviper/logparser.git
```
From project folder:
```
python -m build

python -m pip install dist/logparser-0.1.0-py3-none-any.whl
```
or
```
pip install -e .
```

# Usage examples
-f: file to read  
-i: initial time  
-e: end time  
-host: target hostname  
-o: file to save output (optional)
```
python ./src/log_parser.py -f input-file.txt -i 1565647204351 -e 1565733598341 -host Matina -o output.txt
```

# Testing
```commandline
pytest
```
