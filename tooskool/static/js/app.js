let alertWrappwer = document.querySelector('.alert');
let alertClose = document.querySelector('.alert__close');

if (alertWrappwer) {
    alertClose.addEventListener('click', function() {
        alertWrappwer.style.display = 'none';
    });
}
  
console.log('DOM loaded');

// Event delegation for dynamically loaded elements
document.addEventListener('click', function (e) {
    if (e.target.classList.contains('page-link')) {
        e.preventDefault();
        console.log('Page link clicked');

        const page = e.target.dataset.page;
        const searchForm = document.getElementById('searchForm');

        if (!searchForm || !page) {
            console.error('Search form or page data missing');
            return;
        }

        // Append hidden inputs to the form
        searchForm.innerHTML += `<input value="${page}" name="page" hidden />`;
        const searchQueryInput = searchForm.querySelector('input[name="search_query"]');
        const searchQuery = searchQueryInput ? searchQueryInput.value : '';
        if (searchQuery) {
            searchForm.innerHTML += `<input value="${searchQuery}" name="search_query" hidden />`;
        }
        searchForm.submit();
    }
});
