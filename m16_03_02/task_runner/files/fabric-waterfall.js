function delay(ms) {
  return () => {
    return new Promise((resolve) =>
      setTimeout(() => {
        resolve()
        console.log('!!!')
      }, ms),
    )
  }
}

function waterfall(list) {
  return list.reduce((promise, fn) => {
    return promise.then(() => fn())
  }, Promise.resolve())
}

waterfall([delay(3000), delay(1000), delay(2000)])
