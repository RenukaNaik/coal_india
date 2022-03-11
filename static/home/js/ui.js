document.addEventListener('DOMContentLoaded', function() {
    // nav menu
    const menus = document.querySelectorAll('.side-menu');
    M.Sidenav.init(menus, {edge: 'right'});
    // add recipe form
    // M.Sidenav.init(forms, {edge: 'left'});
    // forms.addEventListener(click)

  });


  const add_btn = document.querySelector('.add-btn');
  const close_btn = document.querySelector('.close-btn');
  const form = document.querySelector('.side-form');
  const capture_div = document.querySelector('.capture-div')
  const videoPlayer = document.querySelector('#player');
  const canvasElement = document.querySelector('#canvas');
  const captureButton = document.querySelector('#capture-btn');
  const imagePicker = document.querySelector('#image-picker');
  const imagePickerArea = document.querySelector('#pick-image');


  const locationBtn = document.querySelector('#location-btn');
  const locationLoader = document.querySelector('#location-loader');
  const latInput = document.querySelector('#lat');
  const lngInput = document.querySelector('#lng');


  const capture_btn = document.querySelector('.capture-btn');
  const upload_btn = document.querySelector('.upload-btn');
  const image_options = document.querySelector('.image-options');
  const upload_section = document.querySelector('.upload-section');
  locationBtn.addEventListener('click',()=>{
    if (!('geolocation' in navigator)) {
      return;
    }

    locationBtn.style.display = 'none';
    locationLoader.style.display = 'block';
    
    // capture_div.style.display = 'none';

    navigator.geolocation.getCurrentPosition(position =>{
      locationBtn.style.display = 'inline-block';
      locationLoader.style.display = 'none';

      fetchedLocation = {lat: position.coords.latitude, lng: position.coords.longitude};
      latInput.value = `${fetchedLocation.lat.toFixed(4)}`
      lngInput.value = `${fetchedLocation.lng.toFixed(4)}`
    },(err) =>{
      locationBtn.style.display = 'inline-block';
      locationLoader.style.display = 'none';
  
    alert('Please allow location access to proceed!');

      fetchedLocation = {lat: 0, lng: 0};
    },{timeout:7000})
  })
  
   getCamera = async () => {
    let devices = await navigator.mediaDevices.enumerateDevices()
    camaras = devices.filter(device => device.kind === 'videoinput')
    deviceID= camaras[camaras.length -1].deviceId
    // console.log(deviceID)
    return deviceID
  }
  const initializeMedia = () =>{
    
    if(!('mediaDevices' in navigator)){   // if mediaDevices not in navigator create ownpolyfill
      navigator.mediaDevices = {};
      console.log(navigator)
    }

    if(!('getUserMedia' in navigator.mediaDevices)){
      navigator.mediaDevices.getUserMedia = function(constraints){
        let getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia;    //for  safari or mozilla
        if(!getUserMedia){
          return Promise.reject(new Error('getUserMedia is not implemented!'));   // if modern getUserMedia not found
        }
        return new Promise((resolve,reject)=>{
          getUserMedia.call(navigator,constraints,resolve,reject);
        })
      }
    }
    getCamera().then(cID=>{
      let streamConstraints={ video: { deviceId: cID } }
      console.log(streamConstraints)

      navigator.mediaDevices.getUserMedia(streamConstraints)
      .then(function(stream){
        videoPlayer.srcObject = stream;
        videoPlayer.style.display = 'block';
      })
      .catch(function(err){
        imagePickerArea.style.display = 'block';
      })
    })
  }

  let picture;
  function dataURItoBlob(dataURI) {
    var byteString = atob(dataURI.split(',')[1]);
    var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0]
    var ab = new ArrayBuffer(byteString.length);
    var ia = new Uint8Array(ab);
    for (var i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }
    var blob = new Blob([ab], {type: mimeString});
    return blob;
  }

  captureButton.addEventListener('click',event =>{
    canvasElement.style.display = 'block';
    videoPlayer.style.display = 'none';
    captureButton.style.display = 'none';

    let context = canvasElement.getContext('2d');
    let canvasWidth = canvas.width;
    let canvasHeight = videoPlayer.videoHeight/(videoPlayer.videoWidth / canvas.width);
    context.drawImage(videoPlayer,0,0,canvasWidth,canvasHeight); // draw image on canvas
    videoPlayer.srcObject.getVideoTracks().forEach(tracks => tracks.stop());   //stop video once image is captured

    // picture = dataURItoBlob(canvasElement.toDataURL());
    picture = canvasElement.toDataURL();
    sendPictureToServer(picture);
  })

  sendPictureToServer = (picture) =>{
    var url = window.location.href;
    $.ajax(
      {
          type:"POST",
          url: url,
          data:{picture: picture},
          success: function( data ) 
          {
              console.log('data')
          }
       })
  }



  
  function openCreatePostModal() {
    form.style.display = 'block';
    captureButton.style.display = 'inline-block';
    initializeMedia();
  }

  function closeCreatePostModal() {
    form.style.display = 'none';
    imagePickerArea.style.display = 'none';
    videoPlayer.style.display = 'none';
    canvasElement.style.display = 'none';
    capture_div.style.display='none';
    upload_section.style.display="none";

    image_options.style.display = 'flex';

  }
  
  add_btn.addEventListener('click', openCreatePostModal);
  close_btn.addEventListener('click', closeCreatePostModal);

  capture_btn.addEventListener('click',()=>{
    capture_div.style.display='block';
    image_options.style.display = 'none';
  })

  upload_btn.addEventListener('click',()=>{
    upload_section.style.display="block";
    image_options.style.display = 'none';

  })