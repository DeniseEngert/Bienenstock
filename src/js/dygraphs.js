import Dygraph from 'dygraphs';

let dygraphs = []

function initDygraphs() {
  const dygraphDivs = document.querySelectorAll('.js-dygraph');

  dygraphDivs.forEach((el) => {
    const csvUrl = el.dataset.csvurl;
    const labelX = el.dataset.labelx;
    const labelY = el.dataset.labely;
    setTimeout(() => {
      dygraphs.push(
        new Dygraph(
          el, // div
          csvUrl, {
            showRangeSelector: true,
            titleHeight: 20,
            xlabel: labelX,
            xLabelHeight: 18,
            ylabel: labelY,
            yLabelWidth: 18,
            labelsSeparateLines: true,
          }
        )
      )
      el.classList.remove('is-loading')
      setTimeout(() => {
        el.classList.add('is-loaded')
      }, 500)
    }, 500)
  })
}

export default initDygraphs

