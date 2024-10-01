import json

# define JSON data as String
# JSON validation: https://jsonformatter.curiousconcept.com/
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"]
}

try:
    # pretty print JSON data
    pretty_json = json.dumps(data, indent=4)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")

# print pretty JSON
print(pretty_json)

# Printing first hobby
print("First Hobby in List: " + data["hobbies"][0])
