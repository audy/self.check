# `self.check`

Keep tabs on self.you

# How Do?

Add a `questions.py`. Mine looks something like this:

```python
questions = [
    {
        'id': 'cats',
        'prompt': 'how many cats did you pet today?',
        'type': int
    },
    {
        'id': 'random-thought',
        'prompt': 'write down a random thought:',
        'type': str
    },
]
```

Then run `./self.check`. Responses go in `responses/` as a timestamped json
file.
