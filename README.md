# RAAN Case Study

Network visualization tool for the RAAN Case Study.

Given an input file that describes a network architecture with nodes and edges defined in the same format as in  `ran_case_study.xlsx`, the program builds and displays a directed graph representing the network.

### Setup

To start the application run `sh setup.sh <filepath> [<port>]`, where

-  `<filepath>` is the the path to the `.xlsx` file describing the network,
- `<port>` (optional) specifies the port which the local web server is run on; defaults to 8000.

The application can then be accessed at `localhost:<port>`.

### Deployed version

This application is available also deployed and available at this [link](https://raan.surge.sh).

### Notes

For the sake of reproducibility, I added to this repo the file `environment.yml`, which specifies the version of each package in the conda environment that I used for the development of the application. In particular, I explicitly installed `pandas`, `xlrd` and `openpyxl`to be able to process an Excel file using python. 

