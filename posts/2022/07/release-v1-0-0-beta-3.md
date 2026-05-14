---
title: "Release v1.0.0-beta.3"
slug: "release-v1-0-0-beta-3"
date: "2022-07-24T00:00:00.000Z"
categories:
  - "releases"
read_time: "1 min read"
summary: "Log root authentication configuration status on server startup, ensure CORS headers are set on all HTTP responses even when request fails with an error, and more..."
source: "https://surrealdb.com/blog/release-v1-0-0-beta-3"
cover: "../../assets/27e83d8ba8ca369a.jpg"
---

# Release v1.0.0-beta.3

![Release v1.0.0-beta.3](../../assets/27e83d8ba8ca369a.jpg)

- Enable years as a unit in durations (1y)
- Log root authentication configuration status on server startup
- Ensure CORS headers are set on all HTTP responses even when request fails with an error
- Improve syntax for defining futures: fn::future -> changed to <future>
- Improve syntax for defining embedded functions: fn::script -> () => changed to function()
- Ensure root authentication is completely disabled when -p or --pass cli arguments are not specified

/releases
