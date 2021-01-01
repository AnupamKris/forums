// localStorage.setItem("theme", "true")
function init_dark() {
  let dark = localStorage.getItem("theme")
  var div = document.getElementById('darklight')
  console.log(localStorage.getItem("theme"))
  if (dark == 'true') {
    div.innerHTML = 'D'
    // less.modifyVars({
    //   '@background-color': '#131419',
    //   '@shadow-big': `-5px -5px 10px rgba(255,255,255,0.05),
    //                   5px 5px 15px rgba(0,0,0,0.5)`,
    //   '@shadow-small': `-2px -2px 6px rgba(255,255,255,0.05),
    //                   2px 2px 6px rgba(0,0,0,0.5)`,
    //   '@shadow-small-inset': `inset -2px -2px 6px rgba(255,255,255,0.05),
    //                           inset 2px 2px 6px rgba(0,0,0,0.5)`,
    //   '@color-secondary': '#03a9f4'
    // })
  } else {
    less.modifyVars({
      '@background-color': '#DDDDDD',
      '@shadow-big': `5px 5px 10px #bcbcbc,
                      -5px -5px 15px #fefefe`,
      '@shadow-small': `2px 2px 6px #bcbcbc,
                      -2px -2px 6px #fefefe`,
      '@shadow-small-inset': `inset 2px 2px 6px #bcbcbc,
                              inset -2px -2px 6px #fefefe`,
      '@color-secondary': '#29248e',
      '@color' : '#868686'
    })
    div.innerHTML = 'L'
  }
}

function dark_mode_toggle() {
    var div = document.getElementById('darklight')
    var dark = localStorage.getItem("theme")
    console.log(dark)
    if (dark == "true") {
    //   dark = false
      less.modifyVars({
        '@background-color': '#DDDDDD',
        '@shadow-big': `5px 5px 10px #bcbcbc,
                        -5px -5px 15px #fefefe`,
        '@shadow-small': `2px 2px 6px #bcbcbc,
                        -2px -2px 6px #fefefe`,
        '@shadow-small-inset': `inset 2px 2px 6px #bcbcbc,
                                inset -2px -2px 6px #fefefe`,
        '@color-secondary': '#29248e',
        '@color' : '#aba7a7'

      })
      localStorage.setItem("theme", "false")
      div.innerHTML = 'L'

    } else {
      less.modifyVars({
        '@background-color': '#131419',
        '@shadow-big': `-5px -5px 10px rgba(255,255,255,0.05),
                        5px 5px 15px rgba(0,0,0,0.5)`,
        '@shadow-small': `-2px -2px 6px rgba(255,255,255,0.05),
                        2px 2px 6px rgba(0,0,0,0.5)`,
        '@shadow-small-inset': `inset -2px -2px 6px rgba(255,255,255,0.05),
                                inset 2px 2px 6px rgba(0,0,0,0.5)`,
        '@color-secondary': '#03a9f4',
        '@color' : '#868686'

      })
      localStorage.setItem("theme", "true")
      div.innerHTML = 'D'
    }
}
