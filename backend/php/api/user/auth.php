<?php
    header("Content-Type: application/json");
    if (isset($_POST["login"]) && isset($_POST["password"])) {
        require __DIR__ . "/../../config/database.php";
        $login = htmlspecialchars($database -> real_escape_string($login));
        $password = password_hash($password, PASSWORD_DEFAULT);
        $user = $database -> query("SELECT `id`, `tokens`, `pseudoId` FROM `users` WHERE `login` = {$login} AND `password` = {$password};");
        if ($user -> num_rows != 0) {
            $user = $user -> fetch_assoc();
            require __DIR__ . "/../../config/func.php";
            $token = createRandomString();
            $user["tokens"] = array_merge(json_decode($user["tokens"]), $token);
            echo json_encode([
                "message" => "ok",
                "token" => $token,
                "id" => $user["pseudoId"],
            ]);
        } else {
            http_response_code(404);
            echo json_encode([
                "message" => "user_is_not_found",
            ]);
        }
        $database -> close();
    } else {
        http_response_code(403);
        echo json_encode([
            "message" => "access_forbidden",
        ]);
    }