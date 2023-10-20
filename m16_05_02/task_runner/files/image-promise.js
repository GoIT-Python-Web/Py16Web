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
