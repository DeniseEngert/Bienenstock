class Navbar {

  constructor(el) {
    this.el = el;
    this.burger = this.el.querySelector('.js-navbar-burger');
    this.menu = this.el.querySelector('.js-navbar-menu');
    this.dropdownItems = this.el.querySelectorAll('.has-dropdown');
    this.dropdownToggles = this.el.querySelectorAll('.js-navbar-dropdown');

    this.init()
  }

  init() {
    this.addEventHandlers();

    // hide dropdowns when clicking somewhere else
    document.addEventListener('click', () => {
      this.dropdownItems.forEach((el) => {
        el.classList.remove('is-active');
      })
    })
  }

  addEventHandlers() {
    // Add Burger click event
    this.burger.addEventListener('click', () => {
      this.burger.classList.toggle('is-active');
      this.menu.classList.toggle('is-active');
    });

    // add dropwdown toggle click event
    this.dropdownToggles.forEach(el => {
      el.addEventListener('click', (e) =>{
        e.stopPropagation();
        const target = el.parentNode;
        // hide all other dropdowns
        this.dropdownItems.forEach((dropdownItem) => {
          if (dropdownItem !== target) {
            dropdownItem.classList.remove('is-active');
          }
        });
        target.classList.toggle('is-active');
      });
    });
  }
}

function initNavbars() {
  const navbars = Array.prototype.slice.call(document.querySelectorAll('.js-navbar'), 0)
  if (navbars.length > 0) {
    navbars.forEach((el) => {
      new Navbar(el)
    })
  }
}

export default initNavbars
