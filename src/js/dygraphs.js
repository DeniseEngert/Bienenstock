import Dygraph from 'dygraphs';

let dygraphs = []

function initDygraphs() {
  const dygraphDivs = document.querySelectorAll('.js-dygraph');

  dygraphDivs.forEach((el) => {
    const csvUrl = el.dataset.csvurl;
    setTimeout(() => {
      dygraphs.push(
        new Dygraph(
          el, // div
          csvUrl, {
            showRangeSelector: true,
            title: 'T and RH in a nuc bee hive',
            titleHeight: 20,
            xlabel: 'Date/Time',
            xLabelHeight: 18,
            ylabel: 'T[°C] / RH [%]',
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
