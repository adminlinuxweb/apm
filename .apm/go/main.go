package main

import (
  "fmt"
  "os"
  "time"
  "os/exec"
  "io/ioutil"
  "log"
)

func pwd() {
  pwd, err := os.Getwd()
	if err != nil {fmt.Println(err)}
	fmt.Println(pwd
}

func ls() {
  files, err := ioutil.ReadDir("./")
  if err != nil {log.Fatal(err)}
  for _, f := range files {fmt.Println(f.Name())}
}

func shell() {
  var command string
  
}

func main() {
  
}
