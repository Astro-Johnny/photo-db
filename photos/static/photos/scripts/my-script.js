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

//Upload modal image display start
function triggerFileInput() {
    document.getElementById('img').click();
}

function displayImage(input) {
    var file = input.files[0];

    if (file) {

        var reader = new FileReader();

        reader.onload = function (e) {
            document.getElementById('add-new-filename').innerHTML = file.name;
            document.getElementById('uploadedImage').src = e.target.result;
            document.getElementById('click').style.display = "none";
        };

        reader.readAsDataURL(file);
    }
}
//Upload modal image display end

function submitForm(identity){
    const el = document.getElementById(identity)
    if (!el.checked && window.location.href.includes("options") && !window.location.href.includes("&")) {
        window.location.href = "/"
        return;
    }
    document.getElementById("sideNavigation").submit();
}

//Photo modal

const photoModal = document.getElementById("photoModal");
const closePhotoModal = document.getElementById("closePhotoModal");
const body = document.getElementsByTagName('body')[0];

if (window.location.href.includes("photo_")){
    photoModal.style.display = "block";
    body.style.overflow = "hidden";
}

if (closePhotoModal !== null){
    closePhotoModal.onclick = function() {
        photoModal.style.display = "none";
        body.style.overflow = "auto";
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

//Upload Modal

const uploadModal = document.getElementById("uploadModal");
const openUploadModal = document.getElementById("openUploadModal");
const closeUploadModal = document.getElementById("closeUploadModal");

openUploadModal.onclick = function() {
    uploadModal.style.display = "block";
    body.style.overflow = "hidden";
}

closeUploadModal.onclick = function() {
    uploadModal.style.display = "none";
    body.style.overflow = "auto";
}

//Exit Modals

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    if (event.target == uploadModal) {
        uploadModal.style.display = "none";
        body.style.overflow = "auto";
    }
        body.style.overflow = "auto";
    }

    if (event.target == photoModal) {
        photoModal.style.display = "none";
        body.style.overflow = "auto";
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

//Submit Form For Modals

function submitModalForm(data) {
    const modalForm = document.getElementById("modalForm");

    if (data === "save"){
        const filename = document.getElementById("filename")
        const newFilename = document.getElementById("new-filename")
        filename.value = newFilename.innerText
    }else if (data === "addPhoto"){
        if (!window.location.href.includes("options")) {
            modalForm.action = window.location.href + "/options"
        }
        const filename = document.getElementById("add-filename")
        const new_filename = document.getElementById("add-new-filename")
        filename.value = new_filename.innerText
    }
    modal_form.submit()
        const newFilename = document.getElementById("add-new-filename")
        filename.value = newFilename.innerText
    }
    modalForm.submit()
}