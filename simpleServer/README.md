# Simple Server

This is a Simple File Server which simply serves all of the files in the folder that is run in.

## How to Install

1.  Install [The Go Programming Language](https://golang.org/)

2.  "Go get" this folder.

    ~~~
    go get github.com/fractalbach/ninjatools/simpleServer
    ~~~



## Usage

~~~
simpleServer [-a IP:PORT] [-index homepage.html]

-a          specifies the server's address.
-index      the file that is reachable from the root.  (aka the home page.)
~~~

- The default server address is localhost:8080
- The default index filename is index.html




## Examples

If you call the command directly, it will run the defaults listed above.
~~~
simpleServer
~~~


To make an outward facing server, you can change the address:
~~~
simpleServer -a :80
~~~


If your index.html file is actually named home.html, then you can use...
~~~
simpleServer -a :80 -index home.html
~~~

