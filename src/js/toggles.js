class Toggle {
  constructor(el) {
    this.el = el;
    this.target = document.querySelector(el.dataset.target);
    if (this.target) {
      this.el.addEventListener('click', () => {
        this.target.classList.toggle('is-active')
      })
    }
  }
}

function initToggles() {
  const toggles = document.querySelectorAll('.js-toggle')

  if (toggles.length > 0) {
    toggles.forEach((el) => {
      new Toggle(el);
    })
  }
}

export default initToggles
