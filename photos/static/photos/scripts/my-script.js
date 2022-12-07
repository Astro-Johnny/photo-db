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

const all_inputs = document.getElementsByTagName('INPUT');
console.log(all_inputs)
for (let i = 0; i < all_inputs.length; i++) {
    const input = all_inputs[i]
    if(input.type === "checkbox"){
        input.check = false
    }
}

function submitForm(identity){
    const el = document.getElementById(identity)
    el.checked = true
    document.getElementById("myForm").submit();
}
