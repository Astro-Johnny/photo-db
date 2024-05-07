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

//Camera modal

const cameraModal = document.getElementById("cameraModal");
const openCameraModal = document.getElementById("openCameraModal");
const closeCameraModal = document.getElementById("closeCameraModal");

openCameraModal.onclick = function() {
    uploadModal.style.display = "none";
    cameraModal.style.display = "block";
    body.style.overflow = "hidden";
}

closeCameraModal.onclick = function() {
    cameraModal.style.display = "none";
    body.style.overflow = "auto";
}

//Event modal

const eventModal = document.getElementById("eventModal");
const openEventModal = document.getElementById("openEventModal");
const closeEventModal = document.getElementById("closeEventModal");

openEventModal.onclick = function() {
    uploadModal.style.display = "none";
    eventModal.style.display = "block";
    body.style.overflow = "hidden";
}

closeEventModal.onclick = function() {
    eventModal.style.display = "none";
    body.style.overflow = "auto";
}

//Film modal

const filmModal = document.getElementById("filmModal");
const openFilmModal = document.getElementById("openFilmModal");
const closeFilmModal = document.getElementById("closeFilmModal");

openFilmModal.onclick = function() {
    uploadModal.style.display = "none";
    filmModal.style.display = "block";
    body.style.overflow = "hidden";
}

closeFilmModal.onclick = function() {
    filmModal.style.display = "none";
    body.style.overflow = "auto";
}

//Exit Modals

window.onclick = function(event) {
    if (event.target == uploadModal) {
        uploadModal.style.display = "none";
        body.style.overflow = "auto";
    }

    if (event.target == cameraModal) {
        cameraModal.style.display = "none";
        body.style.overflow = "auto";
    }

    if (event.target == eventModal) {
        eventModal.style.display = "none";
        body.style.overflow = "auto";
    }

    if (event.target == filmModal) {
        filmModal.style.display = "none";
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
        const newFilename = document.getElementById("add-new-filename")
        filename.value = newFilename.innerText
    }else if (data === "addCamera"){
        if (!window.location.href.includes("options")) {
            modalForm.action = window.location.href + "/options"
        }
        const modelInput = document.getElementById("modelInput")
        const addModel = document.getElementById("addModel")
        modelInput.value = addModel.innerText
    }else if (data === "addEvent"){
        if (!window.location.href.includes("options")) {
            modalForm.action = window.location.href + "/options"
        }
        const addEventNameInput = document.getElementById("addEventNameInput")
        const addEventName = document.getElementById("addEventName")
        addEventNameInput.value = addEventName.innerText

        const addPlaceInput = document.getElementById("addPlaceInput")
        const addPlace = document.getElementById("addPlace")
        addPlaceInput.value = addPlace.innerText
    }else if (data === "addFilm"){
        if (!window.location.href.includes("options")) {
            modalForm.action = window.location.href + "/options"
        }
        const addFilmNameInput = document.getElementById("addFilmNameInput")
        const addFilmName = document.getElementById("addFilmName")
        addFilmNameInput.value = addFilmName.innerText

        const addISOInput = document.getElementById("addISOInput")
        const addISO = document.getElementById("addISO")
        addISOInput.value = addISO.innerText

        const addExposuresInput = document.getElementById("addExposuresInput")
        const addExposures = document.getElementById("addExposures")
        addExposuresInput.value = addExposures.innerText
    }
    modalForm.submit()
}