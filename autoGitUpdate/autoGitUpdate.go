// package gitUpdater
package main

import (
	//"fmt"
	"log"
	"os"
	"os/exec"
)

var (
	// How many clones of the github repo to hold onto.
	// Set to 0 to NEVER use git clone.
	// Set to -1 to ALWAYS use git clone and save every update until crash.
	CONFIG_maxSavedOldVersions = 2

	// Endpoint of the repository you want to update.
	CONFIG_githubRepo = "github.com/fractalbach/autoGitUpdate"
)

type thingy struct {
	wrkdir string
}

func main() {

	workingDirectory, err := os.Getwd()
	if err != nil {
		log.Fatal("cannot get working directory.", err)
	}

	log.Println("working directory:", workingDirectory)

	checkForGit()
}

func checkForGit() {
	path, err := exec.LookPath("git")
	if err != nil {
		log.Fatal("git is not installed.", err)
	}
	log.Printf("git is available at %s\n", path)
}

func checkForGitConfig() {

}
