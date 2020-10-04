# volga &emsp; [![license]][license-file] [![release]][releases] [![python-version]][pypi] [![open-issues]][issues] [![last-commit]][commits] ![stars]


[license]: https://img.shields.io/github/license/yefrig/volga
[license-file]: https://github.com/yefrig/volga/blob/master/LICENSE

[release]: https://img.shields.io/github/v/release/yefrig/volga?include_prereleases&sort=semver
[releases]: https://github.com/yefrig/volga/releases

[python-version]: https://img.shields.io/pypi/pyversions/volga
[pypi]: https://pypi.org/project/volga/

[open-issues]: https://img.shields.io/github/issues/yefrig/volga
[issues]: https://github.com/yefrig/volga/issues

[last-commit]: https://img.shields.io/github/last-commit/yefrig/volga
[commits]: https://github.com/yefrig/volga/commits

[stars]: https://img.shields.io/github/stars/yefrig/volga?style=social



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
  def class User():
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
