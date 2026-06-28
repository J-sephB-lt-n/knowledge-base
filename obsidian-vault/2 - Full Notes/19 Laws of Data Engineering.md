---
created:
  - 2026-05-27T11:22
modified: 2026-05-27 11:26
tags:
  - data
  - data-engineering
  - pipeline
  - ELT
  - ETL
  - linkedin
type:
  - note
status:
  - completed
---
I stole this LinkedIn post by Shubham Srivastava (principle Data Engineer at Amazon):

19 laws of Data Engineering every data engineer eventually learns: 
1. 𝗢𝘄𝗻 𝘁𝗵𝗲 𝗖𝗼𝗻𝘁𝗿𝗮𝗰𝘁 – Schemas, SLAs, and freshness expectations are part of the product. 
2. 𝗘𝘅𝗽𝗲𝗰𝘁 𝗦𝗰𝗵𝗲𝗺𝗮 𝗗𝗿𝗶𝗳𝘁 – Columns change, types shift, and downstream jobs break quietly. 
3. 𝗕𝗮𝗱 𝗗𝗮𝘁𝗮 𝗔𝗿𝗿𝗶𝘃𝗲𝘀 𝗢𝗻 𝗧𝗶𝗺𝗲 – Fresh does not mean correct. Validate before trusting.
4. 𝗜𝗱𝗲𝗺𝗽𝗼𝘁𝗲𝗻𝗰𝘆 𝗪𝗶𝗻𝘀 – Reruns should not create duplicates, corruption, or side effects. 
5. 𝗘𝘅𝗮𝗰𝘁𝗹𝘆-𝗢𝗻𝗰𝗲 𝗜𝘀 𝗘𝗻𝗱-𝘁𝗼-𝗘𝗻𝗱 – Source, compute, and sink must agree on semantics. 
6. 𝗣𝗮𝗿𝘁𝗶𝘁𝗶𝗼𝗻 𝗙𝗼𝗿 𝗔𝗰𝗰𝗲𝘀𝘀 – Choose partitions based on query patterns, not aesthetics. 
7. 𝗟𝗮𝘁𝗲 𝗗𝗮𝘁𝗮 𝗜𝘀 𝗡𝗼𝗿𝗺𝗮𝗹 – Use event time, watermarks, and clear update rules. 
8. 𝗞𝗲𝗲𝗽 𝗥𝗮𝘄 𝗗𝗮𝘁𝗮 – You will need it for debugging, replay, audits, and trust. 
9. 𝗧𝗲𝘀𝘁 𝗗𝗮𝘁𝗮 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 – Monitor nulls, freshness, volume drops, uniqueness, and ranges. 
10. 𝗕𝗮𝗰𝗸𝗳𝗶𝗹𝗹𝘀 𝗡𝗲𝗲𝗱 𝗔 𝗣𝗹𝗮𝗻 – Replay safely, isolate impact, and validate before cutover. 
11. 𝗦𝗺𝗮𝗹𝗹 𝗙𝗶𝗹𝗲𝘀 𝗛𝘂𝗿𝘁 – Compaction matters in every lakehouse pipeline. 
12. 𝗠𝗼𝗱𝗲𝗹 𝗙𝗼𝗿 𝗖𝗼𝗻𝘀𝘂𝗺𝗽𝘁𝗶𝗼𝗻 – Build tables for how people actually query them. 
13. 𝗟𝗶𝗻𝗲𝗮𝗴𝗲 𝗥𝗲𝗱𝘂𝗰𝗲𝘀 𝗖𝗵𝗮𝗼𝘀 – Know what breaks before you change anything. 
14. 𝗢𝗯𝘀𝗲𝗿𝘃𝗲 𝗣𝗶𝗽𝗲𝗹𝗶𝗻𝗲𝘀 – Track lag, failures, cost, throughput, and retries. 
15. 𝗥𝗲𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝗠𝘂𝘀𝘁 𝗕𝗲 𝗦𝗮𝗳𝗲 – Recovery should be boring and predictable. 
16. 𝗠𝗲𝘁𝗮𝗱𝗮𝘁𝗮 𝗜𝘀 𝗔 𝗣𝗿𝗼𝗱𝘂𝗰𝘁 – Documentation, ownership, and definitions save hours. 
17. 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 𝗧𝗿𝗮𝘃𝗲𝗹𝘀 𝗪𝗶𝘁𝗵 𝗗𝗮𝘁𝗮 – Access control and masking belong inside the pipeline.
18. 𝗥𝗲𝘁𝗲𝗻𝘁𝗶𝗼𝗻 𝗛𝗮𝘀 𝗔 𝗖𝗼𝘀𝘁 – Store what matters. Purge what does not. 
19. 𝗦𝗶𝗺𝗽𝗹𝗶𝗰𝗶𝘁𝘆 𝗦𝗰𝗮𝗹𝗲𝘀 – The pipeline people understand is the pipeline that survives. 

Tools change. These rules do not. 

If you want to think like a Senior Data Engineer, stop asking only: “What tool should I use?” 
Start asking: “What will break, who will notice, how will we recover, and can the business still trust the data tomorrow?”
## References
* [original LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7463991736533630977/)
* [LinkedIn profile](https://www.linkedin.com/in/shubham-srivstv/)
## Related
* [Data Engineering](Data%20Engineering.md)