

var firebaseConfig = {
    apiKey: "AIzaSyBeRJyVhFX0I7OVIgvfRrMl5Uu2dEKB35E",
    authDomain: "chat-b5825.firebaseapp.com",
    databaseURL: "https://chat-b5825.firebaseio.com",
    projectId: "chat-b5825",
    storageBucket: "chat-b5825.appspot.com",
    messagingSenderId: "1043486002375",
    appId: "1:1043486002375:web:6cbe99c16f4328efc6c2e2",
    measurementId: "G-RER7P0N2J0"
  };
// Initialize Firebase
firebase.initializeApp(firebaseConfig);


document.addEventListener('DOMContentLoaded', function () {
    var Modalelem = document.querySelector('.modal');
    var instance = M.Modal.init(Modalelem);
    instance.open();
});

$( "#cl" ).click(function() {
    document.getElementById("user").value = document.getElementById("users").value;
    var msgs = document.getElementById("msgs");
    firebase.database().ref('chat').on('value', function(snp) {
        var u = document.getElementById('user');
        msgs.innerHTML = '';
        
        snp.forEach(function(e) {
            var x = e.val();
            if(x.txt == " salir"){
                msgs.innerHTML += `<div class="center gray">
                <p>${x.user} ha salido</p></div><br>`

            }
            else{
                if (x.user != u.value && x.txt != " salir") {
                    msgs.innerHTML += `<div class="bubble bubble-bottom-left">
                    <p><b>${x.user}</b>: ${x.txt}</p></div><br>`
                } else {
                    msgs.innerHTML += `<div class="bubble2 bubble-bottom-left">
                    <p><b>${x.user}</b>: ${x.txt}</p></div><br>`
                }
            }
        })
    });
});

var data = {'message': "",
            'user': ""}

$("#send").click(function() {
    var msg = document.getElementById('msg');
    var aux = msg.value;
    var usr = document.getElementById('user');
    var auxusr = usr.value;
    data['message'] = aux;
    data['user'] = auxusr;
    $.ajax({
        url: "/_get_data/",
        type: "POST",
        data: JSON.stringify(data),
        dataType: "json",
        success:function(resp){
            $('#response').append(resp.data);    
        }
    });
    $('#msg').val('');
    $("#msg").data("emojioneArea").setText('');
});



