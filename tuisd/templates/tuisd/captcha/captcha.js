$("document").ready(function(){
  $("#actualizarCaptcha").trigger("click");
});

$( "#reproducirAudio" ).click(function(){
  var captchaAudio = document.getElementById('audioCaptcha');
  captchaAudio.play();
});


$( "#actualizarCaptcha" ).click(function() {
  url = 'http://localhost:8000'
  $.ajax({
    url: '/servecaptcha/generate_captcha/{{public_key}}/',
    type: 'get',
    dataType: 'json',
    success: function(data) {
      $("#image_captcha").attr("src", url + "/servecaptcha/image/" + data.captcha_id);
      $("#captcha-id").val(data.captcha_id);
      $("#audioCaptcha").attr("src", url + "/servecaptcha/audio/" + data.captcha_id);
    },
    failure: function(data) {
      alert("nada");
    }
  });
});
