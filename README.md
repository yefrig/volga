# volga &emsp; [![Build Status]][build] [![Azure DevOps coverage]][Azure coverage url] [![license]][license-file] [![release]][releases] [![python-version]][pypi]


[Build Status]: https://dev.azure.com/yefrigaitan/volga/_apis/build/status/yefrig.volga?branchName=main
[build]: https://dev.azure.com/yefrigaitan/volga/_build/latest?definitionId=1&branchName=main


[Azure DevOps coverage]: https://img.shields.io/azure-devops/coverage/yefrigaitan/volga/1
[Azure coverage url]: https://dev.azure.com/yefrigaitan/volga/_build/latest?definitionId=1&branchName=main

[license]: https://img.shields.io/github/license/yefrig/volga
[license-file]: https://github.com/yefrig/volga/blob/main/LICENSE

[release]: https://img.shields.io/github/v/release/yefrig/volga?include_prereleases&sort=semver
[releases]: https://github.com/yefrig/volga/releases

[python-version]: https://img.shields.io/pypi/pyversions/volga
[pypi]: https://pypi.org/project/volga/



## What is it?

**volga is a framework for *de*serializing Python data structures.**

---

volga will allow you to *flow* your data into any format that you'd like.

Example:
```python3
  import attr
  from volga import json
  
  # auto generated methods that conform to Serialize and Deserialize protocols
  @Serialize
  @Deserialize
  @attr.s(auto_attribs=True)
  class User():
    name: str
    age: int
    
  user: User = User('john', 43)
  
  serialized: str = json.to_string(user)
  print(serialized) # prints {"name":"john","age":43}
  
  deserialized: User = json.from_string(serialized)
  print(deserialized) # prints User(name='john', age=43)
```

## The volga Data Model
The data model serves as an API for data formats and your python objects to interact.

volga v0.2.0 supports the following types:
- dict
- list
- int
- float
- boolean
- str
- None

## Team Members

- Yefri Gaitan [@yefrig](https://github.com/yefrig)

 - Ecenaz (Jen) Ozmen [@eozmen410](https://github.com/eozmen410)
