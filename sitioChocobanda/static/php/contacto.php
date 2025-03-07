<?php

// Conectar a la base de datos de Django
$servername = "localhost";
$username = "tu_usuario";
$password = "tu_contraseña";
$dbname = "nombre_de_tu_base_de_datos";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Obtener el correo electrónico de contacto desde la base de datos
$sql = "SELECT correo_electronico FROM sitiochocobanda_ajustespagina LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Obtener el correo electrónico
    $row = $result->fetch_assoc();
    $contact_email = $row['correo_electronico'];
} else {
    echo("No se encontró el correo electrónico de contacto.");
}

// Procesar el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $apellido = $_POST['apellido'];
    $email = $_POST['email'];
    $comentario = $_POST['comentario'];
    $asunto = 'Contacto chocobanda: ' . $_POST['asunto'];

    $header = "From: noreply@chocobanda.com" . "\r\n" .
              "Reply-To: $email" . "\r\n" .
              "X-Mailer: PHP/" . phpversion() . "\r\n" .
              "Content-Type: text/html; charset=ISO-8859-1" . "\r\n";

    // Ruta del archivo de texto donde se almacenarán los datos
    $archivo = 'datos.txt';

    // Verificar si el archivo ya existe
    if (file_exists($archivo)) {
        // Si el archivo existe, abrirlo en modo de escritura al final
        $fp = fopen($archivo, 'a');
    } else {
        // Si el archivo no existe, crearlo y abrirlo en modo de escritura
        $fp = fopen($archivo, 'w');
    }

    // Crear la cadena de texto con los datos del formulario
    $cadena = $nombre . ' | ' . $apellido . ' | ' . $email . ' | ' . $asunto . ' | ' . $comentario . PHP_EOL;

    // Escribir la cadena de texto en el archivo
    fwrite($fp, $cadena);

    // Cerrar el archivo
    fclose($fp);

    // Configurar los datos para el envío del mail
    $destinatario1 = $contact_email;
    $destinatario2 = $email;

    // Cuerpo del mail 1
    $cuerpo1 = '<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Detalles del formulario de contacto</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                font-size: 14px;
                line-height: 1.5;
                color: #333;
            }
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid #ccc;
                padding: 8px;
            }
            th {
                background-color: #f7f7f7;
                font-weight: bold;
                text-align: left;
            }
            td {
                vertical-align: top;
            }
        </style>
    </head>
    <body>
        <h1>Detalles del formulario de contacto</h1>
        <table>
            <tr>
                <th>Nombre:</th>
                <td>' .$nombre. '</td>
            </tr>
            <tr>
                <th>Apellido:</th>
                <td>' .$apellido. '</td>
            </tr>
            <tr>
                <th>Email:</th>
                <td>' .$email. '</td>
            </tr>
            <tr>
                <th>Asunto:</th>
                <td>' .$asunto. '</td>
            </tr>
            <tr>
                <th>Comentario:</th>
                <td>' .$comentario. '</td>
            </tr>
        </table>
    </body>
    </html>';

    // Cuerpo del mail 2
    $cuerpo2 = '<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/all.css" integrity="sha384-3AB7yXWz4OeoZcPbieVW64vVXEwADiYyAEhwilzWsLw+9FgqpyjjStpPnpBO8o8S" crossorigin="anonymous">
        <title>Gracias por contactarnos</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                font-size: 14px;
                line-height: 1.5;
            }
            .upper {
                background-color: #0d2033;
                text-align: center;
                transition: all 300ms ease;
                padding: 30px;
                color: white;
            }
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid #ccc;
                padding: 8px;
            }
            th {
                font-weight: bold;
                text-align: left;
            }
            td {
                vertical-align: top;
            }
            .pie-pagina .grupo-2 {
                width: 100%;
                background-color: #0b1620;
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                align-items: center;
                padding: 30px 50px;
            }
            .grupo-1 {
                display: flex;
                flex-wrap: wrap;
                align-items: center;
                justify-content: space-between;
                flex-basis: 50%;
            }
            .grupo-1 .box {
                flex-basis: calc(50% - 20px);
                max-width: 250px;
                margin-bottom: 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .grupo-1 .box figure {
                width: 150px;
                height: 150px;
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 50%;
                background-color: #fff;
                margin-bottom: 10px;
            }
            .grupo-1 .box figure img {
                max-width: 100%;
                max-height: 100%;
                object-fit: contain;
            }
            .grupo-1 .box h2 {
                color: #fff;
                font-size: 20px;
                margin-bottom: 10px;
            }
            .grupo-1 .box p {
                color: #efefef;
                margin-bottom: 10px;
                text-align: center;
            }
            .red-social {
                align-items: center;
            }
            .red-social a {
                display: inline-block;
                width: 45px;
                height: 45px;
                line-height: 45px;
                color: #fff;
                margin-right: 10px;
                background-color: #0d2033;
                text-align: center;
                transition: all 300ms ease;
                border-radius: 50%;
            }
            .red-social a:hover {
                color: #21ebff;
            }
            .pie-pagina .grupo-2 {
                background-color: #0a1a2a;
                padding: 15px 10px;
                margin-bottom: 0;
                text-align: center;
                color: #fff;
            }
            .pie-pagina .grupo-2 small {
                font-size: 15px;
            }
        </style>
    </head>
    <body>
        <div class="upper">
            <h1>Gracias por contactarnos, ' .$nombre. '!</h1>
            <h3>Su mensaje ha sido recibido y será respondido por nuestro equipo de soporte lo antes posible.</h3>
        </div>
        <h4>Aquí están los detalles de su mensaje:</h4>
        <table>
            <tr>
                <th>Nombre:</th>
                <td>' .$nombre. '</td>
            </tr>
            <tr>
                <th>Apellido:</th>
                <td>' .$apellido. '</td>
            </tr>
            <tr>
                <th>Email:</th>
                <td>' .$email. '</td>
            </tr>
            <tr>
                <th>Asunto:</th>
                <td>' .$asunto. '</td>
            </tr>
            <tr>
                <th>Comentario:</th>
                <td>' .$comentario. '</td>
            </tr>
        </table>
    </body>
    <footer class="pie-pagina">
        <div class="grupo-1">
            <div class="box">
                <figure>
                    <a>
                        <img src="/img/logo-zeus.png" alt="Logo de zeus">
                    </a>
                </figure>
            </div>
            <div class="box">
                <h2>SIGUENOS</h2>
                <div class="red-social">
                    <a href="https://facebook.com/" class="fab fa-facebook"></a>
                    <a href="https://instagram.com/" class="fab fa-instagram"></a>
                    <a href="https://twitter.com/" class="fab fa-twitter"></a>
                </div>
            </div>
        </div>
    </footer>
    <div class="grupo-2">
        <small>&copy; 2025 <b>CHOCOBANDA</b> - Todos los Derechos Reservados.</small>
    </div>
    </html>';

    // Enviar ambos mails
    $mail1 = @mail($destinatario1, $asunto, $cuerpo1, $header);
    $mail2 = @mail($destinatario2, $asunto, $cuerpo2, $header);

    if ($mail1 && $mail2) {
        echo "Formulario enviado con éxito.";
    } else {
        echo "Hubo un error al enviar el formulario. Por favor, inténtelo de nuevo.";
    }
}

$conn->close();
?>