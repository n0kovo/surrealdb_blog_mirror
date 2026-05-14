---
title: "Understanding CBOR"
slug: "understanding-cbor"
date: "2024-03-15T00:00:00.000Z"
categories:
  - "engineering"
  - "tutorials"
read_time: "4 min read"
summary: "JSON is the popular kid in school, but CBOR is the new kid who's smaller, faster, and has more tricks up its sleeve!"
source: "https://surrealdb.com/blog/understanding-cbor"
cover: "../../assets/866414876c3203d8.jpg"
---

# Understanding CBOR

![Understanding CBOR](../../assets/866414876c3203d8.jpg)

Data serialisation formats are the backbone of data exchange between different services. JSON (JavaScript Object Notation) has been a popular choice for many developers due to its simplicity and readability. However, CBOR (Concise Binary Object Representation) is emerging as a promising alternative.

In this post, we will look into the details of CBOR, its comparison with JSON, and its benefits, particularly in the context of the Rust programming language - using which SurrealDB is built.

## Understanding Data Serialisation Formats

Data serialisation is the process of converting complex data structures into a format that can be easily stored or transmitted and then reconstructed (deserialised\*)\* later. This is particularly important when data needs to be sent over a network or saved in a file. Common data serialisation formats include XML, JSON, and CBOR.

## What is JSON?

[JSON](https://en.wikipedia.org/wiki/JSON) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is based on a subset of JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C , C#, Java, JavaScript, Perl, Python, and many others.

```json
{
    "name": "Alex Smith",
    "age": 29,
    "hobbies": ["reading", "cycling", "hiking"],
    "contact": {
        "email": "alex.smith@example.com",
        "phone": "123-456-7890"
    }
}
```

## What is CBOR?

CBOR, on the other hand, is a serialisation format that is structurally similar to JSON but which uses a binary instead of text-based format. It aims to have similar simplicity to JSON but smaller size and faster processing. CBOR was developed by the [IETF](https://www.ietf.org) and is described in [RFC 7049](https://www.ietf.org/archive/id/draft-ietf-cbor-7049bis-14.html). It supports a wide variety of types and extends JSON's capabilities by offering more data types and the ability to be self-describing.

For example, a CBOR hex representation for the same JSON document above will look like:

```json
A4                                      # map(4)
   64                                   # text(4)
      6E616D65                          # "name"
   6A                                   # text(10)
      416C657820536D697468              # "Alex Smith"
   63                                   # text(3)
      616765                            # "age"
   18 1D                                # unsigned(29)
   67                                   # text(7)
      686F6262696573                    # "hobbies"
   83                                   # array(3)
      67                                # text(7)
         72656164696E67                 # "reading"
      67                                # text(7)
         6379636C696E67                 # "cycling"
      66                                # text(6)
         68696B696E67                   # "hiking"
   67                                   # text(7)
      636F6E74616374                    # "contact"
   A2                                   # map(2)
      65                                # text(5)
         656D61696C                     # "email"
      76                                # text(22)
         616C65782E736D697468406578616D706C652E636F6D # "alex.smith@example.com"
      65                                # text(5)
         70686F6E65                     # "phone"
      6C                                # text(12)
         3132332D3435362D37383930       # "123-456-7890"
```

## Advantages of CBOR over JSON

While JSON has been the go-to choice for many developers, CBOR offers several advantages that make it a worthy contender:

- **Size**: As a binary format, CBOR is more compact than JSON, which can lead to performance gains in network transmission and storage. The same JSON payload which contains attributes like name, age, and phone are encoded in a compact binary form resulting in fewer bytes compared to JSON representation.
- **Speed**: CBOR can be parsed significantly faster than JSON due to its binary nature.
- **Extensibility**: CBOR supports a broader range of data types than JSON, including binary data, and allows for custom data types.

## Benefits of CBOR in Rust

As you know, Rust is a programming language that runs blazingly fast, prevents segfaults, and guarantees thread safety. When using Rust, CBOR can offer several benefits:

- **Efficiency**: Rust's focus on zero-cost abstractions, move semantics, and efficient C bindings make it a perfect match for the efficient, binary nature of CBOR.
- **Safety**: Rust's emphasis on safety pairs well with CBOR's ability to be self-describing, which can help prevent errors when parsing data.
- **Interoperability**: CBOR's wide support for different data types and extensibility can be leveraged in Rust to create highly interoperable APIs.

## Implementing CBOR in Rust

Rust has a crate called '[ciborium](https://docs.rs/ciborium/latest/ciborium/all.html#functions)' which provides a CBOR implementation for serde, Rust's generic serialisation/deserialisation framework. Here's a simple example of how to serialise and deserialise data using CBOR in Rust:

```rust
use std::io::Cursor;

fn main() {
    // Tuple to be serialized
    let tuple = ("Hello", "World");

    // Serialize the tuple into a vector of bytes
    let mut vec = Vec::new();
    ciborium::ser::into_writer(&tuple, &mut vec).expect("Serialization of tuple");

    //print the serialized representation
    println!("Serialized CBOR: {:?}", vec);

    // Deserialize the CBOR bytes back into a Rust tuple
    let deserialized: (String, String) = ciborium::de::from_reader(&mut Cursor::new(vec))
        .expect("Deserialized back into a Rust tuple");

    // Assert equality (for demonstration, normally you'd use this deserialized data)
    assert_eq!(deserialized, ("Hello".to_string(), "World".to_string()));
    println!("Deserialized Data: {:?}", deserialized);
}
```

## Moving to CBOR at SurrealDB

At SurrealDB, we are always trying to make data accessible in most powerful and efficient way. CBOR brings in that efficiency when you communicate with SurrealDB. There are a couple of notable improvements apart from the stated benefits:

- CBOR allow us to easily tag column types in the responses returned without any overhead. So client SDKs can infer types easily.
- Better communication concerning UUIDs, along with SurrealDB’s recordIDs, durations, decimals, NONE values and dates.

## Conclusion

While JSON has its strengths and is a good choice for many use cases, CBOR's compact size, speed, and extensibility make it a compelling alternative for data serialisation, especially in a language like Rust that values efficiency and safety. By understanding and leveraging these different data serialisation formats, developers can build more efficient, robust, and interoperable software.

Try out [SurrealDB](/install) today to explore the future of multi-model databases and [join our community](https://discord.gg/surrealdb) to share your experience with our team!
