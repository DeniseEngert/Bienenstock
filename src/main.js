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
        $navbarDropdowns.forEach((el) => {
          el.parentNode.classList.remove('is-active')
        })
        const target = el.parentNode;
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
    dygraphs.push(
      new Dygraph(
        el, // div
        csvUrl, // path to CSV file
        {}          // options
      )
    )
  })

})