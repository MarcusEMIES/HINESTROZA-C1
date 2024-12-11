let customersList = [];
// creamos un objeto con unas caracteristicas que se añadiran a la lista del arreglo 
const objCustomer = {
    nombre: '',
    apellido: '',
    Direccion: '',
    Telefono: '',
    Comentarios: ''
}

let editando = false;
// Aqui estamos creando las constantes que almacenaran los arreglos y enlazarlos a los datos que se introduzcan en el formulario para que recojan de ahi sus elementos
const formulario = document.querySelector('#formulario');
const nombreInput = document.querySelector('#nombre');
const apellidoInput = document.querySelector('#apellido');
const direccionInput = document.querySelector('#direccion');
const telefonoInput = document.querySelector('#telefono');
const comentariosInput = document.querySelector('#comentarios');
const btnAgregar = document.querySelector('#btnAgregar');

// ahora añadimos la funcion al evento submit del boton del formulario, decirle que el formulario addevent listener cuando detecte el submit, que vaya a la funcion validarFormulario que crearemos despues de la siguiente linea.

formulario.addEventListener('submit', validarFormulario);

function validarFormulario(e) {
    e.preventDefault();

    if (nombreInput.value === '' || apellidoInput.value === '' || direccionInput.value === '' || telefonoInput.value === '' || comentariosInput.value === '') {
        alert('fill all the gaps you stupid');
        return;
    }

    if (editando) {
        customer
    }

    // ahora se llamara a la funcion editarCustomer que se comentara hasta crearla 

    if (editando) {
        // editarCustomer
        editando = false;  //en caso contrario inicializamos nuestro objeto objCustomer
    } else {
        objCustomer = Date.now // Date.now , nos obtiene el tiempo en milisegundos y nunca se va a replicar o repetir por eso lo usamos como un id.
        objCustomer.nombre = nombreInput.value;
        objCustomer.apellido = apellidoInput.value;
        objCustomer.direccionInput = direccionInput.value;
        objCustomer.direccionInput = direccionInput.value;
        objCustomer.telefonoInput = telefonoInput.value;
        objCustomer.comentariosInput = comentariosInput.value;

        agregarCustomer();

    }

    // esta funcion se crea para recibir el evento e, y le decimos que e.preventDefault que es para que no se ejecute de forma automatica y verificara que no esten vacios los campos para poder ejecutarse, tambien se le dice que si no rellena los campos que retorne una alerta donde le pida que lo haga , por ultimo le indicamos que tras ejecutar todo ejecute la funcion agregarCustomer.

}

// Crearemos la funcion de agregarCustomer

function agregarCustomer() {// Creamos la funcion 

    customersList.push({ ...objCustomer });// le decimos que a nuestra lista por medio del push agregue el objeto utilizando el spread operator ... para copiar el objeto customer, con esto ya lo agregara , despues creamos la funcion mostrar customers 


    mostrarCustomers();
}

function mostrarCustomers() {
    const divCustomer = document.querySelector('div-customers')// Esto es para tener claro donde agregaremos los elementos html.

    customersList.forEach(customer => {
        const { nombre, apellido, Direccion, Telefono, Comentarios } = customer; // esto recorrera la lista mediante el foreach, y desestructuramos los elemnentos para acceder mas facil a ellos

        const parrafo = document.createElement('p');
        parrafo.textContent = `${nombre}- ${apellido} - ${Direccion} - ${Telefono} - ${Comentarios}`;// le indicamos lo que va a tener el parrafo. de la etiqueta 'p'
        parrafo.dataset.id =id;// para identificar que parrafo hay que eliminar o modificar
        const editarBoton =document.createElement('button');
        editarBoton.onclick=() => cargarCustomer(customer);
        editarBoton.textContent ='Editar';
        editarBoton.classList.add('btn','btn-editar');
        parrafo.append(editarBoton);

        const eliminarBoton =document.createElement('button');
        eliminarBoton.onclick=() => cargarCustomer(customer);
        eliminarBoton.textContent ='Editar';
        eliminarBoton.classList.add('btn','btn-editar');
        parrafo.append(eliminarBoton);

        const hr = document.createElement('hr');

        divCustomers.appendChild();

    });

}