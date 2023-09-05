# Mercado Radar - SDK

The Mercado Radar SDK library provides convenient access to the Mercado Radar API from applications written in the Python language. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses.

For more information visit the [API Documentation](https://documenter.getpostman.com/view/7792424/2s9Xy6qVgY).

## Installation
You don't need the source code unless you want to modify the package for contribution. If you just want to use the package, just run:
```shell
pip install mercadoradar
```

## Usage

The library needs to be configured with your account's secret key which you can access through suporte@mercadoradar.com.br. 

1. Set it as the `MERCADORADAR_API_TOKEN` environment variable before using the library:
```shell
export MERCADORADAR_API_TOKEN='YOUR_API_TOKEN'
```

2. Or set `mercadoradar.api_token` to its value:
```python
import mercadoradar

mercadoradar.api_token = 'YOUR_API_TOKEN'
```

### Attribute
```python
import mercadoradar

mercadoradar.Attribute.list(attribute_type: str, search: str = None) -> list
```

### Attribute Type
```python
import mercadoradar

mercadoradar.AttributeType.list(limit: int = 100, offset: int = 0) -> list
```

### Category
```python
import mercadoradar

mercadoradar.Category.list(limit: int = 100, offset: int = 0) -> list
mercadoradar.Category.retrieve(id: int) -> dict
```

### Export
```python
import mercadoradar

mercadoradar.Export.product_history(date: date) -> bytes
```

### Product
```python
import mercadoradar

mercadoradar.Product.list(limit: int = 100,
                          offset: int = 0,
                          attributes_ids: list = None,
                          category_ids: list = None,
                          highest_price: float = None,
                          lowest_price: float = None,
                          product_names: list = None,
                          seller_ids: list = None,
                          site_ids: list = None,
                          status: str = None) -> list

mercadoradar.Product.retrieve(id: int) -> dict

mercadoradar.Product.history(id: int,
                             limit: int = 100,
                             offset: int = 0,
                             date__gte: date = None,
                             date__lte: date = None) -> list
```
- **status (str):** Choices are `ACTIVE`, `OUT_OF_STOCK`, `URL_NOT_FOUND`

### Seller
```python
import mercadoradar

mercadoradar.Seller.list(limit: int = 100, offset: int = 0) -> list
```

### Site
```python
import mercadoradar

mercadoradar.Site.list(limit: int = 100, offset: int = 0) -> list
```

## Requirements
Python 3.10.*

## Contribution
https://github.com/mercadoradar/mercadoradar-sdk

## Licence
MIT License

Copyright (c) 2023 Mercado Radar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.