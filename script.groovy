#!/usr/bin/env groovy

import groovy.json.JsonSlurper

// Read the JSON file
def jsonFile = new File('Config.json')
def jsonSlurper = new JsonSlurper()
def configs = jsonSlurper.parse(jsonFile)

// Calculate the total number of bundles
def totalBundles = configs.bundles.size()
println "Total Array Size = " + totalBundles

// Initialize an array for product names
def productName = new Object[totalBundles]

// Example to fill the array (assuming 'bundles' contains objects with a 'name' property)
configs.bundles.eachWithIndex { bundle, index ->
    productName[index] = bundle.product.name
}

// Print the product names
productName.each { name ->
    println "Product Name: " + name
}