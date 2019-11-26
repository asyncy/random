const http = require('http')
const { boolean, string, integer, list } = require('./helpers')

const { PORT = 8080 } = process.env

http
  .createServer((request, response) => {
    let output = { result: null }
    let statusCode = 200

    const url = new URL(`http://localhost${request.url}`)

    switch (url.pathname) {
      case '/boolean':
        output.result = boolean()
        break
      case '/integer':
        const low = url.searchParams.get('low') || 1
        const high = url.searchParams.get('high') || 10
        output.result = integer(low, high)
        break
      case '/string':
        const length = url.searchParams.get('length') || 10
        output.result = string(length)
        break
      case '/list':
        const type = url.searchParams.get('type') || 'integer'
        const listLength = url.searchParams.get('length') || 10
        const stringLength = url.searchParams.get('stringLength') || 10
        const integerLow = url.searchParams.get('integerLow') || 1
        const integerHigh = url.searchParams.get('integerHigh') || 100
        output.result = list(type, listLength, stringLength, integerLow, integerHigh)
        break
      default:
        statusCode = 500
        output.result = { error: `Unrecognized URL path: ${request.url}` }
    }

    response.writeHead(statusCode, { 'Content-Type': 'application/json' })
    response.end(JSON.stringify(output), 'utf-8')
  })
  .listen(PORT)
console.log(`Server running at http://127.0.0.1:${PORT}`)
