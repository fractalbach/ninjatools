// simpleServer simply serves all of the files in the folder that it is ran in.
// The address (ip:port) can be specified using the "-a" flag,
// and the index/root/homepage file can be specified using the "-index" flag.
// all other files will be served by their filenames.
//
// Requests are logged and include some basic, useful, information.
//
package main

import (
	"flag"
	"log"
	"net/http"
)

var (
	home_page = flag.String("index", "index.html", "Home page accessible at root.")
	addr      = flag.String("a", "localhost:8080", "http service address")
)

func main() {
	flag.Parse()

	mux := http.NewServeMux()
	mux.HandleFunc("/", serveIndex)

	s := &http.Server{
		Addr:    (*addr),
		Handler: mux,
	}

	log.Printf("Listening and Serving on %v", (*addr))
	log.Fatal(s.ListenAndServe())
}

//
// serveIndex will serve the index page and all other files based on URL.
// This exposes all folder contents, and makes them accessible by filename.
// All incoming requests will be logged via the "logRequest" function.
//
func serveIndex(w http.ResponseWriter, r *http.Request) {
	logRequest(r)
	if r.URL.Path == "/" {
		http.ServeFile(w, r, *home_page)
		return
	}
	http.ServeFile(w, r, r.URL.Path[1:])
}

//
// logRequest prints out a useful message to the command line log,
// displaying information about the request that was just made to the server.
//
func logRequest(r *http.Request) {
	log.Printf("(%v) %v %v %v", r.RemoteAddr, r.Proto, r.Method, r.URL)
}
