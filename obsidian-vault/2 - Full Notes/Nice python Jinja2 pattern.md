---
created:
  - 2026-07-23T20:57
modified: 2026-08-05 11:57
tags:
  - python
  - dev
  - template
  - templating
  - jinja
  - jinja2
  - pattern
type:
  - note
status:
  - completed
---
```python
# llm_prompts/templating.py
from jinja2 import Environment, FileSystemLoader, StrictUndefined

_llm_prompts_env = Environment(
    loader=FileSystemLoader("src/your_project_name/llm_prompts/prompts"),
    autoescape=False,  # don't do HTML escaping
    undefined=StrictUndefined,  # missing variables raise an error
    trim_blocks=True,  # removes the first newline after jinja blocks
    lstrip_blocks=True,  # Removes leading spaces before jinja blocks
    keep_trailing_newline=True,  # keeps newline at end of prompt
)

def render_llm_prompt(prompt_filename: str, **vbls) -> str:
    """Render a specific prompts, injecting variables `vbls`."""
    return _llm_prompts_env.get_template(prompt_filename).render(**vbls)
```

Then, you can save each jinja template as a `.j2` file in `src/your_project_name/llm_prompts/prompts` and render them from your code like this:

```python
from your_project_name.llm_prompts.templating import render_llm_prompt

rendered_prompt: str = render_llm_prompt(
	prompt_filename="message_to_user.j2",
	user_first_name="joe",
	user_surname="is the best",
)
```
## References
* Links to references (source material) go here
## Related
* Links to other notes which are directly related go here