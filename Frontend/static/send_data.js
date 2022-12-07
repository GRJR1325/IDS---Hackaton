function getValue()
{
    // Se obtienen los datos que se mandan del formulario
    var exp = document.getElementById("exp").value;
    var node = document.getElementById("node").value;
    var sql = document.getElementById("sql").value;
    var postgsql = document.getElementById("postgsql").value;
    var aws = document.getElementById("aws").value;
    var ningles = document.getElementById("ningles").value;
    var visap = document.getElementById("visap").value;
    var hofiece = document.getElementById("hofice").value;
    //var estudios = document.getElementById("estudios").value;


    // Se construye un objeto con la librería XMLHttpRequest
    var test_result = new XMLHttpRequest();


    // Se abre una conexión asíncrona
    //test_result.open('POST', URL, true);


    // Se configuran las cabeceras a recibir
    //test_result.setRequestHeader("Accept", "aplication/json");
    //test_result.setRequestHeader("Content-type", "aplication/json");


    // Enviar el request
    //test_result.send();
    //test_result.onload = () => {
        //const response = test_result.responseText;
        //const json = JSON.parse(response);
        //console.log(json["hiring"]);
    //}


    //Se hace la redirección a la página de resultados
    //window.location.replace("resultado.html");
    localStorage.setItem("exp", exp);
    window.location.href="resultado.html";


}

function showValue()
{
    console.log(localStorage.getItem("exp"));
    console.log(node);
    console.log(sql);
    console.log(postgsql);s
    console.log(aws);
}