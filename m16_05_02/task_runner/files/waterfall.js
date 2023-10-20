function delay() {
  return new Promise((resolve) =>
    setTimeout(() => {
      resolve()
      console.log('!!!')
    }, 1000),
  )
}

function waterfall(list) {
  return list.reduce((promise, fn) => {
    return promise.then(() => fn())
  }, Promise.resolve())
}

waterfall([delay, delay, delay])
