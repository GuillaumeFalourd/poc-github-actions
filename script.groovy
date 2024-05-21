#!groovy

sh 'cat Config.json'
def configs = readJSON(file: 'Config.json')
def totalBundles = configs.bundles.size()
println "Total Array Size =" + totalBundles
def productName = new Object[totalBundles]