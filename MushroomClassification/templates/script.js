// script.js
document.getElementById('image-upload').addEventListener('change', async function () {
    const file = this.files[0];
    if (file) {
        // ... (image processing and backend API request) ...

        // Assuming 'result' contains the classification result ('Grade A', 'Grade B', 'Grade C', or 'Rejected')
        switch (result) {
            case 'Grade A':
                showPage('grade-a-page');
                break;
            case 'Grade B':
                showPage('grade-b-page');
                break;
            case 'Grade C':
                showPage('grade-c-page');
                break;
            case 'Rejected':
                showPage('rejected-page');
                break;
            default:
                // Handle unexpected result
                break;
        }
    }
});

function showPage(pageId) {
    // Hide all result pages
    const pages = document.querySelectorAll('.hidden');
    pages.forEach(page => page.style.display = 'none');

    // Show the selected result page
    const selectedPage = document.getElementById(pageId);
    selectedPage.style.display = 'block';
}
