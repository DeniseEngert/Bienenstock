// Main CSS
require('../scss/styles.sass');

// Dygraph
import initNavbars from './navbar'
import initDygraphs from './dygraphs'
import initToggles from './toggles'
import initFileInputFields from './fileInputFields'

document.addEventListener('DOMContentLoaded', () => {
  initNavbars();
  initDygraphs();
  initToggles();
  initFileInputFields();
})
