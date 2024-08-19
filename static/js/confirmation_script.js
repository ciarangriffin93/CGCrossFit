document.addEventListener('DOMContentLoaded', function() {
    var deleteButton = document.querySelector('.btn-delete');
    if (deleteButton) {
        deleteButton.addEventListener('click', function(event) {
            var confirmation = confirm('Are you sure you want to delete? This action cannot be undone.');
            if (!confirmation) {
                event.preventDefault();
            }
        });
    }
});
