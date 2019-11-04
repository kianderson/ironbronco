/* opens the pop up window for the form */
function openForm(curr) {
  document.getElementById(curr).style.display = "block";
}

/* closes the form pop up and cancels adding the member */
function closeForm(curr) {
  document.getElementById(curr).style.display = "none";
}
