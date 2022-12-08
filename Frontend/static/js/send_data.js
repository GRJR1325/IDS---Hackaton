function getValues()
{
    // Se obtienen los datos que se mandan del formulario
    var exp = document.getElementById("exp").value;
    var node = document.getElementById("node").value;
    var sql = document.getElementById("sql").value;
    var postgsql = document.getElementById("postgsql").value;
    var aws = document.getElementById("aws").value;
    var js = document.getElementById("js").value;
    var ningles = document.getElementById("ningles").value;
    var visap = document.getElementById("visap").value;
    var hofice = document.getElementById("hofice").value;
    var estudios = document.getElementById("estudios").value;

    var pl = {"exp": parseInt(exp), "node": parseInt(node), "sql": parseInt(sql), "postgsql": parseInt(postgsql), "aws": parseInt(aws), "js": parseInt(js), "ningles": parseFloat(ningles), "visap": parseInt(visap), "hofice": parseInt(hofice), "estudios": parseInt(estudios)};

    console.log("Datos: " + JSON.stringify(pl));


    // Se construye un objeto con la librería XMLHttpRequest
    var test_result = new XMLHttpRequest();


    // Se abre una conexión asíncrona
    test_result.open('POST', URI, true);
    console.log("URL:" + URI);


    // Se configuran las cabeceras a recibir
    test_result.setRequestHeader("Accept", "aplication/json");
    test_result.setRequestHeader("Content-type", "aplication/json");


    // Enviar el request
    test_result.send(JSON.stringify(pl));
    test_result.onload = () => {
        const response = test_result.responseText;
        const json = JSON.parse(response);
        console.log(json["hiring"]);
        localStorage.setItem("prob", json["hiring"]);
    }

    console.log(localStorage.getItem("prob"));

    //Se hace la redirección a la página de resultados
    window.location.href="resultado.html";
}


function showProb()
{
    console.log(localStorage.getItem("prob"));
    var proba = document.getElementById("proba");
    proba.innerHTML = localStorage.getItem("prob");
}
