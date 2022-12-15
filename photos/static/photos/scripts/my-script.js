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

const modal = document.getElementById("myModal");
const btn = document.getElementById("myBtn");
const span = document.getElementsByClassName("close-upload")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

const imgModal = document.getElementById("imgModal");

if (window.location.href.includes("photo_")){
    imgModal.style.display = "block";
}

const imgSpan = document.getElementsByClassName("close-photo")[0];

if (imgSpan !== undefined){
    imgSpan.onclick = function() {
        imgModal.style.display = "none";
        if (window.location.href.includes("&")){
            tagList = window.location.href.split("&")
            tagList.pop()
            path = tagList.join("&")
        } else {
            path = window.location.origin
        }

        window.location.replace(path)
    }
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }

    if (event.target == imgModal) {
        imgModal.style.display = "none";
        if (window.location.href.includes("&")){
            tagList = window.location.href.split("&")
            tagList.pop()
            path = tagList.join("&")
        } else {
            path = window.location.origin
        }

        window.location.replace(path)
    }
}

function submitModalForm() {
    if (window.location.href.includes("photo_")){
        if (window.location.href.includes("&")){
            tagList = window.location.href.split("&")
            tagList.pop()
            path = tagList.join("&")
        } else {
            path = window.location.origin
        }
    }
    const modal_form = document.getElementById("modal-form");
    modal_form.action = path
    modal_form.submit()
}