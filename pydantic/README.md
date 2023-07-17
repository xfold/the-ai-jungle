# Pydantic

> **Note**
**You can find the jupyter notebook [here](pydantic.ipynb)**

In this code, I've used the Pydantic library and typing. Both are powerful tool for data validation using Python type annotations. 

I've checked how Pydantic enforces type checking and raises errors when data of the wrong type is provided. I've also shown how Pydantic can parse data from complex types to simple Python types and vice versa. I created a `User` object from a dictionary, serialized the `User` object to JSON, and then parsed the JSON back to a `User` object. Pydantic handled all of these type conversions automatically, ensuring the integrity of the data and making the data handling process easier.
