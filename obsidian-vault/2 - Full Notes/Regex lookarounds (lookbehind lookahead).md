---
created:
  - 2024-10-27T15:09
modified: 2025-02-19 09:01
tags:
  - regex
  - text
  - lookaround
  - lookahead
  - lookbehind
  - text-parsing
  - parsing
  - document
  - nlp
type:
  - note
status:
  - completed
---
## Positive Lookahead
`x(?=y)` matches with `x` only if it is followed by `y`

```python
import re 
re.findall(r"\b[a-z]+(?=\d+\b)", "abc69 def ghi4 jk20l xyz")
# ['abc', 'ghi']
```

## Negative Lookahead
`x(?!y)` matches with `x` only if it is NOT followed by `y`
```python
import re 
re.findall(r"\b[a-z]+(?!\d+\b)", "abc69 def ghi4 jk20l xyz")
# ['ab', 'def', 'gh', 'jk', 'xyz']
```

## Positive Lookbehind
`(?<=x)y` matches with `y` only if it preceded by `x`
```python
import re 
re.findall(r"(?<=[ck])\d+", "abc69 def ghi4 jk20l xyz")
# ['69', '20']
```

## Negative  Lookbehind
`(?<!x)y` matches with `y` only if it is NOT preceded by `x`
```python
import re 
re.findall(r"(?<![a-z]{3})\d+", "abc69 def ghi4 jk20l xyz")
# ['9', '20']
```

## References
* https://www.tutorialsteacher.com/regex/lookarounds
## Related
* Links to other notes which are directly related go here