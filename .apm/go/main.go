package main

import (
  "fmt"
  "os"
  "time"
  "os/exec"
)

func pwd() {
  pwd, err := os.Getwd()
  if err != nil {
    fmt.Println(err)
  }
  fmt.Println(pwd)
}

func ls() {
  
}

func shell() {
  var command string
  
}

func main() {
  
}
