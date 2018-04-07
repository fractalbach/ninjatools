package structInspector

import (
	"errors"
	"fmt"
	"io"
	"os"
	"reflect"
)

var (
	error_DEPTH = errors.New("Invalid Depth Input.  Must be greater than 0.")
)

// FPrettyPrint recursively prints the fields of each field in the structure.
// Each field is further printed until the specified depth has been reached.
// Makes heavy use of the reflect package, so it may unsafe to use this.
//
func FPrettyPrint(w io.Writer, I interface{}, depth int) error {
	if depth <= 0 {
		return error_DEPTH
	}
	initDepth := depth
	doPrint(w, I, depth, initDepth)
	return nil
}

func doPrint(w io.Writer, I interface{}, depth, initDepth int) {
	if depth <= 0 {
		return
	}
	s := reflect.ValueOf(I).Elem()
	typeOfT := s.Type()
	for i := 0; i < s.NumField(); i++ {
		f := s.Field(i)
		tabs := makeTabs(initDepth - depth)

		if !f.CanInterface() {
			continue
		}
		fmt.Printf("%v%d:%s (%s) = %v\n",
			tabs, i, typeOfT.Field(i).Name, f.Type(), f.Interface())

		if f.Kind() == reflect.Struct && f.NumField() > 1 {
			doPrint(w, f, depth-1, initDepth)
		}

	}
}

// PrettyPrint calls FPrettyPrint and writes to Standard Output (Stdout).
func PrettyPrint(i interface{}, depth int) error {
	return FPrettyPrint(os.Stdout, i, depth)
}

// MakeTabs returns a string which contains n * "\t" characters.
func makeTabs(n int) string {
	var tabs string
	for i := 0; i < n; i++ {
		tabs += "\t"
	}
	return tabs
}
