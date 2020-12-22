# volga: flexible object deserialization

[![Build Status]][build] [![Azure DevOps coverage]][Azure coverage url] [![license]][license-file] [![release]][releases] [![python-version]][pypi]
[![Docs](https://img.shields.io/readthedocs/volga.svg)](https://volga.readthedocs.io)

[Build Status]: https://dev.azure.com/yefrigaitan/volga/_apis/build/status/yefrig.volga?branchName=main
[build]: https://dev.azure.com/yefrigaitan/volga/_build/latest?definitionId=9&branchName=main

[Azure DevOps coverage]: https://img.shields.io/azure-devops/coverage/yefrigaitan/volga/9
[Azure coverage url]: https://dev.azure.com/yefrigaitan/volga/_build/latest?definitionId=9&branchName=main

[license]: https://img.shields.io/github/license/yefrig/volga
[license-file]: https://github.com/yefrig/volga/blob/main/LICENSE

[release]: https://img.shields.io/github/v/release/yefrig/volga?include_prereleases&sort=semver
[releases]: https://github.com/yefrig/volga/releases

[python-version]: https://img.shields.io/pypi/pyversions/volga
[pypi]: https://pypi.org/project/volga/

## What is it?
**volga** provides fast, extensible, and expressive APIs
to deserialize any python data structure from any supported data format
(such as JSON and *eventually* YAML and more). Volga allows full customization of the deserialization 
behavior of your data structures resulting in schema-tized, validated, type-checked 
objects.

```python3
import volga

# Define your model
class User(volga.Schema):
    name: volga.fields.Str
    age: volga.fields.Int
    verified: volga.fields.Bool
  
json_data = '{"name":"bob","age":20,"verified":true}'

bob = volga.json.deserialize(json_data, User)

assert isinstance(bob, User)

print(bob) # prints object User(name='bob', age=20, verified=True)
```

## Main Features


## Documentation

Full documentation will soon be available on https://volga.readthedocs.io/en/latest/


## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/yefrig/volga

Binary installers for the latest released version are available at the [Python
package index](https://pypi.org/project/volga).

```sh
pip install volga
```

## Main Contributors

- Yefri Gaitan [@yefrig](https://github.com/yefrig)

- Ecenaz (Jen) Ozmen [@eozmen410](https://github.com/eozmen410)


## Code Organization

```
.
├── LICENSE                 
├── Makefile
├── README.md
├── azure-pipelines.yml
├── docs                    # readthedocs config and reqs
│   ├── Makefile
│   ├── conf.py
│   ├── index.md
│   ├── make.bat
│   └── requirements.txt
├── poetry.lock
├── pyproject.toml          # project configs
├── pyrightconfig.json      # pyright configs
├── tests
│   ├── fields_test.py
│   ├── json_test.py
│   ├── schema_test.py
│   └── test_test.py
├── typings                 # pyright stubs
│   └── pytest
│       ├── __init__.pyi
│       └── __main__.pyi
└── volga
    ├── exceptions.py       # module for volga error classes
    ├── fields.py           # posible field types for data structures
    ├── format.py           # API/protocols for data formats
    ├── json.py             # a JSON data format implementation
    ├── schema.py           # the schema protocol for data structures
    └── types.py            # API/protocols for deserializable data structures
```
