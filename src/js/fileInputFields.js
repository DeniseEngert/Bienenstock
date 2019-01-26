import { readCookie } from './utils'

function initFileInputFields() {
  // init file input fields
  const fileInputFields = document.querySelectorAll('.file-input');

  fileInputFields.forEach((el) => {

    const icon = el.parentNode.querySelector('.file-icon')
    const fileNameEl = el.parentNode.querySelector('.file-label')
    const lang = readCookie('django_language')

    // insert line break before element
    el.parentNode.insertBefore(document.createElement("br"), el);

    // only change language if not set to 'en'
    if (lang !== 'en') {
      fileNameEl.innerHTML = "Wähle Datei";
    }

    // replace font awesome icon
    icon.innerHTML = "<span class='icon'><i class='material-icons'>cloud_upload</i></span>";

    // on change, replace text in file name element value according to selected file
    el.addEventListener('change', () => {

      if (!fileNameEl) {
        fileLabel.innerHTML = dataArr[0]+ "<span class='file-name'></span>";
      }

      // only use file name, not path (remove fakepath etc.)
      const parts = el.value.split("\\")
      fileNameEl.innerHTML = parts[parts.length - 1 ];
    })
  })
}

export default initFileInputFields
