---
title: "VART: A Persistent Data Structure For Snapshot Isolation"
slug: "vart-a-persistent-data-structure-for-snapshot-isolation"
date: "2024-01-23T00:00:00.000Z"
categories:
  - "engineering"
read_time: "14 min read"
summary: "The blog introduces VART, an Immutable Versioned Adaptive Radix Trie, designed for snapshot isolation in databases (surrealKV), exploring isolation levels, concurrency control."
source: "https://surrealdb.com/blog/vart-a-persistent-data-structure-for-snapshot-isolation"
cover: "../../assets/12bce6889a9cbe2e.jpg"
---

# VART: A Persistent Data Structure For Snapshot Isolation

![VART: A Persistent Data Structure For Snapshot Isolation](../../assets/12bce6889a9cbe2e.jpg)

The foundation of a resilient database hinges on its ability to handle concurrent transactions without compromising data integrity and consistency. Addressing this challenge requires a focus on Isolation, a vital facet of the ACID properties. Isolation ensures the reliability and consistency of transactions when multiple transactions access data concurrently.

This blog post delves into the intricacies of transaction isolation, and introduces VART - a persistent data structure designed for snapshot isolation. Furthermore, it offers a glimpse into the evolution of SurrealKV, our persistent in-memory, transactional Key-Value store with versioning support.

## Understanding Isolation Levels in ACID

Isolation levels, as defined by the [SQL standard](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-95-51.pdf), quantify the extent to which one transaction can operate independently of another. The SQL standard recognises various isolation levels, each addressing specific anomalies such as dirty writes, dirty reads, lost updates, and other potential inconsistencies that can arise in a concurrent transactional environment. The list of these isolation levels is provided below for reference.

| Isolation Level | Dirty Write | Dirty Read | Lost Update | Phantom | Read Skew | Write Skew |
|---|---|---|---|---|---|---|
| READ UNCOMMITTED | Not Possible | Possible | Possible | Possible | Possible | Possible |
| READ COMMITTED | Not Possible | Not Possible | Possible | Possible | Possible | Possible |
| REPEATABLE READ | Not Possible | Not Possible | Not Possible | Possible | Not Possible | Not Possible |
| SNAPSHOT | Not Possible | Not Possible | Not Possible | Sometimes Possible | Not  Possible | Possible |
| ANSI SQL SERIALIZABLE | Not Possible | Not Possible | Not Possible | Not Possible | Not Possible | Not Possible |

Interestingly, the terms MVCC (Multiversion Concurrency Control) and OCC (Optimistic Concurrency Control), essential for managing simultaneous transactions in a database, aren't explicitly addressed in isolation levels. To grasp the complete picture, we need to understand concurrency control and how it fits into the isolation framework.

## Understanding Concurrency Control

Sequential transactions pose no overlap issues. However, the complexity emerges when multiple transactions run concurrently, giving rise to anomalies such as:

1. **Lost Update Problem:** A subsequent transaction replaces a data item's value, causing the first value to be lost for other transactions requiring it.

```rust
Time    | Transaction A          | Transaction B
--------|------------------------|------------------------
T1      | Read X (Value = 10)    |
T2      |                        | Read X (Value = 10)
T3      | Update X (Value = 15)  |
T4      | Commit                 |
T5      |                        | Update X (Value = 20)
T6      |                        | Commit
T7      | Read X (Value = 20)    |

```

2. **Dirty Read Problem:** Transactions read a value from a cancelled or ongoing transaction, resulting in wrong outcomes.

```rust
Time    | Transaction A          | Transaction B
--------|------------------------|------------------------
T0      | Begin                  | Begin
T1      | Read X (Value = 10)    |
T2      |                        | Write X (Value = 20)
T3      | Read X (Value = 20)    |
T4      | Commit                 |
T5      |                        | Commit
```

In such scenarios, where a database has to handle multiple transactions at the same time, ensuring the consistency of your database becomes absolutely critical. This means setting up strong concurrency control mechanisms. These mechanisms are like the traffic signals of your database, helping it navigate challenges to ensure a smooth and reliable execution of transactions in this concurrent environment. Simply put, it's all about maintaining order and reliability when there's a lot happening at once.

### Navigating Concurrency Control Methods

Concurrency control methods fall into two main categories: lock-based and non-lock-based.

**1. Lock-Based Concurrency Control:**

In lock-based approaches, transactions regulate access to data through locks, acting as barriers to prevent conflicting operations from occurring simultaneously. Noteworthy methods include:

- **Two-Phase Locking (2PL):** Transactions use locks in two stages, ensuring orderliness.
- **Strict Two-Phase Locking (Strict 2PL):** Locks persist until the transaction concludes.

**2. Non-Lock-Based Concurrency Control:**

Non-lock-based methods aim to manage concurrency without traditional locks, often adopting optimistic strategies. Transactions proceed initially without locks, with conflict resolution occurring later. Key methods include:

- **Optimistic Concurrency Control (OCC):** Transactions proceed without locks initially. Conflicts are resolved at the transaction's end.
- **Multiversion Concurrency Control (MVCC):** Each write operation creates new versions of database objects, enabling transactions to read different versions simultaneously.

### Why Concurrency Control Matters

Isolation levels solely determine the extent to which one transaction remains independent of another, preventing interference and ensuring consistency. However, concurrency control mechanisms play a vital role in ensuring seamless coordination among concurrent transactions.

Therefore, for a database handling multiple concurrent transactions, the right isolation level and a concurrency control mechanism are crucial. This ensures reliable execution of transactions in a concurrent environment, safeguarding the overall database integrity. In SurrealKV, our initial version uses Snapshot Isolation (including Serializable Snapshot Isolation) to segregate transactions and employs MVCC for concurrency control.

## Data Structures For Isolation

Designing data structures for a database that effectively manages concurrent transactions involves specific considerations. These structures need to possess characteristics such as persistence, immutability, and the ability to retrieve multiple data versions. The essential functionality of accessing and modifying multiple versions is integral to MVCC, and this design process incorporates the use of Persistent Data Structures.

### Persistent Data Structures

Persistent data structures, alternatively referred to as immutable data structures, maintain the original version despite modifications. This concept of unchangeable data is rooted in Chris Okasaki's paper, ["**_Purely Functional Data Structures_**,"](https://www.cs.cmu.edu/~rwh/students/okasaki.pdf) which explores functional data structures like lists, queues, and trees, emphasising the efficiency of persistent amortised data structures. A simple example of an immutable update in a list shows that the updated list shares some of the original structure while keeping the old version valid.

![Whitepaper.jpg](../../assets/35ab11aea849abb0.jpg)

Driscoll et al.'s paper, ["**_Making Data Structures Persistent_**,"](https://www.cs.cmu.edu/~sleator/papers/making-data-structures-persistent.pdf) expands on the concept of persistence in data structures. Ordinary data structures are typically ephemeral, meaning changes destroy the old version, leaving only the new version accessible. In contrast, a persistent structure permits access to any version, whether old or new, at any given time.

The paper introduces simple and efficient techniques, such as fat nodes and path copying, for achieving persistence in linked data structures. These techniques can be applied to create persistent forms of any trie with logarithmic access, insertion, and deletion times. Below, you can see an example of persistence in a radix trie.

![/static/whitepaper.pdf](../../assets/8a8eef06d059c6d7.jpg)

### The Role of Persistent Data Structures in Snapshot Isolation

**_Snapshot isolation_** is a transaction isolation level that provides each transaction with a consistent snapshot of the database, shielding it from the interference of concurrent transactions. As multiple transactions execute concurrently, snapshot isolation ensures that each transaction has a consistent view of the database since the start of the operation.

To maintain a consistent database view for each transaction, we leverage persistent data structures. Transactions connect to a unique snapshot version of the index, and any changes (writes) impact the current snapshot, creating a new root without altering past nodes. This association ensures consistent and distinct dataset views across different transactional time points.

## Introducing VART: An Immutable Versioned Adaptive Radix Trie

VART, short for Versioned Adaptive Radix Trie, is a persistent data structure designed to serve as the index within SurrealKV - our in-memory persistent Key-Value store written in Rust (with support for multiple readers and writers - a topic that will be explored in our future blogs). As a Transactional Key-Value Store, SurrealKV uses VART as its index to manage concurrency support via snapshot isolation.

#### **Decoding "Versioned Adaptive Radix Trie"**

The term "**Versioned**" in VART signifies the use of versioning, indicating a chronological record of every modification made to the tree. The "**Adaptive**" attribute refers to the dynamic node sizes and the path compression technique, aimed at optimising space utilisation and enhancing overall performance. Lastly, the "**Radix Trie**" component underscores the adoption of a tree-like data structure, specifically tailored for storing associative arrays. Now, let's dig deeper into the technicalities of these key elements.

**Radix Tries**, the foundation of VART, represent tree-like data structures used for storing associative arrays. The structure of a Radix Trie is designed to optimise search operations effectively. At its core, each node encapsulates a shared prefix of specific keys, and each additional edge extends the prefix by a character. This structural design allows a Radix Trie to traverse the tree character by character, facilitating rapid key retrieval.

**Radix Tries** offer several advantages, including:

- Complexity depends on key length, not the number of elements
- There’s no need for rebalancing: two different insert orders result in the same tree
- Keys are stored in lexicographical order

**[Adaptive Radix Tries](https://db.in.tum.de/~leis/papers/ART.pdf)** (ART) are an evolved version of Radix Tries that optimise space usage and enhance performance. The principal improvements of ART over traditional Radix Tries are:

1. **Dynamic Node Size:** Unlike static node sizes in traditional Radix Tries, ART nodes dynamically adjust based on the number of children. This dynamic adaptation optimises space usage.
1. **Path Compression:** ART incorporates path compression, eliminating unnecessary nodes in paths with a single child. This drastic reduction in trie depth accelerates key lookups.
1. **Lazy Expansion:** Nodes in ART dynamically expand and contract with key insertions and removals, adapting the trie structure to the dataset's characteristics.

![are.jpg](../../assets/d86061bf9c63cafb.jpg)

While this blog won't go into the intricacies of ART, the linked [paper](https://db.in.tum.de/~leis/papers/ART.pdf) offers a detailed explanation for those interested. These characteristics of radix tries make it a suitable choice for an in-memory index.

## Deep Dive Into VART

Now, let's look closely on how VART works, looking into how it handles persistence, and versioning. Below is a simple diagram explaining the different types of nodes used in VART. While this differs slightly from the original implementation in the ART paper, the overall concept remains the same.

**Different Types of Nodes in VART**

![art.jpg](../../assets/adde1f856776c1ee.jpg)

ART is designed to handle varying levels of sparsity by compressing nodes based on their sparsity. Five primary node types are used to manage different levels of sparsity:

1. **Flat Nodes (4 to 16 Non-Null Children)**

```rust
pub struct FlatNode<P: KeyTrait + Clone, N: Version, const WIDTH: usize> {
    pub(crate) prefix: P,
    pub(crate) version: u64,
    keys: [u8; WIDTH],
    children: Box<[MaybeUninit<Option<Arc<N>>>; WIDTH]>,
    num_children: u8,
}
```

Flat nodes, akin to Node4 and Node16 in the [ART paper](https://db.in.tum.de/~leis/papers/ART.pdf), cater to nodes with up to 16 children. Their fixed-size array efficiently organises child nodes, and keys are lexicographically sorted, facilitating easy binary search through SIMD instructions.

2. **Node Type 48 (17 to 48 Non-Null Children)**

```rust
pub struct Node48<P: KeyTrait + Clone, N: Version> {
    pub(crate) prefix: P,
    pub(crate) version: u64,
    keys: SparseVector<u8, 256>,
    children: SparseVector<Arc<N>, 48>,
    num_children: u8,
}
```

A Node48 is designed to accommodate a larger number of keys compared to a Node16, with a capacity of up to three times as many keys. In this structure, the keys are stored implicitly in an array of 256 indexes. Each entry in this array serves as an index, pointing to a separate array containing up to 48 pointers.

3. **Node Type 256 (49 to 256 Non-Null Children)**

```rust
pub struct Node256<P: KeyTrait + Clone, N: Version> {
    pub(crate) prefix: P,    // Prefix associated with the node
    pub(crate) version: u64, // Version for node256
    children: SparseVector<Arc<N>, 256>,
    num_children: usize,
}
```

A Node256 represents the traditional trie node, utilised when a node has a child count ranging from 49 to 256. This node type is the most efficient among all node types when it comes to looking up child pointers.

4. **Twig Node**

```rust
#[derive(Clone)]
pub struct TwigNode<K: KeyTrait + Clone, V> {
    pub(crate) prefix: K,
    pub(crate) values: Vec<Arc<LeafValue<V>>>,
    pub(crate) version: u64,
}

```

The Twig Node mirrors a Fat Node, encapsulating pointers to different versions and values. It serves as a repository for the entire history of key mutations, easing the traversal of various version histories.

5. **Leaf Node**

```rust
pub struct LeafValue<V> {
    pub(crate) value: V,
    pub(crate) version: u64,
    pub(crate) ts: u64,
}
```

A leaf node contains the value and a version field that specifies the version number for the modified key. The `ts` field is used to track actual timestamps.

### \***\*Persistence Through Copy-On-Write (CoW)\*\***

The persistence in VART is achieved using a Copy-On-Write (CoW) approach. Every modification to the data structure spawns a new version, mirroring the changes while preserving the original version. This results in a branching history of versions, where both the original and updated versions coexist, ready for further modifications.

In the context of Copy-On-Write (CoW) in Rust, the use of smart pointers, specifically **`std::rc::Rc`** and **`std::sync::Arc`**, plays a crucial role in avoiding unnecessary data copying or cloning. These smart pointers provide a mechanism for multiple sections of code to share ownership of the data without duplicating its content.

![PathCopying.jpg](../../assets/764ffa620691cab0.jpg)

When employing smart pointers like **`Arc`** (Atomically Reference Counted), data ownership is tracked through reference counting. This means that the data itself is not cloned or copied when shared between different sections of code. Instead, the smart pointer maintains a count of references to the underlying data. When one section necessitates data modification and creates a new version, only the reference count is updated, and a new smart pointer is created to point to the modified data. This ensures that modifications are isolated to the specific section of code making changes, and the original data remains unchanged for other sections using it.

This approach aligns seamlessly with the principles of CoW, allowing for a more memory-efficient and performant handling of shared data in the context of concurrent modifications. A practical example of this can be seen in the [`add_child`](https://github.com/surrealdb/vart/blob/d298b364f6616c1301cc9c1d22cd60c46547a57e/src/node.rs#L301) function for a FlatNode.

```rust
impl<P: KeyTrait + Clone, N: Version, const WIDTH: usize> NodeTrait<N> for FlatNode<P, N, WIDTH> {
    // Add a child to the current node and return a newer node, creating a new version in the process.
    fn add_child(&self, key: u8, node: N) -> Self {
        // create a clone of the existing node
        let mut new_node = self.clone();
        let idx = self.find_pos(key).expect("node is full");

        // Convert the node to Arc<N> and insert it.
        new_node.insert_child(idx, key, Arc::new(node));
        new_node
    }

    // Clone the current node, ensuring the persistence of the existing version.
    fn clone(&self) -> Self {
        let mut new_node = Self::new(self.prefix.clone());
        for i in 0..self.num_children as usize {
            new_node.keys[i] = self.keys[i];
            new_node.children[i] = self.children[i].clone();
        }
        new_node.num_children = self.num_children;
        new_node.version = self.version;
        new_node
    }
}
```

As you can see, each update produces a new version that reflects changes while retaining references to the unchanged nodes from the previous version. This results in a branching version history. When updating an immutable tree, only some nodes which are affected are copied, and a new root is returned. The old root remains valid until it's removed. Changes to adaptive radix tree nodes only impact the O(log256 n) ancestors of that node and hence can efficiently be converted into persistent structures via path copying. [This ](https://github.com/surrealdb/vart/blob/d298b364f6616c1301cc9c1d22cd60c46547a57e/src/art.rs#L983) method helps in the generation of snapshots.

```rust
    pub fn insert(
        &mut self,
        key: &P,
        value: V,
        version: u64,
        ts: u64,
    ) -> Result<Option<V>, TrieError> {

        let (new_root, old_node) = match &self.root {
            None => {
                let mut commit_version = version;
                if version == 0 {
                    commit_version += 1;
                }
                (
                    Arc::new(Node::new_twig(
                        key.as_slice().into(),
                        key.as_slice().into(),
                        value,
                        commit_version,
                        ts,
                    )),
                    None,
                )
            }
            Some(root) => {
                // Check if the given version is older than the root's current version.
                // If so, return an error and do not insert the new node.
                let curr_version = root.version();
                let mut commit_version = version;
                if version == 0 {
                    commit_version = curr_version + 1;
                } else if curr_version >= version {
                    return Err(TrieError::Other(
                        "given version is older than root's current version".to_string(),
                    ));
                }
                match Node::insert_recurse(root, key, value, commit_version, ts, 0) {
                    Ok((new_node, old_node)) => (new_node, old_node),
                    Err(err) => {
                        return Err(err);
                    }
                }
            }
        };

        self.root = Some(new_root);
        Ok(old_node)
    }
```

### Navigating Snapshots with CoW

Snapshot generation in VART is based on the CoW approach method described above. Every modification to a node, including the root node, results in a new copy of that node, leaving the original node unaffected.

![snapshots.jpg](../../assets/5e9e190b7752d03a.jpg)

Put simply, any changes to the tree after this point do not affect the snapshot, allowing you to revert to that state if needed. Let's see how this works in practice.

```rust
    pub fn create_snapshot(&mut self) -> Result<Snapshot<P, V>, TrieError> {
        let root = self.root.as_ref().cloned();
        let version = self.root.as_ref().map_or(1, |root| root.version() + 1);
        let new_snapshot = Snapshot::new(new_snapshot_id, root, version);

        Ok(new_snapshot)
    }
```

This method gives each transaction its own local copy of the tree. As a result, the tree's main index remains unchanged during the transaction, ensuring isolation between different transactions. This, in turn, helps support a "read-your-own-writes" consistency model, which allows a transaction to immediately see its own updates, and enable read snapshots, allowing a transaction to read from a consistent snapshot of the database. This snapshot includes all updates from transactions that finished before its creation, and excludes those from transactions that did not.

Additionally, this approach aids in conflict detection. Each transaction works on its own copy of the tree, making it easy to identify when two transactions try to modify the same node - each will have different copies of the node. This helps in conflict detection and resolution, a topic that we will talk about in an upcoming blog post.

### The Significance of Versions

The "Versioned" aspect in VART provides a chronological record of each modification to the tree. It serves four key purposes:

1. **Historical Queries**: Establishes an order for mutations, enabling efficient querying through historical versions of a record.
1. **Preventing Stale Writes**: Every modification to the trie results in an increment of the root's version. If a node undergoes an update with a timestamp older than the current version, it signifies outdated writes, thereby ensuring data consistency.
1. **MVCC:** Read operations retrieve the version of the data committed at or before the transaction's read timestamp, ensuring consistency. Write operations create new versions with the transaction's timestamp, preventing interference with other transactions.
1. **Transaction Ordering:** Helps in ordering transactions, ensuring a clear sequence of events. This ordering is essential for maintaining the integrity of the database and resolving conflicts systematically.

![Timestamps.jpg](../../assets/091c62d45a8a024b.jpg)

## Benchmarks

**Key Types:**

1. Fixed-length datatypes, such as 128-bit integers or strings of exactly 64 bytes.
1. Variable-length datatypes, such as general strings suffixed with the NULL byte to every key, indicating that this is the end of the key.

**Storage Information:**

- Fixed length datatypes can be stored on the stack.
- Variable length datatypes need to be stored on the heap, impacting performance.

**Hardware Overview:**

```cli
  Model Name: MacBook Pro
  Chip: Apple M2 Max
  Total Number of Cores: 12 (8 performance and 4 efficiency)
  Memory: 32 GB
```

**Test Environment:** The benchmarks were conducted with the 16byte fixed size keys

```cli
| Test                         | Time         |
|------------------------------|--------------|
| inserts/seq_insert           | 957.81 ns    |
| inserts/rand_insert          | 1.3932 µs    |
| deletes/seq_delete           | 60.669 ns    |
| deletes/rand_delete          | 81.183 ns    |
| reads/seq_get/100            | 8.6815 ns    |
| reads/seq_get/1000           | 8.9618 ns    |
| reads/seq_get/10000          | 8.7215 ns    |
| reads/seq_get/100000         | 10.763 ns    |
| reads/rand_get/100           | 35.839 ns    |
| reads/rand_get/1000          | 47.081 ns    |
| reads/rand_get/10000         | 54.464 ns    |
| reads/rand_get/100000        | 98.734 ns    |
| random_get_str/art/1000000    | 403.10 ns   |
| iters/iter_u64/100           | 2.5586 µs    |
| iters/iter_u64/1000          | 25.229 µs    |
| iters/iter_u64/10000         | 245.74 µs    |
| iters/iter_u64/100000        | 2.8753 ms    |
| iters/iter_variable_size_key  | 24.665 ms   |
```

## Conclusion

The utilisation of Adaptive Radix Tries with persistence makes VART proficient in managing both write and read-heavy workloads, making the creation of data snapshots easy. While Persistent Data Structures may not match the speed of non-persistent structures, they provide the advantages of immutability and versioning.

We have recently released both the [crate](https://crates.io/crates/vart) and the corresponding [code](https://github.com/surrealdb/vart), which we would love for you to check out. Although this represents our initial implementation with ample room for improvement, we invite the community to kindly explore, test, and share any insights or potential issues you may come across. Contributions and feedback are always appreciated, and we welcome any thoughts you may have by opening issues on our repository.

## Future Work

We’ve planned for several significant enhancements to VART. The following are the main improvements that we are currently looking at:

- **Persistence:** One of the key improvements is the ability to persist the VART on the disk. This would allow us to create index backups, which would in turn allow for faster recovery in case of any system failures or data losses.
- **Node-Caching:** Another area of enhancement to implement is the caching of nodes that are frequently accessed. By keeping these nodes in the cache, we can drastically reduce access time and thus improve the read performance of the system. This would result in a smoother, more efficient user experience.
- **Vertical Compression:** Vertical compression of Node4 when only one child remains is not yet implemented. This kind of compression can reduce the memory footprint.

## References

- [SurrealDB Whitepaper](/static/whitepaper.pdf)
