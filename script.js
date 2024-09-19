document.addEventListener('DOMContentLoaded', function() {
    // Konfirmasi penghapusan buku
    const deleteLinks = document.querySelectorAll('.delete-link');
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            if (!confirm('Apakah Anda yakin ingin menghapus buku ini?')) {
                e.preventDefault();
            }
        });
    });

    // Highlight baris tabel saat hover
    const tableRows = document.querySelectorAll('table tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseover', function() {
            this.style.backgroundColor = '#e6ffe6';
        });
        row.addEventListener('mouseout', function() {
            this.style.backgroundColor = '';
        });
    });
});