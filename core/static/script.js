const editKey = document.querySelectorAll(".option-act");
const editOptions = document.querySelectorAll('.option-list');


for (let i = 0; i < editKey.length; i++) {
    editKey[i].addEventListener('click',function(){
        editOptions[i].classList.toggle('option-list-hidden');
    });
    };

