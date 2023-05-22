const titleInput = document.querySelector('input[name=title]')
const slugInput = document.querySelector('input[name=slug]')

const slugify = (val) => { // function
    return val.toString().toLowerCase().trim()
        .replace(/&/g,'-and-')  // replace & with '-and-'
        .replace(/[\s\W-]+/g, '-') // replace spaces, non word chars and dashes with '-'
}

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});