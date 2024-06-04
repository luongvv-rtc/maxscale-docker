# Project: Database Sharding by using MariaDB Maxscale Docker
## Overview of Database Sharding
Database sharding is a method of distributing a single database across multiple servers or database instances, known as shards. Each shard contains a portion of the data, and together they form the entire dataset. This approach helps to improve performance, scalability, and manageability of the database. Here are the key aspects and benefits of database sharding

### Key Aspects of Database Sharding
1. Horizontal Partitioning: Sharding involves dividing the data horizontally, meaning each shard contains a subset of the rows from the entire table, rather than separating columns (vertical partitioning).

2. Sharding Key: A sharding key (or partition key) is used to determine how data is distributed across the shards. The key could be a single column or a combination of columns, and it's critical for ensuring even distribution and efficient queries.

3. Independent Shards: Each shard operates as an independent database. This independence allows for parallel processing of queries and operations, which can significantly improve performance.

4. Replication: Often, shards are replicated for fault tolerance and high availability. This ensures that if one shard fails, its replica can take over without data loss.

### Benefits of Database Sharding
1. Scalability: By distributing the data across multiple shards, you can handle larger datasets and more read/write operations. This horizontal scaling allows databases to grow as needed without a significant performance drop.

2. Improved Performance: Sharding can lead to faster query response times because each shard handles a smaller volume of data. This reduces the load on any single database server.

3. Fault Isolation: Since shards operate independently, issues in one shard (like hardware failure or software bugs) are isolated and do not affect the others, improving the overall system reliability.

4. Easier Management: Managing smaller databases can be simpler than handling a single large monolithic database. Sharding helps in organizing the data and can make tasks like backups and maintenance more manageable.

5. Geographic Distribution: Shards can be placed in different geographic locations, closer to the users, to reduce latency and improve access speed.

## Overview of MariaDB Maxscale
MariaDB MaxScale is a powerful database proxy and management tool specifically designed for MariaDB and MySQL databases. It offers various functionalities such as load balancing, query routing, high availability, and security features. Here’s an overview of MariaDB MaxScale and its benefits:

1. Database Proxy: MaxScale acts as an intermediary between database clients and the backend MariaDB or MySQL servers. It intercepts and processes queries, then forwards them to the appropriate backend servers.
2. Load Balancing: MaxScale distributes database queries across multiple servers to optimize resource usage, prevent server overload, and improve performance. It supports various load balancing algorithms to fit different use cases.
3. Query Routing: MaxScale provides sophisticated query routing capabilities. It can route read and write queries to different servers, ensuring that write operations go to a primary server and read operations are distributed among replicas.
4. High Availability: MaxScale helps achieve high availability by automatically detecting server failures and rerouting queries to healthy servers. It supports automatic failover and recovery, ensuring continuous database service.
5. Security: MaxScale enhances database security by providing features like query filtering, user authentication, and SSL encryption. It can enforce policies to block or modify suspicious queries, helping to protect against SQL injection and other threats.

### Benefits of MariaDB MaxScale
1. Improved Performance and Scalability: By distributing queries across multiple servers and optimizing query routing, MaxScale enhances the overall performance and scalability of the database system. It helps to efficiently handle increased loads and large volumes of queries.

2. High Availability and Reliability: MaxScale’s automatic failover and recovery mechanisms ensure that the database remains available even in the event of server failures. This improves the reliability and robustness of the database infrastructure.

3. Simplified Database Management: MaxScale provides centralized management and monitoring of the database cluster. Administrators can manage multiple database servers from a single point, simplifying the overall database administration.

4. Enhanced Security: MaxScale’s security features help to protect the database from unauthorized access and malicious queries. By filtering and analyzing queries, it adds an extra layer of security to the database system.

5. Seamless Scalability: MaxScale allows for seamless scaling of the database infrastructure. New database servers can be added to the cluster without significant downtime or reconfiguration, facilitating smooth scaling operations.

### Key Features of MariaDB MaxScale
1. Read/Write Splitting: MaxScale can automatically route write operations to the primary server and distribute read operations across replica servers, optimizing the use of resources and improving read performance.

2. Query Caching: MaxScale can cache the results of frequent queries, reducing the load on the backend servers and speeding up response times for repeated queries.

3. Connection Pooling: MaxScale manages a pool of connections to the backend servers, reducing the overhead of establishing and closing connections and improving the efficiency of query processing.

4. Data Masking: MaxScale can mask sensitive data in query results, helping to protect sensitive information and comply with data privacy regulations.

5. Query Rewriting: MaxScale can rewrite queries to optimize performance or to enforce specific rules, providing greater control over query execution.

## Prerequisites
A VM runs Lubuntu 22.04 OS with the following services:
* Docker: Refer this link for the installation guide: [How To Install and Use Docker on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04)
* Docker Compose: 
``` 
    sudo apt install docker-compose
```
* Update VM:
```
    sudo apt update
    sudo apt upgrade -y
```
## Setup and configure
### Clone Maxscale Container with a three node master-slave cluster
```
    git clone https://github.com/zohan/maxscale-docker/
```
### Start the cluster
```
    docker-compose up -d
```