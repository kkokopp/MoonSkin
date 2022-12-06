
  function showPreview(event){
    if(event.target.files.length > 0){
      var src = URL.createObjectURL(event.target.files[0]);
      var preview = document.getElementById("preview-image");
      preview.src = src;
      preview.style.display = "block";
      return true;
    }
  }

  function cekImage(form){
    const img = document.getElementsByName("preview-image")
    if(img.values == 0){
      alert("Hasur Upload Foto Kulit Dahulu!");
      return false;
    }
  }

  function myFunction() {
    var x = document.getElementById("menu-bar");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }

  /* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}

// 'user strict';

// const video = document.getElementById('video');
// const canvas = document.getElementById('canvas');
// const snap = document.getElementById('snap');
// const errorMsgElement = document.getElementById('spanErrorMsg');

// const constrains = {
//   audio: true,
//   video:{
//     width: 1280, height: 720
//   }
// };

// async function init(){
//   try{
//     const stream = await navigator.mediaDevices.getUserMedia(constrains);
//     handleSource(stream);
//   }
//   catch(e){
//     errorMsgElement.innerHTML = 'navigator.getUserMedia.error:${e.toString()}';
//   }
// }

// function handleSource(stream){
//   window.stream = stream;
//   video.srcObject = stream;
// }

// init();

// var context = canvas.getContext('2d');
// snap.addEventListener("click", function(){
//   context.drawImage(video, 0,0, 649, 480);
// });

