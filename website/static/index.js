function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId})
        }).then((_res) => {
            window.location.href = "/";
        });
}
function markAsDone(noteId) {
    fetch('/mark-done', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId})
        }).then((_res) => {
            window.location.href = "/";
        });
}
function changeDate(date) {
    fetch('/date', {
        method: 'POST',
        body: JSON.stringify({selectedDate: date})
    }).then((_res) => {
            window.location.href = "/";
        });
}

$(document).ready(function() {
    $('#date').datepicker().on('change', function() {
    var selectedDate = $('#date').val();
    //window.alert(selectedDate);
    changeDate(selectedDate);
    // Wykonaj dodatkowe działania po wybraniu daty
});
});