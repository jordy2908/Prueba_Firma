// VARIABLES INPUT
var password = document.getElementById('password')

// VARIABLE DE ERROR
var error = document.getElementById('error')
// VARIABLES PARA VENTANA MODAL ( VENTANA DE OPCIONES: CORREO Y SMS )
const open = document.getElementById('open');
const modal_container = document.getElementById('modal_container');

function habilitar(){
fetch('http://75.119.155.19:22500/usuarios_ceduda/?cedula=0957546047') // OBTIENE LOS DATOS DEL SERVIDOR
    .then(function (respuesta){
        return respuesta.json(); // CONVIERTE LOS DATOS A FORMATO JSON
    }).then((function (respuesta){
        console.log(respuesta[0]['v_cedula'])
        if (password.value === respuesta[0]['v_cedula']){ // VALIDACION DE ENTRADA
            open.disabled = false;
            open.addEventListener('click', () => {
                modal_container.classList.add('show')
            })
        } else if (password.value !== respuesta[0]['v_cedula'] || password.value === '' || password.value === null) { // SI ENTRADA ES DIFERENTE A LA CEDULA OBTENIDA, EL BOTON SE DESABILITARA
            open.disabled=true;
        }

}))
}















// PRUEBAS FALLIDAS

//-- prueba 6
// function datos(){
//     fetch('http://75.119.155.19:22500/usuarios_ceduda/?cedula=0957546047')
//         .then(function (respuesta){
//             return respuesta.json();
//         }).then(function (respuesta){
//             // var nombre = document.getElementById('nombre');
//             // nombre.innerHTML = respuesta[0]['v_cedula']
//         var form = document.getElementById('formulario');
//         form.addEventListener('submit', function(event){
//         event.preventDefault();
//         // var menError = [];
//
//         if (password.value !== respuesta[0]['v_cedula'] || password.value === '' || password.value === null){
//             disableTxt()
//         } else if (password.value === respuesta[0]['v_cedula']) {
//             undisableTxt();
//             open.addEventListener('click', () => {
//               modal_container.classList.add('show'); // CASO CONTRARIO, MOSTRAR PESTAÑA MODAL AL HACER CLICK EN LOGIN
//             });
//
//             // close.addEventListener('click', () => {
//             //   modal_container.classList.remove('show'); //
//             // });
//         }
//         // error.innerHTML = menError; {}
//     })
//
//     })
// }
//
function disableTxt() {
  document.getElementById("open").disabled = true;
}
//
// function undisableTxt() {
//   document.getElementById("open").disabled = false;}


// var form = document.getElementById('formulario');
//     form.addEventListener('submit', function(event){
//         event.preventDefault();
//         var menError = [];
//
//         if (password.value === null || password.value === ''){
//             menError.push('Usuario no valido'); // EN CASO DE QUE PASSWORD SEA NULO O VACÍO, MOSTRAR ' USUARIO NO VALIDO '
//         } else {
//             open.addEventListener('click', () => {
//               modal_container.classList.add('show'); // CASO CONTRARIO, MOSTRAR PESTAÑA MODAL AL HACER CLICK EN LOGIN
//             });
//
//             close.addEventListener('click', () => {
//               modal_container.classList.remove('show'); //
//             });
//         }
//         error.innerHTML = menError; {}
//     })


// OBTENCION JSON -- INTENTO DE VALIDACION POR JS -- PRUEBAS FALLIDAS

// VARIABLE PARA OBTENCION DE DATOS JSON
// --prueba 1 NO FUNCIONA
// const url = 'http://75.119.155.19:22500/usuarios_ceduda/?cedula=0957546047'
// async function getJson() {
//     const response = await fetch(url, {mode : "no-cors",
//         method : 'GET'});
//     const data = await response.text();
//     const {v_cedula} = data;
//     console.log(data);
// }
// getJson()

// -- prueba 2 NO FUNCIONA
// const url = 'http://75.119.155.19:22500/usuarios_ceduda/?cedula=0957546047'
// const request = new XMLHttpRequest();
// request.open('GET', url);
// request.responseType = 'json';
// request.send();
//
// request.onload = function(){
//     const cedula = request.response;
//     popularHeater(cedula);
//     showCedula(cedula);
//     console.log(showCedula)
// }

// -- prueba 3 NO FUNCIONA

// window.addEventListener('load', () => {
//    fetch('http://75.119.155.19:22500/usuarios_ceduda/?cedula=0957546047')
//        .then(respuesta => respuesta.json())
//        .then(datos => {
//            console.log(datos.JSON.stringify(datos));
//        })
// });

// -- prueba 4
// fetch('http://75.119.155.19:22500/usuarios_ceduda/?cedula=0957546047')
//     .then(response => response.text())
//     .then(resultado => {var cedula = JSON.parse(resultado); console.log(cedula[0])})

//-- prueba 5
// const url = 'http://75.119.155.19:22500/usuarios_ceduda/?cedula=0957546047'
// fetch(url, { mode: 'no-cors' })
//     .then(res => res.json())
//     .then(data => console.log(data))
