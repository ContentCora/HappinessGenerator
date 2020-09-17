//wait until button "Add item" is clicked, then deliver a success message
const add = document.getElementById("add");

function success_message() {
    //prompt("Your note was added to the list");
    Swal.fire('Your item was added to the list of happiness!');
}

add.addEventListener("click", success_message); 