console.log('Hello world!')

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

function loadImage(url) {
  return new Promise((resolve) => {
    const image = new Image()
    image.height = '200'
    image.src = url
    image.addEventListener('load', () => {
      resolve()
    })

    document.body.appendChild(image)
  })
}

function waterfall(list) {
  return list.reduce((promise, fn) => {
    return promise.then(() => fn())
  }, Promise.resolve())
}

const images = [
  'https://i.ytimg.com/vi/qyEzsAy4qeU/maxresdefault_live.jpg',
  'https://wallpaperscraft.com/image/planet_light_spots_space_86643_1920x1080.jpg',
  'https://cdn.spacetelescope.org/archives/images/wallpaper2/heic1509a.jpg',
]

const promises = images.map((url) => {
  return () => loadImage(url)
})

waterfall(promises).then(() => console.log('все картинки загружены'))

