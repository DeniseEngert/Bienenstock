// Main CSS
require('./scss/styles.sass');

// Dygraph
import Dygraph from 'dygraphs';


document.addEventListener('DOMContentLoaded', () => {
  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.js-navbar-burger'), 0);
  const $navbarDropdowns = Array.prototype.slice.call(document.querySelectorAll('.js-navbar-dropdown'), 0);
  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
      el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = Array.prototype.slice.call(document.querySelectorAll('.js-navbar-menu'), 0)[0];

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });
  }

  if ($navbarDropdowns.length > 0) {
    $navbarDropdowns.forEach(el => {
      el.addEventListener('click', (e) =>{
        e.stopPropagation();
        const target = el.parentNode;
        $navbarDropdowns.forEach((el) => {
          const parent = el.parentNode
          if (parent !== target) {
            parent.classList.remove('is-active');
          }
        })
        target.classList.toggle('is-active');
      });
    });

  // hide dropdowns when clicking somewhere else
  document.addEventListener('click', () => {
    $navbarDropdowns.forEach((el) => {
      el.parentNode.classList.remove('is-active')
    })
  })

  }

  // init dygraphs
  let dygraphs = [];
  const dygraphDivs = document.querySelectorAll('.js-dygraph');

  dygraphDivs.forEach((el) => {
    const csvUrl = el.dataset.csvurl;
    setTimeout(() => {
      dygraphs.push(
        new Dygraph(
          el, // div
          csvUrl, // path to CSV file
          {}          // options
        )
      )
      el.classList.remove('is-loading')
      setTimeout(() => {
        el.classList.add('is-loaded')
      }, 500)
    }, 500)
  })


  // init file input fields
  const fileInputFields = document.querySelectorAll('.file-input');

  fileInputFields.forEach((el) => {
    // remove font awesome icon
    const icon = el.parentNode.getElementsByClassName('file-icon')[0]
    icon.innerHTML = "<span class='icon'><i class='material-icons'>insert_chart</i></span>";

    const fileCta = el.parentNode.getElementsByClassName('file-cta')[0]

    el.addEventListener('change', () => {
      console.log(el);
    const fileName = el.parentNode.getElementsByClassName('file-label')[0]

    if (!fileName) {
      fileLabel.innerHTML = dataArr[0]+ "<span class='file-name'></span>";
    }

    fileName.innerHTML = el.value;
    })
  })


})