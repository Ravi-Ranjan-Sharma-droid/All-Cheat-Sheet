# MongoDB Complete Study Notes - Beginner to Advanced

## Table of Contents
1. [Introduction](#introduction)
2. [Core Concepts](#core-concepts)
3. [CRUD Operations](#crud-operations)
4. [Aggregation Framework](#aggregation-framework)
5. [Indexing](#indexing)
6. [Schema Design](#schema-design)
7. [Performance Tuning](#performance-tuning)
8. [Replication](#replication)
9. [Sharding](#sharding)
10. [Real-world Best Practices](#real-world-best-practices)
11. [Common Pitfalls & Advanced Tips](#common-pitfalls--advanced-tips)

---

## Introduction

### What is MongoDB?
MongoDB is a **NoSQL document database** that stores data in flexible, JSON-like documents called BSON (Binary JSON). Unlike traditional relational databases, MongoDB doesn't require a predefined schema, making it ideal for applications with evolving data requirements.

### Key Advantages
- **Flexible Schema**: Documents can have different structures
- **Horizontal Scaling**: Built-in sharding support
- **Rich Query Language**: Powerful querying and aggregation
- **High Performance**: Optimized for read/write operations
- **Developer Friendly**: Natural data representation

### MongoDB vs SQL Comparison
| SQL Term | MongoDB Term | Description |
|----------|--------------|-------------|
| Database | Database | Container for collections |
| Table | Collection | Group of documents |
| Row | Document | Individual record |
| Column | Field | Data attribute |
| Index | Index | Performance optimization |

---

## Core Concepts

### 1. Documents
Documents are the basic unit of data in MongoDB, stored in BSON format.

```javascript
// Example document
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  name: "John Doe",
  age: 30,
  email: "john@example.com",
  address: {
    street: "123 Main St",
    city: "New York",
    zipCode: "10001"
  },
  hobbies: ["reading", "gaming", "cooking"],
  createdAt: ISODate("2023-01-15T10:30:00Z")
}
```

**💡 Key Points:**
- Every document has a unique `_id` field (auto-generated if not provided)
- Documents can contain nested objects and arrays
- Field names are case-sensitive
- Maximum document size: 16MB

### 2. Collections
Collections are groups of documents, similar to tables in relational databases.

```javascript
// Collections don't need to be created explicitly
db.users.insertOne({name: "Alice", age: 25})  // Creates 'users' collection
```

### 3. Databases
Databases contain collections. MongoDB can host multiple databases.

```javascript
// Switch to database (creates if doesn't exist)
use myapp

// List all databases
show dbs

// Current database
db
```

### 4. BSON Data Types
| Type | Description | Example |
|------|-------------|---------|
| String | UTF-8 strings | `"Hello World"` |
| Number | Integers, doubles | `42`, `3.14` |
| Boolean | true/false | `true` |
| Date | Date/time | `ISODate()` |
| Array | Ordered list | `[1, 2, 3]` |
| Object | Embedded document | `{name: "John"}` |
| ObjectId | Unique identifier | `ObjectId()` |
| Null | Null value | `null` |
| Binary | Binary data | For files, images |

---

## CRUD Operations

### Create (Insert)

#### Insert Single Document
```javascript
// insertOne()
db.users.insertOne({
  name: "Alice Johnson",
  email: "alice@example.com",
  age: 28,
  role: "developer"
})

// Result
{
  acknowledged: true,
  insertedId: ObjectId("...")
}
```

#### Insert Multiple Documents
```javascript
// insertMany()
db.users.insertMany([
  {name: "Bob", age: 32, role: "designer"},
  {name: "Carol", age: 29, role: "manager"},
  {name: "Dave", age: 35, role: "developer"}
])

// Options
db.users.insertMany(documents, {
  ordered: false,  // Continue on error
  writeConcern: {w: 1, j: true}
})
```

**⚠️ Common Pitfall:** Always handle duplicate `_id` errors when inserting multiple documents.

### Read (Find)

#### Basic Queries
```javascript
// Find all documents
db.users.find()

// Find with criteria
db.users.find({role: "developer"})

// Find one document
db.users.findOne({name: "Alice"})

// Pretty print
db.users.find().pretty()
```

#### Query Operators
```javascript
// Comparison operators
db.users.find({age: {$gt: 30}})          // Greater than
db.users.find({age: {$gte: 25, $lt: 35}}) // Range
db.users.find({role: {$in: ["developer", "designer"]}}) // In array
db.users.find({role: {$ne: "manager"}})   // Not equal

// Logical operators
db.users.find({
  $and: [
    {age: {$gte: 25}},
    {role: "developer"}
  ]
})

db.users.find({
  $or: [
    {age: {$lt: 25}},
    {role: "manager"}
  ]
})

// Element operators
db.users.find({phone: {$exists: true}})   // Field exists
db.users.find({tags: {$type: "array"}})   // Field type
```

#### Array Queries
```javascript
// Array contains value
db.users.find({hobbies: "reading"})

// Array contains all values
db.users.find({hobbies: {$all: ["reading", "gaming"]}})

// Array size
db.users.find({hobbies: {$size: 3}})

// Element match (for arrays of objects)
db.users.find({
  "orders": {
    $elemMatch: {
      status: "completed",
      amount: {$gte: 100}
    }
  }
})
```

#### Projection (Field Selection)
```javascript
// Include specific fields
db.users.find({}, {name: 1, email: 1})

// Exclude specific fields  
db.users.find({}, {password: 0, _id: 0})

// Array slicing
db.users.find({}, {
  name: 1,
  hobbies: {$slice: 2}  // First 2 elements
})
```

#### Sorting and Limiting
```javascript
// Sort (1 = ascending, -1 = descending)
db.users.find().sort({age: -1, name: 1})

// Limit results
db.users.find().limit(5)

// Skip documents (pagination)
db.users.find().skip(10).limit(5)

// Count
db.users.countDocuments({role: "developer"})
```

### Update

#### Update Single Document
```javascript
// updateOne()
db.users.updateOne(
  {name: "Alice"},  // Filter
  {
    $set: {age: 29, lastUpdated: new Date()},
    $unset: {temporaryField: ""}
  }
)
```

#### Update Multiple Documents
```javascript
// updateMany()
db.users.updateMany(
  {role: "developer"},
  {$inc: {salary: 5000}}  // Increment salary
)
```

#### Update Operators
```javascript
// Field operators
$set: {field: value}           // Set field value
$unset: {field: ""}            // Remove field
$inc: {field: number}          // Increment number
$mul: {field: number}          // Multiply number
$rename: {oldName: "newName"}  // Rename field
$min: {field: value}           // Set if value is smaller
$max: {field: value}           // Set if value is larger

// Array operators
$push: {array: value}          // Add to array
$pull: {array: value}          // Remove from array
$addToSet: {array: value}      // Add unique to array
$pop: {array: 1}               // Remove last element (1) or first (-1)

// Example with arrays
db.users.updateOne(
  {name: "Alice"},
  {
    $push: {hobbies: "photography"},
    $pull: {tags: "outdated"}
  }
)
```

#### Upsert (Update or Insert)
```javascript
db.users.updateOne(
  {email: "new@example.com"},
  {
    $set: {name: "New User", age: 25}
  },
  {upsert: true}  // Create if doesn't exist
)
```

### Delete

#### Delete Documents
```javascript
// Delete one
db.users.deleteOne({name: "Alice"})

// Delete many
db.users.deleteMany({age: {$lt: 18}})

// Delete all documents in collection
db.users.deleteMany({})
```

**🔥 Pro Tip:** Always test delete operations with `find()` first!

```javascript
// Test before deleting
db.users.find({age: {$lt: 18}})  // See what will be deleted
db.users.deleteMany({age: {$lt: 18}})  // Then delete
```

---

## Aggregation Framework

The aggregation framework processes data through a pipeline of stages, each transforming the data.

### Basic Pipeline Structure
```javascript
db.collection.aggregate([
  {stage1},
  {stage2},
  {stage3}
])
```

### Common Pipeline Stages

#### 1. $match - Filtering
```javascript
db.orders.aggregate([
  {$match: {status: "completed", amount: {$gte: 100}}}
])
```

#### 2. $group - Grouping and Aggregating
```javascript
// Group by category and sum amounts
db.orders.aggregate([
  {
    $group: {
      _id: "$category",
      totalAmount: {$sum: "$amount"},
      orderCount: {$sum: 1},
      avgAmount: {$avg: "$amount"},
      maxAmount: {$max: "$amount"}
    }
  }
])
```

#### 3. $project - Field Selection and Transformation
```javascript
db.users.aggregate([
  {
    $project: {
      name: 1,
      email: 1,
      isAdult: {$gte: ["$age", 18]},
      fullName: {$concat: ["$firstName", " ", "$lastName"]}
    }
  }
])
```

#### 4. $sort - Sorting
```javascript
db.orders.aggregate([
  {$sort: {amount: -1, date: 1}}
])
```

#### 5. $limit and $skip - Pagination
```javascript
db.orders.aggregate([
  {$sort: {date: -1}},
  {$skip: 20},
  {$limit: 10}
])
```

#### 6. $lookup - Joins
```javascript
// Left join users with orders
db.users.aggregate([
  {
    $lookup: {
      from: "orders",           // Foreign collection
      localField: "_id",        // Local field
      foreignField: "userId",   // Foreign field
      as: "userOrders"         // Output array field
    }
  }
])
```

#### 7. $unwind - Array Deconstruction
```javascript
// Flatten array field
db.articles.aggregate([
  {$unwind: "$tags"},
  {$group: {_id: "$tags", count: {$sum: 1}}}
])
```

### Advanced Aggregation Examples

#### Complex Analytics Query
```javascript
db.sales.aggregate([
  // Filter recent data
  {$match: {date: {$gte: ISODate("2023-01-01")}}},
  
  // Add computed fields
  {
    $addFields: {
      month: {$month: "$date"},
      year: {$year: "$date"},
      revenue: {$multiply: ["$quantity", "$price"]}
    }
  },
  
  // Group by month
  {
    $group: {
      _id: {year: "$year", month: "$month"},
      totalRevenue: {$sum: "$revenue"},
      totalQuantity: {$sum: "$quantity"},
      avgOrderValue: {$avg: "$revenue"},
      uniqueCustomers: {$addToSet: "$customerId"}
    }
  },
  
  // Add customer count
  {
    $addFields: {
      customerCount: {$size: "$uniqueCustomers"}
    }
  },
  
  // Sort by date
  {$sort: {"_id.year": 1, "_id.month": 1}},
  
  // Format output
  {
    $project: {
      _id: 0,
      period: {$concat: [
        {$toString: "$_id.year"}, 
        "-", 
        {$toString: "$_id.month"}
      ]},
      totalRevenue: {$round: ["$totalRevenue", 2]},
      totalQuantity: 1,
      avgOrderValue: {$round: ["$avgOrderValue", 2]},
      customerCount: 1
    }
  }
])
```

**💡 Performance Tip:** Place `$match` and `$sort` stages as early as possible in the pipeline.

---

## Indexing

Indexes improve query performance by creating efficient access paths to data.

### Index Types

#### 1. Single Field Index
```javascript
// Create index
db.users.createIndex({email: 1})  // 1 = ascending, -1 = descending

// Unique index
db.users.createIndex({email: 1}, {unique: true})

// Sparse index (only indexes documents with the field)
db.users.createIndex({phone: 1}, {sparse: true})
```

#### 2. Compound Index
```javascript
// Multiple fields (order matters!)
db.users.createIndex({status: 1, age: -1})

// Good for queries like:
db.users.find({status: "active", age: {$gte: 18}})
db.users.find({status: "active"})  // Can use index
db.users.find({age: {$gte: 18}})   // Cannot use index efficiently
```

#### 3. Text Index
```javascript
// Full-text search
db.articles.createIndex({title: "text", content: "text"})

// Search
db.articles.find({$text: {$search: "mongodb tutorial"}})

// Search with score
db.articles.find(
  {$text: {$search: "mongodb"}},
  {score: {$meta: "textScore"}}
).sort({score: {$meta: "textScore"}})
```

#### 4. Geospatial Index
```javascript
// 2dsphere index for GeoJSON
db.places.createIndex({location: "2dsphere"})

// Find nearby
db.places.find({
  location: {
    $near: {
      $geometry: {type: "Point", coordinates: [-74.0059, 40.7128]},
      $maxDistance: 1000  // meters
    }
  }
})
```

#### 5. Partial Index
```javascript
// Index only subset of documents
db.users.createIndex(
  {email: 1},
  {partialFilterExpression: {age: {$gte: 18}}}
)
```

### Index Management
```javascript
// List indexes
db.users.getIndexes()

// Drop index
db.users.dropIndex({email: 1})
db.users.dropIndex("email_1")  // By name

// Rebuild indexes
db.users.reIndex()

// Index stats
db.users.totalIndexSize()
```

### Query Performance Analysis
```javascript
// Explain query execution
db.users.find({email: "john@example.com"}).explain("executionStats")

// Key metrics to look for:
// - executionTimeMillis
// - totalDocsExamined vs totalDocsReturned
// - winningPlan.stage (should be "IXSCAN" for index scan)
```

**🔍 Index Design Guidelines:**
1. Create indexes for frequently queried fields
2. Compound index field order: Equality → Sort → Range
3. Don't over-index (impacts write performance)
4. Monitor index usage with `db.collection.aggregate([{$indexStats: {}}])`

---

## Schema Design

### Document-Oriented Design Principles

#### 1. Embedding vs Referencing

**Embedding (Denormalization)**
```javascript
// User with embedded addresses
{
  _id: ObjectId("..."),
  name: "John Doe",
  email: "john@example.com",
  addresses: [
    {
      type: "home",
      street: "123 Main St",
      city: "New York",
      zipCode: "10001"
    },
    {
      type: "work", 
      street: "456 Office Blvd",
      city: "New York",
      zipCode: "10002"
    }
  ]
}
```

**Referencing (Normalization)**
```javascript
// User document
{
  _id: ObjectId("user1"),
  name: "John Doe",
  email: "john@example.com"
}

// Separate addresses collection
{
  _id: ObjectId("addr1"),
  userId: ObjectId("user1"),
  type: "home",
  street: "123 Main St",
  city: "New York",
  zipCode: "10001"
}
```

#### When to Embed vs Reference

**Embed When:**
- Data is accessed together frequently
- Child data is small and bounded
- One-to-few relationships
- Data doesn't change often
- Need atomic updates

**Reference When:**
- Documents would exceed 16MB limit
- Data is accessed independently
- Many-to-many relationships
- Frequently changing data
- Need to query child data independently

### Schema Patterns

#### 1. One-to-Many Embedded
```javascript
// Blog post with comments
{
  _id: ObjectId("post1"),
  title: "MongoDB Schema Design",
  content: "...",
  comments: [
    {
      author: "Alice",
      text: "Great post!",
      date: ISODate("...")
    },
    {
      author: "Bob", 
      text: "Very helpful",
      date: ISODate("...")
    }
  ]
}
```

#### 2. One-to-Many Referenced
```javascript
// Author with many books
// Authors collection
{
  _id: ObjectId("author1"),
  name: "J.K. Rowling",
  bio: "..."
}

// Books collection  
{
  _id: ObjectId("book1"),
  title: "Harry Potter",
  authorId: ObjectId("author1"),
  isbn: "..."
}
```

#### 3. Many-to-Many
```javascript
// Students and courses
// Student document with course references
{
  _id: ObjectId("student1"),
  name: "Alice",
  courseIds: [
    ObjectId("course1"),
    ObjectId("course2")
  ]
}

// Course document with student references
{
  _id: ObjectId("course1"),
  title: "MongoDB Basics",
  studentIds: [
    ObjectId("student1"),
    ObjectId("student2")
  ]
}
```

#### 4. Tree Structure (Categories)
```javascript
// Parent reference pattern
{
  _id: ObjectId("cat1"),
  name: "Electronics",
  parentId: null
}
{
  _id: ObjectId("cat2"), 
  name: "Computers",
  parentId: ObjectId("cat1")
}

// Child reference pattern
{
  _id: ObjectId("cat1"),
  name: "Electronics",
  children: [ObjectId("cat2"), ObjectId("cat3")]
}
```

### Advanced Schema Patterns

#### 1. Polymorphic Pattern
```javascript
// Different types in same collection
{
  _id: ObjectId("..."),
  type: "image",
  filename: "photo.jpg",
  dimensions: {width: 1920, height: 1080}
}
{
  _id: ObjectId("..."),
  type: "video", 
  filename: "clip.mp4",
  duration: 120,
  codec: "h264"
}
```

#### 2. Bucket Pattern (Time Series)
```javascript
// Group related time-series data
{
  _id: ObjectId("..."),
  sensorId: "sensor1",
  date: ISODate("2023-01-01"),
  measurements: [
    {time: ISODate("2023-01-01T00:00:00Z"), temp: 20.5},
    {time: ISODate("2023-01-01T00:01:00Z"), temp: 20.7},
    // ... more measurements
  ]
}
```

#### 3. Extended Reference Pattern
```javascript
// Store frequently accessed fields from referenced document
{
  _id: ObjectId("order1"),
  customerId: ObjectId("customer1"),
  customerName: "John Doe",  // Duplicated for performance
  customerEmail: "john@example.com",  // Duplicated for performance
  items: [...],
  total: 150.00
}
```

**⚖️ Schema Design Trade-offs:**
- Embedding: Faster reads, larger documents, potential data duplication
- Referencing: Normalized data, multiple queries, smaller documents

---

## Performance Tuning

### Query Optimization

#### 1. Use Indexes Effectively
```javascript
// Bad: No index
db.users.find({email: "john@example.com"})

// Good: With index
db.users.createIndex({email: 1})
db.users.find({email: "john@example.com"})

// Compound index optimization
db.users.createIndex({status: 1, age: 1, name: 1})

// Good queries (can use index)
db.users.find({status: "active"})
db.users.find({status: "active", age: {$gte: 18}})
db.users.find({status: "active", age: {$gte: 18}}).sort({name: 1})

// Bad query (cannot use index efficiently)
db.users.find({age: {$gte: 18}})  // Skips status field
```

#### 2. Projection for Large Documents
```javascript
// Bad: Returns entire document
db.articles.find({category: "tech"})

// Good: Only return needed fields
db.articles.find(
  {category: "tech"},
  {title: 1, author: 1, publishDate: 1}
)
```

#### 3. Limit Results
```javascript
// Always use limit for large result sets
db.products.find({inStock: true}).limit(20)

// Pagination
db.products.find({inStock: true}).skip(20).limit(20)
```

#### 4. Efficient Sorting
```javascript
// Bad: Sort without index
db.users.find().sort({createdAt: -1})

// Good: Create index for sorting
db.users.createIndex({createdAt: -1})
db.users.find().sort({createdAt: -1})
```

### Write Optimization

#### 1. Batch Operations
```javascript
// Bad: Multiple individual inserts
for (let user of users) {
  db.users.insertOne(user)
}

// Good: Batch insert
db.users.insertMany(users)

// Bulk operations
const bulk = db.users.initializeUnorderedBulkOp()
bulk.insert({name: "Alice", age: 25})
bulk.find({name: "Bob"}).update({$set: {age: 30}})
bulk.find({name: "Charlie"}).remove()
bulk.execute()
```

#### 2. Write Concern Optimization
```javascript
// Fast writes (less durability)
db.logs.insertMany(documents, {writeConcern: {w: 0}})

// Durable writes (slower)
db.critical.insertOne(document, {writeConcern: {w: "majority", j: true}})
```

### MongoDB Performance Monitoring

#### 1. Database Profiler
```javascript
// Enable profiler for slow operations (>100ms)
db.setProfilingLevel(1, {slowms: 100})

// Profile all operations
db.setProfilingLevel(2)

// View profiler data
db.system.profile.find().limit(5).sort({ts: -1}).pretty()
```

#### 2. Current Operations
```javascript
// See currently running operations
db.currentOp()

// Kill long-running operation
db.killOp(opId)
```

#### 3. Database Statistics
```javascript
// Database stats
db.stats()

// Collection stats
db.users.stats()

// Index stats
db.users.aggregate([{$indexStats: {}}])
```

### Performance Best Practices

1. **Index Strategy**
   - Create indexes for query patterns
   - Monitor index usage
   - Remove unused indexes

2. **Document Design**
   - Keep frequently accessed data together
   - Avoid deep nesting (>2-3 levels)
   - Use appropriate data types

3. **Query Patterns**
   - Use projection to limit returned fields
   - Implement proper pagination
   - Cache frequent queries at application level

4. **Hardware Considerations**
   - Use SSDs for better I/O performance
   - Ensure adequate RAM for working set
   - Monitor CPU and memory usage

---

## Replication

Replication provides redundancy and increases data availability through replica sets.

### Replica Set Architecture

```
Primary Node (Read/Write)
    ↓ (replicates to)
Secondary Node (Read only)
Secondary Node (Read only)
```

### Setting Up Replica Set

#### 1. Start MongoDB Instances
```bash
# Start three mongod instances
mongod --replSet myReplicaSet --port 27017 --dbpath /data/db1
mongod --replSet myReplicaSet --port 27018 --dbpath /data/db2  
mongod --replSet myReplicaSet --port 27019 --dbpath /data/db3
```

#### 2. Initialize Replica Set
```javascript
// Connect to one instance and initialize
rs.initiate({
  _id: "myReplicaSet",
  members: [
    {_id: 0, host: "localhost:27017"},
    {_id: 1, host: "localhost:27018"},
    {_id: 2, host: "localhost:27019"}
  ]
})
```

#### 3. Replica Set Management
```javascript
// Check replica set status
rs.status()

// Add member
rs.add("localhost:27020")

// Remove member
rs.remove("localhost:27020")

// Step down primary (force election)
rs.stepDown()

// Set member priority (higher = more likely to be primary)
cfg = rs.conf()
cfg.members[1].priority = 2
rs.reconfig(cfg)
```

### Read Preferences

```javascript
// Primary (default) - read from primary only
db.users.find().readPref("primary")

// Secondary - read from secondary if available
db.users.find().readPref("secondary")

// Primary preferred - prefer primary, fallback to secondary
db.users.find().readPref("primaryPreferred")

// Secondary preferred - prefer secondary, fallback to primary
db.users.find().readPref("secondaryPreferred")

// Nearest - read from nearest member
db.users.find().readPref("nearest")
```

### Write Concern with Replication

```javascript
// Wait for acknowledgment from majority of replica set
db.users.insertOne(
  {name: "Alice"},
  {writeConcern: {w: "majority", j: true, wtimeout: 5000}}
)

// Custom write concern
db.users.insertOne(
  {name: "Bob"},
  {writeConcern: {w: 2}}  // Wait for 2 members
)
```

**🛡️ Replication Benefits:**
- **High Availability**: Automatic failover
- **Data Redundancy**: Multiple copies of data
- **Read Scaling**: Distribute reads across secondaries
- **Backup**: Take backups from secondary without impacting primary

---

## Sharding

Sharding distributes data across multiple servers for horizontal scaling.

### Sharding Architecture

```
Application
    ↓
Mongos Router
    ↓
Config Servers (Replica Set)
    ↓
Shard 1 (Replica Set) | Shard 2 (Replica Set) | Shard 3 (Replica Set)
```

### Setting Up Sharding

#### 1. Config Server Replica Set
```bash
# Start config servers
mongod --configsvr --replSet configReplSet --port 27019
mongod --configsvr --replSet configReplSet --port 27020
mongod --configsvr --replSet configReplSet --port 27021

# Initialize config replica set
rs.initiate({
  _id: "configReplSet",
  configsvr: true,
  members: [
    {_id: 0, host: "localhost:27019"},
    {_id: 1, host: "localhost:27020"},
    {_id: 2, host: "localhost:27021"}
  ]
})
```

#### 2. Shard Replica Sets
```bash
# Shard 1
mongod --shardsvr --replSet shard1 --port 27017
mongod --shardsvr --replSet shard1 --port 27018

# Shard 2  
mongod --shardsvr --replSet shard2 --port 27022
mongod --shardsvr --replSet shard2 --port 27023
```

#### 3. Mongos Query Router
```bash
mongos --configdb configReplSet/localhost:27019,localhost:27020,localhost:27021 --port 27016
```

#### 4. Add Shards
```javascript
// Connect to mongos and add shards
sh.addShard("shard1/localhost:27017,localhost:27018")
sh.addShard("shard2/localhost:27022,localhost:27023")
```

### Shard Key Selection

The shard key determines how data is distributed across shards.

#### Good Shard Keys
```javascript
// High cardinality, good distribution
{userId: 1}
{email: 1}
{timestamp: 1, userId: 1}  // Compound key
```

#### Bad Shard Keys
```javascript
// Low cardinality
{status: 1}  // Only few possible values

// Monotonically increasing
{_id: 1}     // ObjectId timestamp creates hotspots
{timestamp: 1}  // All new data goes to one shard
```

### Enable Sharding
```javascript
// Enable sharding for database
sh.enableSharding("myapp")

// Shard collection
sh.shardCollection("myapp.users", {userId: 1})

// Check sharding status
sh.status()
```

### Chunk Management
```javascript
// View chunks
db.chunks.find({"ns": "myapp.users"})

// Split chunk manually
sh.splitFind("myapp.users", {userId: "user12345"})

// Move chunk between shards
sh.moveChunk("myapp.users", {userId: "user12345"}, "shard2")
```

**⚖️ Sharding Considerations:**
- **Benefits**: Horizontal scaling, increased throughput
- **Complexity**: More complex architecture and operations
- **Limitations**: Cannot easily change shard key, scatter-gather queries
- **When to Shard**: When single server can't handle load/data size

---

## Real-world Best Practices

### 1. Connection Management

#### Connection Pooling
```javascript
// Node.js with MongoDB driver
const { MongoClient } = require('mongodb')

const client = new MongoClient(uri, {
  maxPoolSize: 10,        // Maximum connections in pool
  minPoolSize: 2,         // Minimum connections to maintain
  maxIdleTimeMS: 30000,   // Close connections after 30s idle
  serverSelectionTimeoutMS: 5000, // How long to try selecting server
  socketTimeoutMS: 45000, // How long socket stays open
})

// Reuse connection across requests
const db = client.db('myapp')
const users = db.collection('users')
```

#### Connection Best Practices
- **Reuse connections**: Don't create new connections for each request
- **Pool sizing**: Start with 10-20 connections per server
- **Error handling**: Implement proper connection error handling
- **Graceful shutdown**: Close connections properly on app shutdown

### 2. Error Handling

```javascript
// Comprehensive error handling
async function createUser(userData) {
  try {
    const result = await db.users.insertOne(userData)
    return { success: true, id: result.insertedId }
  } catch (error) {
    // Handle specific MongoDB errors
    if (error.code === 11000) {
      // Duplicate key error
      return { success: false, error: 'User already exists' }
    } else if (error.name === 'ValidationError') {
      return { success: false, error: 'Invalid data format' }
    } else if (error.name === 'MongoNetworkError') {
      // Connection issues
      return { success: false, error: 'Database connection failed' }
    }
    
    // Log unexpected errors
    console.error('Unexpected database error:', error)
    return { success: false, error: 'Internal server error' }
  }
}
```

### 3. Data Validation

#### Schema Validation (MongoDB 3.6+)
```javascript
// Create collection with validation rules
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email", "age"],
      properties: {
        name: {
          bsonType: "string",
          minLength: 2,
          maxLength: 50,
          description: "Name must be a string between 2-50 characters"
        },
        email: {
          bsonType: "string",
          pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
          description: "Must be a valid email address"
        },
        age: {
          bsonType: "int",
          minimum: 0,
          maximum: 150,
          description: "Age must be between 0 and 150"
        },
        role: {
          enum: ["user", "admin", "moderator"],
          description: "Role must be user, admin, or moderator"
        }
      }
    }
  },
  validationAction: "error", // or "warn"
  validationLevel: "strict"   // or "moderate"
})
```

#### Application-Level Validation
```javascript
// Using Joi for validation (Node.js)
const Joi = require('joi')

const userSchema = Joi.object({
  name: Joi.string().min(2).max(50).required(),
  email: Joi.string().email().required(),
  age: Joi.number().integer().min(0).max(150).required(),
  role: Joi.string().valid('user', 'admin', 'moderator').default('user')
})

function validateUser(userData) {
  return userSchema.validate(userData)
}
```

### 4. Security Best Practices

#### Authentication & Authorization
```javascript
// Enable authentication
use admin
db.createUser({
  user: "admin",
  pwd: "strongPassword123!",
  roles: ["root"]
})

// Create application user with limited permissions
use myapp
db.createUser({
  user: "appUser",
  pwd: "appPassword123!",
  roles: [
    { role: "readWrite", db: "myapp" },
    { role: "read", db: "analytics" }
  ]
})
```

#### Connection Security
```javascript
// Use TLS/SSL in production
const client = new MongoClient(uri, {
  ssl: true,
  sslValidate: true,
  sslCA: fs.readFileSync('ca-certificate.crt'),
  sslCert: fs.readFileSync('client-certificate.crt'),
  sslKey: fs.readFileSync('client-key.key')
})
```

#### Input Sanitization
```javascript
// Prevent NoSQL injection
function sanitizeInput(input) {
  if (typeof input === 'object' && input !== null) {
    // Remove dangerous operators
    const dangerous = ['$where', '$regex', '$gt', '$lt', '$ne', '$in', '$nin']
    for (let key of dangerous) {
      delete input[key]
    }
  }
  return input
}

// Safe query building
function findUserByEmail(email) {
  // Ensure email is a string
  if (typeof email !== 'string') {
    throw new Error('Email must be a string')
  }
  
  return db.users.findOne({ email: email })
}
```

### 5. Monitoring & Logging

#### Application Monitoring
```javascript
// Track database operations
const startTime = Date.now()
try {
  const result = await db.users.find({status: 'active'}).toArray()
  const duration = Date.now() - startTime
  
  // Log slow queries
  if (duration > 1000) {
    console.warn(`Slow query detected: ${duration}ms`)
  }
  
  // Metrics collection
  metrics.increment('db.query.count')
  metrics.timing('db.query.duration', duration)
  
  return result
} catch (error) {
  metrics.increment('db.query.error')
  throw error
}
```

#### Health Checks
```javascript
// Database health check endpoint
async function healthCheck() {
  try {
    await db.admin().ping()
    const stats = await db.stats()
    
    return {
      status: 'healthy',
      database: {
        connected: true,
        collections: stats.collections,
        dataSize: stats.dataSize,
        indexSize: stats.indexSize
      }
    }
  } catch (error) {
    return {
      status: 'unhealthy',
      error: error.message
    }
  }
}
```

### 6. Backup & Recovery

#### Automated Backups
```bash
# mongodump for logical backups
mongodump --host localhost:27017 --db myapp --out /backup/$(date +%Y%m%d)

# Point-in-time recovery with replica sets
mongodump --host localhost:27017 --oplog

# Compressed backup
mongodump --gzip --archive=/backup/myapp_$(date +%Y%m%d).gz
```

#### Backup Strategy
```javascript
// Backup rotation script
const backupRetentionDays = 30
const backupPath = '/backups'

async function performBackup() {
  const timestamp = new Date().toISOString().split('T')[0]
  const backupFile = `${backupPath}/backup_${timestamp}.gz`
  
  // Create backup
  exec(`mongodump --gzip --archive=${backupFile}`)
  
  // Clean old backups
  const cutoffDate = new Date()
  cutoffDate.setDate(cutoffDate.getDate() - backupRetentionDays)
  
  const oldBackups = fs.readdirSync(backupPath)
    .filter(file => {
      const fileDate = new Date(file.match(/\d{4}-\d{2}-\d{2}/)[0])
      return fileDate < cutoffDate
    })
  
  oldBackups.forEach(file => fs.unlinkSync(`${backupPath}/${file}`))
}
```

### 7. Deployment Patterns

#### Blue-Green Deployment
```javascript
// Connection string switching for zero-downtime deployments
const connections = {
  blue: 'mongodb://blue-cluster:27017/myapp',
  green: 'mongodb://green-cluster:27017/myapp'
}

let currentEnvironment = process.env.DB_ENVIRONMENT || 'blue'
const connectionString = connections[currentEnvironment]

// Graceful connection switching
async function switchDatabase(newEnvironment) {
  const newClient = new MongoClient(connections[newEnvironment])
  await newClient.connect()
  
  // Test new connection
  await newClient.db().admin().ping()
  
  // Switch active connection
  const oldClient = client
  client = newClient
  currentEnvironment = newEnvironment
  
  // Close old connection after delay
  setTimeout(() => oldClient.close(), 30000)
}
```

#### Environment Configuration
```javascript
// Environment-specific configurations
const config = {
  development: {
    uri: 'mongodb://localhost:27017/myapp_dev',
    options: {
      maxPoolSize: 5,
      serverSelectionTimeoutMS: 5000
    }
  },
  staging: {
    uri: 'mongodb://staging-cluster:27017/myapp_staging',
    options: {
      maxPoolSize: 10,
      ssl: true,
      authSource: 'admin'
    }
  },
  production: {
    uri: 'mongodb+srv://prod-cluster.mongodb.net/myapp',
    options: {
      maxPoolSize: 50,
      ssl: true,
      authSource: 'admin',
      retryWrites: true,
      w: 'majority'
    }
  }
}

const env = process.env.NODE_ENV || 'development'
const dbConfig = config[env]
```

---

## Common Pitfalls & Advanced Tips

### ❌ Common Pitfalls

#### 1. Poor Schema Design
```javascript
// ❌ Bad: Unbounded arrays
{
  _id: ObjectId("..."),
  userId: "user123",
  activities: [
    // This array could grow infinitely
    {date: "2023-01-01", action: "login"},
    {date: "2023-01-02", action: "purchase"},
    // ... thousands more entries
  ]
}

// ✅ Good: Separate collection or bucketing
{
  _id: ObjectId("..."),
  userId: "user123",
  month: "2023-01",
  activities: [
    // Limited to one month of data
    {date: "2023-01-01", action: "login"},
    {date: "2023-01-02", action: "purchase"}
  ]
}
```

#### 2. Inefficient Queries
```javascript
// ❌ Bad: No index, regex at start
db.users.find({name: /^john/i})

// ✅ Good: Text index for full-text search
db.users.createIndex({name: "text"})
db.users.find({$text: {$search: "john"}})

// ❌ Bad: Large skip values
db.products.find().skip(10000).limit(20)

// ✅ Good: Cursor-based pagination
db.products.find({_id: {$gt: lastSeenId}}).limit(20)
```

#### 3. Ignoring Write Concerns
```javascript
// ❌ Bad: Fire and forget writes
db.orders.insertOne(order) // Default write concern might not be durable

// ✅ Good: Appropriate write concern for critical data
db.orders.insertOne(order, {
  writeConcern: {
    w: "majority",
    j: true,
    wtimeout: 5000
  }
})
```

#### 4. Not Handling Errors
```javascript
// ❌ Bad: No error handling
const user = await db.users.findOne({_id: userId})
console.log(user.name) // Could throw if user is null

// ✅ Good: Proper error handling
try {
  const user = await db.users.findOne({_id: userId})
  if (!user) {
    return { error: 'User not found' }
  }
  return { name: user.name }
} catch (error) {
  console.error('Database error:', error)
  return { error: 'Database unavailable' }
}
```

### 🚀 Advanced Tips

#### 1. Aggregation Optimization
```javascript
// Use $match early in pipeline
db.orders.aggregate([
  // ✅ Filter first (uses indexes)
  {$match: {status: "completed", date: {$gte: startDate}}},
  
  // Then transform
  {$group: {_id: "$customerId", total: {$sum: "$amount"}}},
  {$sort: {total: -1}},
  {$limit: 10}
])

// Use $project to reduce document size early
db.orders.aggregate([
  {$match: {status: "completed"}},
  // ✅ Reduce document size early
  {$project: {customerId: 1, amount: 1, date: 1}},
  {$group: {_id: "$customerId", total: {$sum: "$amount"}}}
])
```

#### 2. Bulk Operations for Performance
```javascript
// ✅ Efficient bulk operations
const bulk = db.users.initializeUnorderedBulkOp()

users.forEach(user => {
  if (user._id) {
    bulk.find({_id: user._id}).upsert().updateOne({$set: user})
  } else {
    bulk.insert(user)
  }
})

const result = await bulk.execute()
```

#### 3. Memory-Efficient Large Result Sets
```javascript
// ✅ Process large datasets with cursors
const cursor = db.largeCollection.find({}).batchSize(1000)

await cursor.forEach(async (doc) => {
  // Process each document
  await processDocument(doc)
})

// Or use async iteration
for await (const doc of db.largeCollection.find({})) {
  await processDocument(doc)
}
```

#### 4. Advanced Indexing Strategies
```javascript
// Partial indexes for sparse data
db.users.createIndex(
  {premiumExpiry: 1},
  {
    partialFilterExpression: {
      userType: "premium",
      premiumExpiry: {$exists: true}
    }
  }
)

// TTL indexes for automatic cleanup
db.sessions.createIndex(
  {createdAt: 1},
  {expireAfterSeconds: 3600} // Delete after 1 hour
)

// Sparse indexes for optional fields
db.users.createIndex(
  {phoneNumber: 1},
  {sparse: true, unique: true}
)
```

#### 5. Advanced Query Patterns
```javascript
// Use aggregation for complex transformations
db.users.aggregate([
  {
    $addFields: {
      fullName: {$concat: ["$firstName", " ", "$lastName"]},
      isActive: {
        $and: [
          {$ne: ["$status", "inactive"]},
          {$gte: ["$lastLogin", thirtyDaysAgo]}
        ]
      }
    }
  },
  {$match: {isActive: true}},
  {$project: {fullName: 1, email: 1, lastLogin: 1}}
])

// Efficient existence checks
// ✅ Use findOne with projection for existence
const exists = await db.users.findOne(
  {email: "test@example.com"},
  {projection: {_id: 1}}
)

// ✅ Use countDocuments with limit for counting
const count = await db.users.countDocuments(
  {status: "active"},
  {limit: 1}
)
```

#### 6. Schema Versioning
```javascript
// Handle schema evolution gracefully
{
  _id: ObjectId("..."),
  schemaVersion: 2,
  name: "John Doe",
  // v1 had separate firstName/lastName
  // v2 uses single name field
  contact: {
    email: "john@example.com",
    phone: "+1234567890"
  }
}

// Migration function
async function migrateUserSchema() {
  const cursor = db.users.find({schemaVersion: {$ne: 2}})
  
  for await (const user of cursor) {
    let update = {$set: {schemaVersion: 2}}
    
    if (user.firstName && user.lastName) {
      update.$set.name = `${user.firstName} ${user.lastName}`
      update.$unset = {firstName: "", lastName: ""}
    }
    
    await db.users.updateOne({_id: user._id}, update)
  }
}
```

---

## Quick Reference Cheat Sheet

### Essential Commands
```javascript
// Database Operations
use mydb                    // Switch database
show dbs                   // List databases
db.dropDatabase()          // Delete current database

// Collection Operations
show collections           // List collections
db.createCollection("users") // Create collection
db.users.drop()           // Delete collection

// CRUD Quick Reference
db.users.insertOne({name: "Alice"})
db.users.find({age: {$gte: 18}})
db.users.updateOne({name: "Alice"}, {$set: {age: 25}})
db.users.deleteOne({name: "Alice"})

// Index Management
db.users.createIndex({email: 1})
db.users.getIndexes()
db.users.dropIndex({email: 1})

// Aggregation
db.orders.aggregate([
  {$match: {status: "completed"}},
  {$group: {_id: "$customerId", total: {$sum: "$amount"}}}
])
```

### Query Operators Quick Reference
```javascript
// Comparison
$eq, $ne, $gt, $gte, $lt, $lte, $in, $nin

// Logical  
$and, $or, $not, $nor

// Element
$exists, $type

// Array
$all, $elemMatch, $size

// Text
$text, $regex

// Geospatial
$near, $geoWithin, $geoIntersects
```

### Update Operators
```javascript
// Field Updates
$set, $unset, $inc, $mul, $rename, $min, $max, $currentDate

// Array Updates
$push, $pull, $addToSet, $pop, $pullAll, $each, $slice, $sort
```

---

## Interview Questions & Answers

### Junior Level Questions

**Q: What is MongoDB and how is it different from SQL databases?**
A: MongoDB is a NoSQL document database that stores data in flexible, JSON-like documents. Unlike SQL databases with fixed schemas and tables, MongoDB uses collections of documents that can have varying structures, making it ideal for applications with evolving data requirements.

**Q: Explain the difference between find() and findOne()**
A: `find()` returns a cursor to all documents matching the query, while `findOne()` returns only the first matching document or null if no match is found. Use `findOne()` when you expect only one result to improve performance.

**Q: What is the _id field in MongoDB?**
A: The `_id` field is a unique identifier for each document, automatically created if not provided. It's typically an ObjectId containing a timestamp, machine identifier, process ID, and counter, ensuring uniqueness across the cluster.

### Senior Level Questions

**Q: How would you design a schema for a social media application with users, posts, and comments?**
A: I'd use a hybrid approach:
- **Users**: Separate collection with basic info
- **Posts**: Separate collection with author reference and embedded basic comments (limited number)
- **Comments**: For posts with many comments, use separate collection with post reference
- **Relationships**: Reference pattern for followers/following to avoid document size limits

**Q: Explain MongoDB's aggregation framework and when to use it over find()**
A: Aggregation framework processes data through pipelines of stages (match, group, project, sort, etc.). Use it for:
- Complex data transformations
- Grouping and statistical operations  
- Joining data from multiple collections ($lookup)
- Data analysis and reporting
Use `find()` for simple queries and when you need all document fields.

**Q: How do you handle eventual consistency in a distributed MongoDB setup?**
A: Use appropriate read/write concerns:
- **Write Concern**: `{w: "majority"}` ensures writes are acknowledged by majority of replica set
- **Read Concern**: `"majority"` ensures reading only majority-committed data
- **Read Preference**: Use "primary" for consistent reads, "secondary" for potentially stale but distributed reads
- Implement application-level consistency checks for critical operations

This comprehensive guide covers MongoDB from basic concepts to advanced production patterns. Use it as both a learning resource and quick reference for your MongoDB development journey!