---
title: "Getting started with the SurrealDB Go Driver"
slug: "getting-started-with-the-surrealdb-go-driver"
date: "2023-05-05T00:00:00.000Z"
categories:
  - "tutorials"
read_time: "6 min read"
summary: "In our Beta 9 release, we updated our Go driver. In this tutorial, we will learn to build a simple SurrealDB URL shortener using the Go driver. A URL shortener is a very simple yet powerful tool that can help you be more productive."
source: "https://surrealdb.com/blog/getting-started-with-the-surrealdb-go-driver"
cover: "../../assets/0d0c78264bb81fce.jpg"
---

# Getting started with the SurrealDB Go Driver

![Getting started with the SurrealDB Go Driver](../../assets/0d0c78264bb81fce.jpg)

In our Beta 9 release, we updated our Go driver. In this tutorial, we will learn to build a simple SurrealDB URL shortener using the Go driver. A URL shortener is a very simple yet powerful tool that can help you be more productive. URL shorteners are used to condense long URLs into shorter, more manageable links and also to track and analyse a particular website. But that's not it. URL shorteners use databases to store and manage the mappings between the original URLs and their shortened versions.

## Prerequisites

Before you begin, make sure you have the following software installed on your system:

1. Go (version 1.17 or higher): [https://golang.org/doc/install](https://golang.org/doc/install)
1. SurrealDB: [/install](/install)

## Project Structure

Our project will have the following file structure:

```syntax
    ├── README.md
    ├── connectSurreal.sh
    ├── go.mod
    ├── go.sum
    ├── main.go
    ├── repository
        └── repository.go
    ├── shortenUrl.sh
    ├── startSurreal.sh
    ├── urls.db
    ├── useShort.sh
    └── web
        └── web.go
```

## Step 1: Setting Up the Project

Create a new folder for your project, and inside the folder, initialise it as a Go module:

```cli
$ mkdir surreal-urlshortener
$ cd surreal-urlshortener
$ go mod init github.com/yourusername/surreal-urlshortener
```

Replace `yourusername` with your GitHub username or any other namespace you prefer.

## Step 2: Import the SurrealDB Go Driver and other required packages.

### Installation

Install the SurrealDB go driver by running the following command

```cli
go get github.com/surrealdb/surrealdb.go
```

In your `go.mod` file, add the following dependencies:

```go
module github.com/yourusername/surreal-urlshortner

go 1.19

require github.com/surrealdb/surrealdb.go v0.2.1

require (
    github.com/gorilla/websocket v1.5.0 // indirect
    github.com/sirupsen/logrus v1.9.0 // indirect
    golang.org/x/sys v0.0.0-20220715151400-c0bba94af5f8 // indirect
)
```

## How does the URL shortener work?

SurrealDB is at the heart of the URL shortener. It will efficiently map the original URLs to their shortened counterparts. When a user submits a long URL, the shortening service will generate a unique key which is then used to create the shortened URL. This unique key, along with the original URL, will be stored as a new record in the database. When someone accesses the shortened URL, the service will look up the corresponding key in the database, retrieve the original URL, and redirect the user to that destination.

## Step 3: Setting Up the Repository

Create a new file called `repository.go` inside the `repository` folder. This file will contain the `ShortenerRepository` struct and methods to interact with the SurrealDB database. The repository design pattern is responsible for handling the database interactions, such as creating short URLs, retrieving the original URLs from the shortened ones, and managing the database connections. This separation of concerns allows the web service layer to focus on handling HTTP requests and responses without worrying about the details of data access and storage.

```go
package repository


    "fmt"
    logger "github.com/sirupsen/logrus"
    surreal "github.com/surrealdb/surrealdb.go"
)

var log = logger.New()

type ShortenerRepository struct {
    db *surreal.DB
}
```

The `ShortenerRepository` struct is defined with a single field `db` of type `*surreal.DB`, which is a pointer to the SurrealDB database connection.

**1. Connect to SurrealDB**: In order to store the original and shortened links on the SurrealDB database, you first have to establish a connection to the SurrealDB instance and connect to a local database endpoint.

`db, err := surrealdb.New(address)`

```go

func NewShortenerRepository(address, user, password, namespace, database string) (*ShortenerRepository, error) {

    db, err := surreal.New(address)

    if err != nil {
        return nil, fmt.Errorf("failed to connect to database: %s", err)
    }

```

**2. db.Signin**: This method signs in to the SurrealDB instance using the provided credentials (username and password).

`_, err = db.Signin(map[string]string{   "user": "root",   "pass": "root", })`

```go
    _, err = db.Signin(map[string]interface{}{
        "user": user,
        "pass": password,
    })

    if err != nil {
        return nil, fmt.Errorf("failed to sign in: %w", err)
    }
```

**3. db.Use**: You can select the namespace and database to be used for the application.

`_, err = db.Use(namespace, database)`

```go
    _, err = db.Use(namespace, database)

    if err != nil {
        return nil, err
    }

    return &ShortenerRepository{db}, nil

}
```

**4. db.Close**: The close method can be called at the end of the program or during shutdown.

```go
func (r ShortenerRepository) Close() {
    r.db.Close()
}
```

**5. db.Create** : `db.Create` method is used to create a new record in the `urls` table of the database. The first parameter of the function is the table name, in this case, "urls".

The second parameter is a `map[string]interface{}`, which represents the data to be inserted into the new record. The keys of the map correspond to the column names in the `urls` table, and their respective values are the function's input parameters `original` and `shortened`

```go
func (r ShortenerRepository) CreateShortUrl(original string, shortened string) (interface{}, error) {

    return r.db.Create("urls", map[string]interface{}{
        "original": original,
        "shortened": shortened,
    })

}
```

**6. db.Query**: The purpose of this method is to query the database and find the corresponding original URL for a given shortened URL ID. `db.Query` function is called to execute a SurrealQL query on the database. This query selects all columns from the `urls` table where the `shortened` column value matches the provided `$shortened` parameter, and it limits the result to one record.

```go
func (r ShortenerRepository) FindShortenedURL(id string) (interface{}, error) {

    return r.db.Query("SELECT * FROM urls WHERE shortened = $shortened limit 1", map[string]interface{}{
        "shortened": "<http://localhost:8090/>" + id,
    })

}
```

## Step 4: Implementing the Web Service

The `web.go` file will contain the code to handle HTTP requests and responses. There are two main handler functions in this code:

**1. `ShortenURL`**: This function shortens a given URL. When an HTTP request is made to the handler, it expects a form value named "url" to be provided. The function checks if the URL has an "[http://"](http://%22) or "[https://"](https://%22) prefix, and if not, it adds "[https://".](https://%22.) It then generates a shortened URL using the `shortenURL` helper function and saves the mapping in the repository using `ws.repository.CreateShortUrl()`. Finally, it sends the shortened URL as a JSON response to the client.

```go
func (ws webService) ShortenURL(writer http.ResponseWriter, request *http.Request) {

    original := request.FormValue("url")

    if original == "" {
        badRequest(writer, errors.New("url is required"))
        return
    }

    if !strings.HasPrefix(original, "http://") && !strings.HasPrefix(original, "https://") {
        original = "https://" + original
    }

    shortened := shortenURL(ws.redirectAddress)

    log.Tracef("created shortened url '%s' for input '%s'", shortened, original)

    urlMap, err := ws.repository.CreateShortUrl(original, shortened)

    if err != nil {
        internalError(writer, fmt.Errorf("failed to create short url: %+v", err))
        return
    }

    log.Tracef("created url mapping: %+v", urlMap)

    // return json response with shortened url

    writer.Header().Set("Content-Type", "application/json")

    json.NewEncoder(writer).Encode(map[string]string{
        "shortened": shortened,
        "original": original
    })

}
```

**2. `shortenURL`**: This function takes a single parameter, `redirectUrl`, which is the base URL. You generate a 6-character random string by appending a random character to the empty string "s" and then concatenate it to the base URL.

```go
func shortenURL(redirectUrl string) string {

    s := ""

    //rand.Intn](https://rand.intn)(26) returns a random number between 0 and 25. 97 is the ascii value of 'a'. So rand.Intn(26) + 97 returns a random lowercase letter.

    for i := 0; i < 6; i++ {
        s += string(rand.Intn(26) + 97)
    }

    shortendURL := fmt.Sprintf("%s/%s", redirectUrl, s)

    return shortendURL

}
```

**3. `RedirectURL`**: When a shortened URL is accessed, this function redirects the user to the original URL. It does this by extracting the URL's ID from the request path and fetching the original URL from the repository using `ws.repository.FindShortenedURL()`. The user is then redirected to the original URL.

```go

func (ws webService) RedirectURL(writer http.ResponseWriter, request *http.Request) {

    id := request.URL.Path[1:]

    log.Tracef("Generating redirect URL for %s", id)

    data, err := ws.repository.FindShortenedURL(id)

    if err != nil {
        internalError(writer, fmt.Errorf("failed to find shortened url: %+v", err))
        return
    }

    jsonBytes, err := json.Marshal(data)

    if err != nil {
        internalError(writer, fmt.Errorf("failed to marshal shortened url: %+v", err))
        return
    }

    //unmarshal the data

    var results []Result

    err = json.Unmarshal(jsonBytes, &results)

    if err != nil {
        internalError(writer, fmt.Errorf("failed to unmarshal shortened url: %+v", err))
        return
    }

    if len(results) == 0 {
        internalError(writer, errors.New("no results found"))
        return
    }

    something := results[0].URLs

    if len(something) == 0 {
        internalError(writer, errors.New("results did not contain any URLs"))
        return
    }

    originalURL := something[0].Original

    if originalURL == "" {
        internalError(writer, errors.New("original URL is empty"))
        return
    }

    log.Tracef("Translated short '%s' to original '%s'", id, originalURL)

    //redirect to the original url

    http.Redirect(writer, request, originalURL, http.StatusSeeOther)

}
```

## Step 5: The main function.

The main.go function brings together the components implemented in `web.go` and `repository.go` to create a fully functional URL shortener application. The `main.go` file is responsible for initialising the database repository, setting up the web service, and starting the HTTP server to handle incoming requests.

We start by importing the required packages, including those implemented in the `web` and `repository` files. Additionally, we import the `logrus` package for logging and the `http` package for handling HTTP requests.

```go

package main


    "fmt"
    logger "github.com/sirupsen/logrus"
    "github.com/timpratim/surreal-urlshortner/repository"
    "github.com/timpratim/surreal-urlshortner/web"
    "net/http"
)
```

Next, we set up constants for the application, such as the listening port, the redirect address, and the database connection details like URL, namespace, and database name.

```go
const port = 8090

var redirectAddress = fmt.Sprintf("<http://localhost>:%d", port)

const url = "ws://localhost:8000/rpc"

const namespace = "surrealdb-conference-content"

const database = "urlshortner"

var log = logger.New()

func main() {

    log.SetLevel(logger.TraceLevel)

    // Create the database repository that uses SurrealDB to store information

    repository, err := repository.NewShortenerRepository(url, "root", "root", namespace, database)

    if err != nil {
        log.Fatalf("failed to create shortener repository: %+v", err)
    }

    log.Infof("Connected to database")

    // Close connections to the database at program shutdown

    defer func() {
        log.Infof("Closing database")
        repository.Close()
    }()

```

We then define HTTP endpoints and their corresponding handlers, which were implemented in the `web.go` file. In this case, we have two endpoints:

`/shorten`: Handles POST requests to shorten a given URL.

`/`: Handles GET requests for redirection of shortened URLs to their original counterparts.

```go

    // Create the web service

    ws := web.NewWebService(repository, redirectAddress)

    http.HandleFunc("/shorten", ws.ShortenURL)

    http.HandleFunc("/", ws.RedirectURL)

    log.Infof("Listening on port %d", port)

    err = http.ListenAndServe(fmt.Sprintf(":%d", port), nil)

    if err != nil {
        log.Fatalf("failed to listen: %+v", err)
    }

}
```

## Running the URL shortener

To test the URL shortener, we will first start the SurrealDB server on our local machine using the following command.

`surreal sql -c <http://localhost:8000> --ns surrealdb-conference-content --db urlshortner`

Run the URL shortener with the following command

`go run main.go`

We will then run the following bash script using the following command in another terminal

`./shortenURL.sh`

```cli
#!/bin/bash

SVC="<http://localhost:8090>"

if [ -z "$1" ]; then
    LONG="<https://surrealdb.com>"
else
    LONG="$1"
fi

curl -X POST --data "url=$LONG" $SVC/shorten
```

Following is the screenshot of original URL and the shortened URL

![SurrealDB URL shortener](../../assets/c12b01f9413dd03b.jpg)

## Conclusion

In this tutorial, you have successfully built a URL shortener using Go and SurrealDB. You've learned how to set up your project structure, create a connection to the SurrealDB database, create a repository to interact with the database, and implement a web service to handle HTTP requests for shortening and redirecting URLs. You can find the code [here](https://github.com/timpratim/surreal-urlshortner).

By following this tutorial, you have gained a deeper understanding of building web applications using Go and interacting with databases like SurrealDB. This knowledge can be applied to create other web applications or even extend the functionality of this URL shortener. Happy coding!
