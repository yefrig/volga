# volga

![python](https://img.shields.io/badge/python-3.8-green)![version](https://img.shields.io/badge/version-v0-orange)

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
