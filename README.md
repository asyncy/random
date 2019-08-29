# _Random Generation_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)

Random generation of boolean, string, integer and list

## Direct usage in [Storyscript](https://storyscript.io/):

##### Boolean
```coffee
>>> random boolean
# result: true
```
##### String
```coffee
>>> random string length:'2'
# result: Kw
```
##### Integer
```coffee
>>> random integer low:'2' high:'50'
# result: 39
```
##### List
```coffee
>>> random list type:'string' length:'5'
# result: ["77FFXXiWP4","yrq8o8xtdt","q5fsCt99LA","s5W4uPqOFY","CYWTdA5xQC"]
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Boolean
```shell
$ omg run boolean
```
##### String
```shell
$ omg run string -a length=<LENGTH_OF_STRING>
```
##### Integer
```shell
$ omg run integer -a low=<LOWEST_NUMBER> -a high=<HIGHEST_NUMBER>
```
##### List
```shell
$ omg run list -a type=<STRING/BOOLEAN/INTEGER> -a length=<LENGTH_OF_LIST> -a stringLength=<LENGTH_OF_STRING> -a integerLow=<LOWEST_NUMBER> -a integerHigh=<HIGHEST_NUMBER>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/random/blob/master/LICENSE).

