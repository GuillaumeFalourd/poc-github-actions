// First Go program
package main

import "fmt"

// Main function
func main() {
	SetTag("1.4.1")
}

func SetTag(value string) {
	fmt.Printf(`::set-output name=repo_tag::%s`, value)
	fmt.Print("\n")
	fmt.Printf(`::set-output name=ecr_tag::%s`, "v"+value)
	fmt.Print("\n")
}
