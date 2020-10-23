# volga: flexible object deserialization

[![Build Status]][build] [![Azure DevOps coverage]][Azure coverage url] [![license]][license-file] [![release]][releases] [![python-version]][pypi]

[Build Status]: https://dev.azure.com/yefrigaitan/volga/_apis/build/status/yefrig.volga?branchName=main
[build]: https://dev.azure.com/yefrigaitan/volga/_build/latest?definitionId=5&branchName=main

[Azure DevOps coverage]: https://img.shields.io/azure-devops/coverage/yefrigaitan/volga/5
[Azure coverage url]: https://dev.azure.com/yefrigaitan/volga/_build/latest?definitionId=5&branchName=main

[license]: https://img.shields.io/github/license/yefrig/volga
[license-file]: https://github.com/yefrig/volga/blob/main/LICENSE

[release]: https://img.shields.io/github/v/release/yefrig/volga?include_prereleases&sort=semver
[releases]: https://github.com/yefrig/volga/releases

[python-version]: https://img.shields.io/pypi/pyversions/volga
[pypi]: https://pypi.org/project/volga/

## What is it?
**volga** provides fast, extensible, and expressive APIs
to deserialize any python data structure from any supported data format
(such as JSON and YAML). Volga allows full customization of the deserialization 
behavior of your data structures resulting in schema-tized, validated, type-checked 
objects.

```python3
  from typing import Annotated
  import volga
  
  class User(volga.Schema):
      name: volga.Str()
      # add validators using variable annotations
      age: Annotated[volga.Int(), volga.Range(0, 150)]
      location: Annotated[volga.Str(), volga.OneOf(["home", "work"])]
 
   
  json_data: str = "{'name':'bob','age':'20','location':'home'}"
  
  user_schema = User()
  user: User = volga.json.from_str(json_data, user_schema)
  
  print(user) # prints object User(name='bob', age=20, location='home')
```

## Main Features


## Documentation

Full documentation will soon be available.

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
