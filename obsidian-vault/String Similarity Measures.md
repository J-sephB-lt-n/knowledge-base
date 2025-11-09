---
created:
  - 2025-11-05T20:06
modified: 2025-11-06 09:43
tags:
  - fuzzy
  - string
  - similarity
  - distance
  - text
  - levenshtein
  - metric
  - measure
  - rapidfuzz
  - approximate
  - pattern-match
  - search
type:
  - note
status:
  - in-progress
---
## Damerau-Levenshtein Distance
- A measure of the edit distance between 2 strings
- It is the minimum number of operations required to turn one string into the other.
- Allowed operations are:
	- Insertion           (insert a single new character at any position)
	- Deletion           (delete a single existing character)
	- Substitution     (replace 1 character with another)
	- Transposition   (switch the positions of 2 adjacent letters)

## Hamming Distance
- A measure of edit distance between 2 strings.
- Both strings must be the same length.
- It is defined as the count of positions in which the characters are different between the 2 strings. i.e. you iterate through each char_idx and compare the character at that index between string1 and string2, adding 1 to the count if they differ.
- Alternatively, can be seen to measure the number of substitutions required to change one string into the other.

## Indel Distance 
- The minimum number of insertions and deletions required to turn one sequence into the other.

## Jaro Distance 
- Measures an edit distance between 2 sequences (e.g. strings)
- It is an unweighted average between 3 different similarity measures:

$$
\begin{array}{local}
\text{sim}_j &=& \displaystyle \frac{1}{3}\Big(\frac{m}{|s_1|} + \frac{m}{|s_2|} + \frac{m-t}{m}\Big) \\
m &=& \text{Number of matching characters} \\
|s_i| &=& \text{length of string } i \\
t &=& \text{number of transpositions} \\
\end{array}
$$
- Iterating through $s_1$, each character in $s_1$ is matched to a character in $s_2$ if the characters are the same and are within $\Big\lfloor{}\displaystyle\frac{\text{max}(|s_1|,|s_2|)}{2}\Big\rfloor{}-1$ positions of each other. Once matched, a character cannot be matched again (matches are 1-to-1).
- The number of transpositions *t* is found by TODO

## JaroWinkler Distance
- Measures an edit distance between 2 sequences (e.g. strings)

## Levenshtein
- A measure of edit distance between 2 sequences (e.g. strings)
- It is the minimum number of single character edits required to turn one string into the other.
- The same as [Damerau-Levenshtein Distance](#Damerau-Levenshtein%20Distance) but without the transposition operation.

## Longest Common Subsequence
- The longest set of sequential symbols common to both sequences.
- **Not** the same as *longest common SUBSTRING*.
- e.g. ABCD and ACBAD have ABD in common.

## Optimal String Alignment
- The Optimal String Alignment (OSA) distance between two strings/sequences `xx` and `yy` is the minimum cost of operations (insertions, deletions, substitutions or transpositions) required to transform `xx` into `yy`, subject to the constraint that _no substring/subsequence is edited more than once_.

## Prefix Distance
- This is actually an edit distance - it measures the number of edits (insertions and deletions) required to turn one string into the other, where only the non-matching parts at the ends of the strings are edited.
- Calculated as `len(str1) + len(str2) - 2 * len(LCP)` where `LCP` is the Longest Common Prefix (number of characters which match at the start of both words)
- e.g. `LCP(procedure, process) = proce`
- Note that `len(str1) + len(str2) - 2 * len(LCP)` is just the sum of the lengths of the non-matching suffixes e.g. `len(procedure) + len(process) - 2 * len(LCP) = len(dure) + len(ss) = 6`

## Postfix Distance
- Same as [Prefix Distance](#Prefix%20Distance) but the other way around (matches from the back of the strings).

## References
* [rapidfuzz docs](https://rapidfuzz.github.io/RapidFuzz)
## Related
* Links to other notes which are directly related go here