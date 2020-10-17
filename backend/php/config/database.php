<?php
    $connect = parse_ini_file(__DIR__ . "/../../config/database.ini");
    $database = new mysqli(
        $connect["host"],
        $connect["login"],
        $connect["password"],
        $connect["database"]
    );
    unset($connect);
    if ($database -> errno) {
        http_response_code(500);
        exit;
    }