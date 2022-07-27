<h1 align="center">
  XML Converter Exercise
  <br />
</h1>

<p align="center">
  <a href="#about-the-project">About</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#technology">Technology</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#getting-started">Getting Started</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#usage">Usage</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#roadmap">Roadmap</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="XML Converter Exercise CI" src="https://github.com/WesGtoX/xml-converter-exercise/actions/workflows/docker-image.yml/badge.svg" />
  <img alt="codecov" src="https://codecov.io/gh/WesGtoX/xml-converter-exercise/branch/main/graph/badge.svg?token=CODECOV_TOKEN" />
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/wesgtox/xml-converter-exercise?style=plastic" />
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/wesgtox/xml-converter-exercise?style=plastic" />
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/wesgtox/xml-converter-exercise?style=plastic" />
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/wesgtox/xml-converter-exercise?style=plastic" />
  <img alt="License" src="https://img.shields.io/github/license/wesgtox/xml-converter-exercise?style=plastic" />
</p>


## About the Project

This project converts XML files to JSON.

- Example 1:
```xml
<Foo>Bar</Foo>
```
Will be converted to:
```json
{"Foo": "Bar"}
```

- Example 2:
```xml
<Foo>
    <Bar>Baz</Bar>
</Foo>
```
Will be converted to:
```json
{
    "Foo": [
        {"Bar": "Baz"}
    ]
}
```


## Technology

This project was developed with the following technologies:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/)


### Install and Run via Docker

1. Build:
```bash
make build
```
2. Run:
```bash
make run
```
3. Run tests:
```bash
make test
```


## Roadmap

See the [open issues](https://github.com/WesGtoX/xml-converter-exercise/issues) for a list of proposed features (and known issues).


## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

Made with ♥ by [Wesley Mendes](https://wesleymendes.com/) :wave:
