var dropdown = document.getElementsByClassName("dropdown-btn");

for (var i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
        }
    });
}

$("#cb").click(function(e) {
  e.preventDefault();
  $('#mode').click(function(e) {
    e.stopPropagation();
  })
  $("#mode").prop("checked", !$("#mode").prop("checked"));
})

let allLinks = document.querySelectorAll("a");
console.log(allLinks)
console.log(1)

function submitForm(){
    //document.getElementsById("myForm").submit()
}