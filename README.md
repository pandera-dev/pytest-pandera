# pytest-pandera

pandas data testing with pandera.

This package is a [pytest plugin](https://docs.pytest.org/en/stable/contents.html)
that leverages [pandera](https://pandera.readthedocs.io/en/stable/) for testing
_data processing_ code written in [pandas](https://pandas.pydata.org/pandas-docs/stable/).


## Motivation

Testing for the modern python data science stack is hard! The logic required
to transform your raw data into something ready for analysis or modeling can
be highly complex, and more often than not we just want to breeze through data
processing tasks and get to the fun stuff.

This package lets you balance the need for speed and the incurred technical
debt 

## Features

- Specify `pandera` schemas and add dataframe typing annotations to your
  data processing code to automatically catch schema errors.
- Test your data processing code with `pytest` and generate human-readable
  error reports to debug complex ETL pipelines more quickly.
- Unit testing support: use `pandera` schemas to generate synthetic data to
  fully isolate ETL code from real data.
- Integration testing support: or bring real-world data to test your ETL code
  end-to-end.
