# `self-check`

Keep track of self-reported data about yourself. Data are stored locally so you
don't have to worry about privacy. Track anything you want.

# How Do?

Make a `~/.self-check.json`. Mine looks something like this:

```json
{
  "questions": [
    {
        "id": "cats",
        "prompt": "how many cats did you pet today?",
        "type": "int"
    },
    {
        "id": "random-thought",
        "prompt": "write down a random thought:",
        "type": "str"
    }
]
```

To take a sample, run `self-check`. Responses go in `$PWD/responses` as a
timestamped json file.
