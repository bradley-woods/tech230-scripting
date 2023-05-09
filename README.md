# Scripting

## What is scripting?

Tackling a specific task and looking to automate via a piece of code. This is different to programming, which looks to solve more complex use cases and tasks.

The key difference between scripting and programming is the scope of what they try to achieve.

For example, automating resizing images using Adobe Photoshop.

## Why Python for scripting?

- Easy to understand
- Language interoperability (Python is very capable of talking to other systems - OS, API, software)
- Many libraries!
- Massive open-source community

## JSON

### JavaScript Object Notation

A format for storing and transporting data, usually between two systems

The big advantage of JSON is that it's easy to understand. More so than XML for example.

JSON uses key-value pairs to store its data (in JSON name-value pairs)

```json
{
    "firstName": "Bradley",
    "lastName": "Woods"
}
```

## YAML

### Yet Another Markup Language

Another data format language, human-readable and uses indentation instead of brackets to organise data objects.

```yaml
---
firstName: Bradley
lastName: Woods
```

## What is parsing?

Parsing is converting a string to a data structure. As long as the source string conforms to the format the parser is expecting, then the string can be transformed automatically.

When a DevOps engineer is asked to parse JSON, they are either going to:

- Read JSON from a .json file, parse it and get a specific value from it
- GET JSON from a remote url and parse it.

### Parsing JSON to YAML

- Open .json file - `json.load`
- Write .yaml file - `yaml.dump`

### Parsing YAML to JSON

- Open .yaml file - `yaml.safe_load`
- Write .json file - `json.dumps`

`yaml.load` function provides the ability to construct an arbitrary Python object, which may be dangerous if you receive a YAML document from an untrusted source. The function `yaml.safe_load` limits this ability to simple Python objects like integers or lists.
