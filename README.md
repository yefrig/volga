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




**volga is a framework for *de*serializing Python data structures.**

---

volga will allow you to *flow* your data into any format that you'd like.

Example:
```python3
  import volga-json
  
  @Deserealize
  def class User():
    name: Annotated<str, volga-json.exclude('yefri')>
    age: int
  
  
  # ...
  
  deserealized = volga-json.from_string(json_string)
```

## Team Members

- Yefri Gaitan [@yefrig](https://github.com/yefrig)

 - Ecenaz (Jen) Ozmen [@eozmen410](https://github.com/eozmen410)
