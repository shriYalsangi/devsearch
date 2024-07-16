const searchForm = document.querySelector('#searchForm');
const pagination = document.querySelector('.pagination');
const pageLinks = pagination.querySelectorAll('a');

pageLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const page = link.getAttribute('data-page');
    searchForm.insertAdjacentHTML('beforeend', `<input type="hidden" name="page" value="${page}" />`);
    searchForm.submit();

  });
});