const dropdowns = document.getElementsByClassName("dropdown-btn");

for (let i = 0; i < dropdowns.length; i++) {
    dropdowns[i].addEventListener("click", function() {
        this.classList.toggle("active");
        const dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
        }
    });
}

function submitForm(identity){
    const el = document.getElementById(identity)
    if (el.checked) {
        el.removeAttribute("checked")
    } else {
        el.setAttribute("checked", "")
    }
    document.getElementById("myForm").submit();
}
