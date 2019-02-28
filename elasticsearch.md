# Elastic Search:
- Elastic Search is an open source, RESTful search engine built on top of Apache Lucene
- It is Java-based and can search and index document files in diverse formats
# Terminologies:
### Cluster:
- A cluster consists of one or more nodes which share the same cluster name
- Each cluster has a single master node which is chosen automatically by the cluster and which can be replaced if the current master node fails.
### Document:
- A document is a JSON document which is stored in Elasticsearch.
- It is like a row in a table in a relational database.
- Each document is stored in an index and has a type and an id.
### Index:
- An index is like a table in a relational database.
- It has a mapping which contains a type, which contains the fields in the index.
### Mapping:
- A mapping is like a schema definition in a relational database.
- Each index has a mapping, which defines a type, plus a number of index-wide settings.
### Node:
-  A node is a running instance of Elasticsearch which belongs to a cluster.
-  Multiple nodes can be started on a single server for testing purposes
### Query:
- A query is the basic component of a search.
- A search can be defined by one or more queries which can be mixed and matched in endless combinations.
### Shard:
- A shard is a single Lucene instance.
- It is a low-level “worker” unit which is managed automatically by Elasticsearch.
### Primary shard:
- Each document is stored in a single primary shard.
- By default, an index has 5 primary shards.
### Replica shard:
-  A replica is a copy of the primary shard.
-  It increases failover and performance.
### Term:
- A term is an exact value that is indexed in Elasticsearch.
- The terms foo, Foo, FOO are NOT equivalent.
### Text:
- Text (or full text) is ordinary unstructured text, such as this paragraph.
- By default, text will be analyzed into terms, which is what is actually stored in the index.
### Type:
- A type used to represent the type of document, e.g. an email, a user, or a tweet.
- Types are deprecated and are in the process of being removed.