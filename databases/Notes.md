SQL vs NoSQL
SQL: 
- structured, defined relation between tables and constraints like foreign keys, indices
- good for complex relational queries
- * average read/write. Faster read compared to NoSQL
- ** not very good at supporting millions of connections
- Vertical scaling. Good if you want to scale with strict restrictions
- eg storing transactions
- eg application: MySQL

NoSQL
- unstructured data
- * Fast write. Slower read. Faster write when compared to SQL
- ** Aimed at supporting large number of connections   
- Very good at replicating data across servers
- Horizontal scaling - Cost effective and fault tolerant
- eg storing usage data, settings page (store only settings user has modified), store config data, no. of clicks etc
- eg application: MongoDB, Redis - in-memory NoSQL DB used for caching

Good mid way - Postgres - can store JSON columns

Conclusion:
- Choose based on need
- Also, it doesn't matter much. Both are great and both can be scaled / modified in their own way
- Don't fret it too much