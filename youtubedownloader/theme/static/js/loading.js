
console.log('hyello')

var elements = document.getElementsByClassName("get");


for (var i=0; i<elements.length; i++){
        elements[i].addEventListener("click", ()=>{

            swal.fire({
                title: "Downloading...",
                text: "Please wait",
                iconHtml: '<img src= "https://media0.giphy.com/media/3oEjI6SIIHBdRxXI40/200w.gif?cid=82a1493bd21t8n5ya4lxnm4o9lmcd7ms8c810ch79cpowsju&rid=200w.gif&ct=g" width=100px height=100px/>',
                showConfirmButton: false,
                allowOutsideClick: false
              });
            })


}
